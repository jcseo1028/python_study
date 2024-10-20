import sys                        # system specific parameters and functions : 파이썬 스크립트 관리
from PyQt5.QtWidgets import *     # GUI의 그래픽적 요소를 제어       하단의 terminal 선택, activate py37_32,  pip install pyqt5,   전부다 y
from PyQt5 import uic             # ui 파일을 가져오기위한 함수
from PyQt5.QtCore import *
import os                         # 운영체제와 상호작용하기 위한 함수

################# 부가 기능 수행(일꾼) #####################################
from kiwoom import Kiwoom          # 키움증권 함수/공용 방 (싱글턴)
from Qthread_1 import Thread1      # 계좌평가 잔고내역 가져오기
from Qthread_2 import Thread2      # 계좌 관리

#=================== 프로그램 실행 프로그램 =========================#

# Get the absolute path of the current file
current_dir = os.path.dirname(os.path.abspath(__file__))
ui_path = os.path.join(current_dir, "ALBA.ui")

form_class = uic.loadUiType(ui_path)[0]             # 만들어 놓은 ui 불러오기

class Login_Machnine(QMainWindow, QWidget, form_class):       # QMainWindow : PyQt5에서 윈도우 생성시 필요한 함수

    def __init__(self, *args, **kwargs):                      # Main class의 self를 초기화 한다.

        print("Login Machine 실행합니다.")
        super(Login_Machnine, self).__init__(*args, **kwargs)
        form_class.__init__(self)                            # 상속 받은 from_class를 실행하기 위한 초기값(초기화)
        self.setUI()                                         # UI 초기값 셋업 반드시 필요

        ### 초기 셋팅
        self.label_11.setText(str("총매입금액"))
        self.label_12.setText(str("총평가금액"))
        self.label_13.setText(str("추정예탁자산"))
        self.label_14.setText(str("총평가손익금액"))
        self.label_15.setText(str("총수익률(%)"))

        ####기타함수
        self.login_event_loop = QEventLoop()  # QEventLoop 객체 초기화

        ####키움증권 로그인 하기
        self.k = Kiwoom()                     # Kiwoom()을 실행하며 상속 받는다. Kiwoom()은 전지적인 아이다.

        self.set_signal_slot()
        self.signal_login_commConnect()

        #### 이벤트 생성 및 진행
        self.call_account.clicked.connect(self.c_acc)   # 계좌 정보 가져오기
        self.acc_manage.clicked.connect(self.a_manage)  # 계좌 관리하기

    def setUI(self):
        self.setupUi(self)                # UI 초기값 셋업

    def set_signal_slot(self):
        self.k.kiwoom.OnEventConnect.connect(self.login_slot)

    def signal_login_commConnect(self):
        self.k.kiwoom.dynamicCall("CommConnect()")
        self.login_event_loop.exec_()

    def login_slot(self, errCode):
        if errCode == 0:
            print("로그인 성공")
            self.statusbar.showMessage("로그인 성공")
            self.get_account_info()     # 로그인 시 계좌정보 가져오기

        elif errCode == 100:
            print("사용자 정보교환 실패")

        elif errCode == 101:
            print("서버접속 실패")

        elif errCode == 102:
            print("버전처리 실패")

        self.login_event_loop.exit()    # 로그인이 완료되면 로그인 창을 닫는다.

    def get_account_info(self):
        account_list = self.k.kiwoom.dynamicCall("GetLoginInfo(String)", "ACCNO")

        for n in account_list.split(';'):
            self.accComboBox.addItem(n)

    def c_acc(self):
        print("선택 계좌 정보 가져오기")
        ##### 1번 일꾼 실행
        h1 = Thread1(self)
        h1.start()

    def a_manage(self):
        print("계좌 관리")
        h2 = Thread2(self)
        h2.start()

if __name__=='__main__':             # import된 것들을 실행시키지 않고 __main__에서 실행하는 것만 실행 시킨다.
                                     # 즉 import된 다른 함수의 코드를 이 화면에서 실행시키지 않겠다는 의미이다.

    app = QApplication(sys.argv)     # PyQt5로 실행할 파일명을 자동으로 설정, PyQt5에서 자동으로 프로그램 실행
    CH = Login_Machnine()            # Main 클래스 myApp으로 인스턴스화
    CH.show()                        # myApp에 있는 ui를 실행한다.
    app.exec_()                      # 이벤트 루프
