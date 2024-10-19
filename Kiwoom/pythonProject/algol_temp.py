###############################################################
############# 실시간을 위한 조건문 구성하기 ########################
###############################################################


            #1. 매수 알고리즘 가동

            #1차#############################################################################################
            if self.k.portfolio_stock_dict[sCode]["현재가"] <= self.k.portfolio_stock_dict[sCode]["매수가"]:
                if sCode not in self.orderitmelist_1:

                    wa = []
                    wa.append(sCode)

                    if len(wa) > 1:
                        wa.clear()
                        pass
                    else:
                        print("매수 시작 %s" % sCode)

                        self.orderitmelist_1.append(sCode)  # 이 기법을 더이상 사용하지 못하게 하기
                        order_success1 = self.k.kiwoom.dynamicCall("SendOrder(QString, QString, QString ,int, QString, int, int, QString, QString)",
                                                                   ["신규매수", self.k.portfolio_stock_dict[sCode]['주문용스크린번호'], self.account_num, 1, sCode,
                                                                    self.k.portfolio_stock_dict[sCode]["매수수량"], self.k.portfolio_stock_dict[sCode]["현재가"],
                                                                    self.realType.SENDTYPE['거래구분']['지정가'], ""])

                        wf2 = open("dist/mesu_database.txt", "a", encoding="utf8")  # "a" 달아 쓴다. "w" 덮어 쓴다. files라느 파이썬 페키지 볼더를 만든다.
                        wf2.write("%s\t%s\t%s\t%s\n" % ("1매수정보", self.k.portfolio_stock_dict[sCode]["종목명"], b, self.k.portfolio_stock_dict[sCode]["채결시간"]))  # t는 tap을 의미한다.
                        wf2.close()

                        if order_success1 == 0:
                            print("최우선매수호가로 주문 전달 성공")
                        else:
                            print("최우선매수호가로 주문 전달 실패")



            #2. 매도 알고리즘 가동

            #1차 익절 #############################################################################################
            if self.k.portfolio_stock_dict[sCode]["현재가"] >= self.k.portfolio_stock_dict[sCode]["익절가"]:
                if sCode not in self.orderitmelist_2:

                    wa = []
                    wa.append(sCode)

                    if len(wa) > 1:
                        wa.clear()
                        pass
                    else:
                        print("익절 시작 %s" % sCode)

                        self.orderitmelist_2.append(sCode)  # 이 기법을 더이상 사용하지 못하게 하기
                        order_success2 = self.k.kiwoom.dynamicCall("SendOrder(QString, QString, QString ,int, QString, int, int, QString, QString)",
                                                                   ["신규익절", self.k.portfolio_stock_dict[sCode]['주문용스크린번호'], self.account_num, 2, sCode,
                                                                    self.k.portfolio_stock_dict[sCode]["매수수량"], self.k.portfolio_stock_dict[sCode]["현재가"],
                                                                    self.realType.SENDTYPE['거래구분']['지정가'], ""])

                        wf2 = open("dist/mesu_database.txt", "a", encoding="utf8")  # "a" 달아 쓴다. "w" 덮어 쓴다. files라느 파이썬 페키지 볼더를 만든다.
                        wf2.write("%s\t%s\t%s\t%s\n" % ("1익절정보", self.k.portfolio_stock_dict[sCode]["종목명"], b, self.k.portfolio_stock_dict[sCode]["채결시간"]))  # t는 tap을 의미한다.
                        wf2.close()

                        if order_success2 == 0:
                            print("익절가로 주문 전달 성공")
                        else:
                            print("익절가로 주문 전달 실패")

            #1차 손절 #############################################################################################
            if self.k.portfolio_stock_dict[sCode]["현재가"] <= self.k.portfolio_stock_dict[sCode]["손절가"]:
                if sCode not in self.orderitmelist_3:
                    wa = []
                    wa.append(sCode)

                    if len(wa) > 1:
                        wa.clear()
                        pass
                    else:
                        print("손절 시작 %s" % sCode)

                        self.orderitmelist_3.append(sCode)  # 이 기법을 더이상 사용하지 못하게 하기
                        order_success3 = self.k.kiwoom.dynamicCall("SendOrder(QString, QString, QString ,int, QString, int, int, QString, QString)",
                                                                   ["신규손절", self.k.portfolio_stock_dict[sCode]['주문용스크린번호'], self.account_num, 2, sCode,
                                                                    self.k.portfolio_stock_dict[sCode]["매수수량"], self.k.portfolio_stock_dict[sCode]["현재가"],
                                                                    self.realType.SENDTYPE['거래구분']['지정가'], ""])

                        wf2 = open("dist/mesu_database.txt", "a", encoding="utf8")  # "a" 달아 쓴다. "w" 덮어 쓴다. files라느 파이썬 페키지 볼더를 만든다.
                        wf2.write("%s\t%s\t%s\t%s\n" % ("1손절정보", self.k.portfolio_stock_dict[sCode]["종목명"], b, self.k.portfolio_stock_dict[sCode]["채결시간"]))  # t는 tap을 의미한다.
                        wf2.close()

                        if order_success3 == 0:
                            print("손절가로 주문 전달 성공")
                        else:
                            print("손절가로 주문 전달 실패")


            #미체결 잔고 매수/매도 취소 #############################################################################################
            not_meme_list = list(self.k.not_account_stock_dict)  # 체결하지 않은 종목들을 실제 미체결 잔고에서 받아온다.
            if len(self.k.not_account_stock_dict) > 0:

                for order_num in not_meme_list:  # not_meme_listnot_meme_list에는 주문번호가 들어가 있다.

                    code = self.k.not_account_stock_dict[order_num]["종목코드"]
                    meme_price = self.k.not_account_stock_dict[order_num]['주문가격']
                    not_quantity = self.k.not_account_stock_dict[order_num]['미체결수량']
                    order_gubun = self.k.not_account_stock_dict[order_num]['주문구분']

                    ##### 매수에 대한 취소 주문 : 주문가격이 최우선 매수호가보다 작을 경우

                    if order_gubun == "매수" and not_quantity > 0 and (1.01 * meme_price) < self.k.portfolio_stock_dict[sCode]["현재가"]:

                        order_success = self.k.kiwoom.dynamicCall(
                            "SendOrder(QString, QString, QString ,int, QString, int, int, QString, QString)",
                            ["매수취소", self.k.portfolio_stock_dict[sCode]['주문용스크린번호'], self.account_num, 3, code, 0, 0,
                             self.realType.SENDTYPE['거래구분']['지정가'], order_num])  # order_num 은 어떤 주문을 취소할 것인가.

                        if order_success == 0:
                            print("%s 매수취소 전달 성공" % code)  # 체결잔고에서  del을 했기 때문에 여기서 하지 않는다.
                            self.cancel_the_order.append(code)  # 차 후 재매수를 위해 필요함
                        else:
                            print("%s 매수취소 전달 실패" % code)

                        wf2 = open("dist/chiso_database.txt", "a", encoding="utf8")  # "a" 달아 쓴다. "w" 덮어 쓴다. files라느 파이썬 페키지 볼더를 만든다.
                        wf2.write("%s\t%s\t%s\t%s\n" % ("매수취소", self.k.portfolio_stock_dict[sCode]["종목명"], not_quantity, self.k.portfolio_stock_dict[sCode]["채결시간"]))  # t는 tap을 의미한다.
                        wf2.close()

                    elif not_quantity == 0:
                        del self.k.not_account_stock_dict[order_num]


                    ##### 매도에 대한 취소 주문 : 주문가격이 최우선매도호가보다 클결우

                    elif order_gubun == "매도" and not_quantity > 0 and self.k.portfolio_stock_dict[sCode]["현재가"] < (0.99 * meme_price):

                        order_success = self.k.kiwoom.dynamicCall(
                            "SendOrder(QString, QString, QString ,int, QString, int, int, QString, QString)",
                            ["매도취소", self.k.portfolio_stock_dict[sCode]['주문용스크린번호'], self.account_num, 4, code, 0, 0,
                             self.realType.SENDTYPE['거래구분']['지정가'], order_num])  # order_num 은 어떤 주문을 취소할 것인가.

                        wf2 = open("dist/chiso_database.txt", "a",
                                   encoding="utf8")  # "a" 달아 쓴다. "w" 덮어 쓴다. files라느 파이썬 페키지 볼더를 만든다.
                        wf2.write("%s\t%s\t%s\t%s\n" % ("매도취소", self.k.portfolio_stock_dict[sCode]["종목명"], not_quantity,
                                                        self.k.portfolio_stock_dict[sCode]["채결시간"]))  # t는 tap을 의미한다.
                        wf2.close()

                        if order_success == 0:
                            print("%s 매도취소 전달 성공" % code)  # 체결잔고에서  del을 했기 때문에 여기서 하지 않는다.
                            self.cancel_the_order.append(code)  # 차 후 재매수를 위해 필요함

                        else:
                            print("%s 매도취소 전달 실패" % code)

                    elif not_quantity == 0:
                        del self.k.not_account_stock_dict[order_num]



            ########################
            # 5. 재 매수 알고리즘 : 현재가가 매수 되지 못하였을 경우를 대비하여 재 매수 알고리즘 가동
            ########################
            elif sCode in self.cancel_the_order:
                # 재매수#############################################################################################
                if self.k.portfolio_stock_dict[sCode]["현재가"] <= self.k.portfolio_stock_dict[sCode]["매수가"]:
                    if sCode not in self.orderitmelist_4:
                        wa = []
                        wa.append(sCode)

                        if len(wa) > 1:
                            wa.clear()
                            pass
                        else:
                            print("재매수 시작 %s" % sCode)

                            self.orderitmelist_4.append(sCode)  # 이 기법을 더이상 사용하지 못하게 하기
                            order_success3 = self.k.kiwoom.dynamicCall(
                                "SendOrder(QString, QString, QString ,int, QString, int, int, QString, QString)",
                                ["신규매수", self.k.portfolio_stock_dict[sCode]['주문용스크린번호'], self.account_num, 1, sCode,
                                 self.k.portfolio_stock_dict[sCode]["매수수량"], self.k.portfolio_stock_dict[sCode]["현재가"],
                                 self.realType.SENDTYPE['거래구분']['지정가'], ""])

                            wf2 = open("dist/mesu_database.txt", "a",
                                       encoding="utf8")  # "a" 달아 쓴다. "w" 덮어 쓴다. files라느 파이썬 페키지 볼더를 만든다.
                            wf2.write("%s\t%s\t%s\t%s\n" % ("재매수정보", self.k.portfolio_stock_dict[sCode]["종목명"], b,
                                                            self.k.portfolio_stock_dict[sCode][
                                                                "채결시간"]))  # t는 tap을 의미한다.
                            wf2.close()
                            if order_success3 == 0:
                                print("재매수 주문 전달 성공")
                            else:
                                print("재매수 주문 전달 실패")