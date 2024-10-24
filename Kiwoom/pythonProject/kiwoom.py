from PyQt5.QtWidgets import *
from PyQt5.QAxContainer import *
from PyQt5Singleton import Singleton

class Kiwoom(QWidget, metaclass=Singleton):
    def __init__(self, parent=None, **kwargs):
        print("로그인 프로그램을 실행합니다.")
        super().__init__(parent, **kwargs)

        ########## 로그인 관련 정보
        self.kiwoom = QAxWidget('KHOPENAPI.KHOpenAPICtrl.1')

        ########## 전체 공유 데이터
        self.All_Stock_Code = {}            # 코스피, 코스닥 전체 코드넘버 입력
        self.acc_portfolio = {}             # 계좌에 들어있는 종목의 코드, 수익률 등등 입력
        self.portfolio_stock_dict = {}      # 매매에 관한 모든 종목(현재계좌 종목.금일 등록 종목)이 모두 들어간다.

        self.today_meme = {}                # 금일 매매하는 종목에 대하여 들어간다.
        self.not_account_stock_dict = {}    # 미체결 잔고

        ########## 금일 잔고
        self.jango_dict = {}                #
        self.buy_jogon = {}                 # 미체결 잔고


