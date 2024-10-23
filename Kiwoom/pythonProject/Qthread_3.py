import os                                   # 현재 디렉토리 확인 기능
from PyQt5.QtCore import *                  # 쓰레드 함수를 불러온다.
from kiwoom import Kiwoom                   # 로그인을 위한 클래스
from kiwoomType import *


class Thread3(QThread):
    def __init__(self, parent):   # 부모의 윈도우 창을 가져올 수 있다.
        super().__init__(parent)  # 부모의 윈도우 창을 초기화 한다.
        self.parent = parent      # 부모의 윈도우를 사용하기 위한 조건

        ################## 키움서버 함수를 사용하기 위해서 kiwoom의 능력을 상속 받는다.
        self.k = Kiwoom()
        ##################

        ################## 사용되는 변수
        account = self.parent.accComboBox.currentText()  # 콤보박스 안에서 가져오는 부분
        self.account_num = account
        # 계좌번호 가져오는 부분은 Qthread_3 분리 시 로그인 후 계좌번호를 가져오는 함수로 교체된다. Lecture_0529.py

        ################# 매수관련 변수
        self.Load_code()    # 매수 종목/금액/수량 가져오기

        ####### 주문 전송 시 필요한 FID 번호
        self.realType = RealType()  # 실시간 FID 번호를 모아두는 곳

        ######################################################################
        ###### 등록된 계좌 전체 해제하기(작동 정지 되었을 때 등록 정보를 다 끊어야 한다.)
        self.k.kiwoom.dynamicCall("SetRealRemove(QString, QString)", ["ALL", "ALL"])
        ######################################################################

        ######################################################################
        ###### 선정된 종목 등록하기 : 키움서버에 리얼 데이터 등록하기

        self.screen_num = 5000

        for code in self.k.portfolio_stock_dict.keys():  # 포트폴리오에 저장된 코드들을 실시간 등록
            fids = self.realType.REALTYPE['주식체결']['체결시간']  # 주식체결에 대한 모든 데이터를 로드할 수 있다.
            self.k.kiwoom.dynamicCall("SetRealReg(QString, QString, QString, QString)", self.screen_num, code, fids,
                                      "1")  # 실시간 데이터를 받아오기 위해 각 코드들을 서버에 등록(틱 변화가 있으면 데이터 송신)
            self.screen_num += 1

        ######################################################################
        ###### 현재 장 상태 알아보기 (장 시작 / 장 마감 등)
        self.screen_start_stop_real = "300"  # 장시 시작 전/후 상태 확인용 스크린 번호
        self.k.kiwoom.dynamicCall("SetRealReg(QString, QString, QString, QString)", self.screen_start_stop_real, '', self.realType.REALTYPE['장시작시간']['장운영구분'], "0")  # 장의 시작인지, 장 외인지등에 대한 정보 수신

        ###### 실시간 슬롯 (데이터를 받아오는 슬롯을 설정한다)
        self.k.kiwoom.OnReceiveRealData.connect(self.realdata_slot)  # 실시간 데이터를 받아오는 곳

    def Load_code(self):

        if os.path.exists("dist/Selected_code.txt"):
            f = open("dist/Selected_code.txt", "r", encoding="utf8")
            lines = f.readlines()   # 여러 종목이 저장되어 있다면 모든 항목을 가져온다.
            screen = 4000
            for line in lines:
                if line != "":   # 만약에 line이 비어 있지 않다면
                    ls = line.split("\t") # \t(tap)로 구분을 지어 놓는다.
                    t_code = ls[0]
                    t_name = ls[1]
                    curren_price = ls[2]
                    dept = ls[3]
                    mesu = ls[4]
                    n_o_stock = ls[5]
                    profit = ls[6]
                    loss = ls[7].split("\n")[0]
                    try:

                        self.k.portfolio_stock_dict.update({t_code: {"종목명": t_name}})
                        self.k.portfolio_stock_dict[t_code].update({"현재가": int(curren_price)})
                        self.k.portfolio_stock_dict[t_code].update({"신용비율": dept})
                        self.k.portfolio_stock_dict[t_code].update({"매수가": int(mesu)})
                        self.k.portfolio_stock_dict[t_code].update({"매수수량": int(n_o_stock)})
                        self.k.portfolio_stock_dict[t_code].update({"익절가": int(profit)})
                        self.k.portfolio_stock_dict[t_code].update({"손절가": int(loss)})
                        self.k.portfolio_stock_dict[t_code].update({"주문용스크린번호": screen}) # 아래 내용을 업데이트
                    except Exception as e:
                        # 예외가 발생했을 때 실행할 코드
                        print(f"An error occurred: {e}")

            f.close()

    def realdata_slot(self, sCode, sRealType, sRealData):

        # 실시간으로 서버에서 데이터들이 날라온다.
        if sRealType == "장시작시간":
            fid = self.realType.REALTYPE[sRealType]['장운영구분']

            # 실시간시세 데이터 수신 이벤트인 OnReceiveRealData() 가 발생될때 실시간데이터를 얻어오는 함수
            value = self.k.kiwoom.dynamicCall("GetCommRealData(QString, int)", sCode, fid)

            if value == '0':
                print("장 시작 전")

            elif value == '3':
                print("장 시작")

            elif value == '2':
                print("장 종료, 동시호가로 넘어감감")

            elif value == '4':
                print("장 마감했습니다.")