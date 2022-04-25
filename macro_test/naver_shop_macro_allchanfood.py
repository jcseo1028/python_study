
# 네이버 쇼핑몰 자동구매 매크로

# 올찬식탁 - 따로 항목이 있는게 아니라 다른 제품의 옵션에 빵이 들어가 있음.

# https://smartstore.naver.com/allchanfood/

# 전체 제품을 들어가면서 선택버튼 눌러서 품절되지 않는 상품을 찾아야 함. 

# <li class="-qHwcFXhj0"><a href="/allchanfood/products/4109956218" class="_3BkKgDHq3l N=a:all.product linkAnchor">
# <div class="MClmEyr46E"><span class="_3FmRUN0zLX"><span class="text blind">BEST</span></span></div><div class="_2Yq8Q_jTJv"><div class="_3VHN1dJCno"><div class="_2JNWBGd-04 _3uKZ70Wwcp EnqpMc_sIs"><img class="_25CKxIKjAk" src="https://shop-phinf.pstatic.net/20220216_137/1644994906497ReSc0_PNG/46130733997459976_13503178.png?type=f232_232" alt="삼립 쫄깃한 잉글리쉬머핀240g(4개입) 1봉/맥모닝빵 샌드위치 아침식사 간식 소풍 간편"></div></div></div><strong class="QNNliuiAk3">삼립 쫄깃한 잉글리쉬머핀240g(4개입) 1봉/맥모닝빵 샌드위치 아침식사 간식 소풍 간편</strong><div class="_23DThs7PLJ"><strong><span class="nIAdxeTzhx">900</span>원</strong></div></a><div class="_27Y22p2kob"><span class="_1ah-_dNSCu">리뷰</span><em class="_1dH1kEDaAZ">244</em><span class="_1ah-_dNSCu">평점</span><em class="_1dH1kEDaAZ">4.8</em><span class="_2V9oxVY-ye">/</span><span class="_1dH1kEDaAZ">5</span></div><button class="_2VV5LOGs4M N=a:all.mylist" type="button" aria-pressed="false"><span class="blind">찜하기</span></button><div class="_1xFgNBb3ny"><div class="_15wa8-0F_5"><button class="_3emqXg0PDV _1o5ePo58C7 N=a:all.mylist2" type="button" aria-pressed="false"><span class="blind">찜하기</span></button><button type="button" class="_3emqXg0PDV _2fW2daK-yF N=a:all.simple"><span class="blind">상품 간략보기</span></button></div></div></li>

import winsound
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pyperclip
import configparser
 
config = configparser.ConfigParser()
config.read('macro_test/config.ini')

# 네이버 로그인 정보
login_id = config['NAVER']['ID']
login_pw = config['NAVER']['PW']

# 구매 물품 link
# url = 'https://brand.naver.com/samlip/products/6510954368' # 삼립 포켓몬 빵

# url = 'https://smartstore.naver.com/allchanfood/products/6362403787' # 샤니

# url = 'https://smartstore.naver.com/allchanfood/products/4241129373' # 구매버튼 눌러지는지 테스트

# 04/21 : https://smartstore.naver.com/allchanfood/products/6470240152

url = 'https://smartstore.naver.com/allchanfood/'

# 브라우저 기동 후 네이버 이동.
driver = webdriver.Chrome('D:/chromedriver')
driver.get('https://naver.com')
time.sleep(1)

# 네이버 로그인 과정
driver.find_element_by_xpath("//a[@class='link_login']").click()
time.sleep(1)


tag_id = driver.find_element_by_name('id')
tag_id.clear()
tag_id.click()
pyperclip.copy(login_id)  ## 네이버 아이디
tag_id.send_keys(Keys.CONTROL, 'v')

tag_pw = driver.find_element_by_name('pw')
tag_pw.clear()
tag_pw.click()
pyperclip.copy(login_pw)  ## 네이버 패스워드
tag_pw.send_keys(Keys.CONTROL, 'v')
#time.sleep(1)

# 로그인 버튼을 못 찾는데...
#driver.find_element_by_id('log.ligin').click()
driver.find_element_by_xpath("//div[@class='btn_login_wrap']").click()
time.sleep(1)

# 쇼핑몰 판매 사이트로 이동.
driver.get(url)
driver.set_window_size(1200, 1080)

# 현재 페이지 내 모든 상품 링크 리스트화
li_list = driver.find_elements_by_xpath("//a[@class='_3BkKgDHq3l N=a:all.product linkAnchor']")
item_url = [] 

# 이미 링크가 확보된 사이트 우선추가
item_url.append('https://smartstore.naver.com/allchanfood/products/6470240152')
item_url.append('https://smartstore.naver.com/allchanfood/products/6445085619')
item_url.append('https://smartstore.naver.com/allchanfood/products/6445312309')
item_url.append('https://smartstore.naver.com/allchanfood/products/6507478368')
item_url.append('https://smartstore.naver.com/allchanfood/products/6445203510')

item_url.append('https://smartstore.naver.com/allchanfood/products/6317310782')
item_url.append('https://smartstore.naver.com/allchanfood/products/6316581397')
item_url.append('https://smartstore.naver.com/allchanfood/products/6316579255')
item_url.append('https://smartstore.naver.com/allchanfood/products/6316569456')
item_url.append('https://smartstore.naver.com/allchanfood/products/6316134527')

item_url.append('https://smartstore.naver.com/allchanfood/products/6333541088')
item_url.append('https://smartstore.naver.com/allchanfood/products/6507478368')
item_url.append('https://smartstore.naver.com/allchanfood/products/6470240152')
item_url.append('https://smartstore.naver.com/allchanfood/products/6445203510')
item_url.append('https://smartstore.naver.com/allchanfood/products/6469856745')
item_url.append('https://smartstore.naver.com/allchanfood/products/6445312309')
item_url.append('https://smartstore.naver.com/allchanfood/products/6445085619')
item_url.append('https://smartstore.naver.com/allchanfood/products/6317310782')
item_url.append('https://smartstore.naver.com/allchanfood/products/6316581397')
item_url.append('https://smartstore.naver.com/allchanfood/products/6316579255')
item_url.append('https://smartstore.naver.com/allchanfood/products/6316569456')
item_url.append('https://smartstore.naver.com/allchanfood/products/6316134527')

print("count : {0}".format(len(li_list)))
# time.sleep(1)
# for item in li_list:
#     item_url.append(item.get_attribute("href"))
    
print(item_url)

while True:
    for one_url in item_url:
        driver.get(one_url)
        time.sleep(0.5)    

        # 여기서 선택 버튼을 클릭 후 아이템에 원하는 상품이 있는 지 체크
        try:
            check_button = driver.find_element_by_xpath("//a[@class='bd_1fhc9 N=a:pcs.opopen']")
            check_button.click()
            time.sleep(0.5)

            items = driver.find_elements_by_xpath("//a[@class='bd_3iRne N=a:pcs.opone']")

            bFind = False
            for opt_item in items:
                if opt_item.text.find("포켓몬") != -1:
                    print(opt_item.text)
                if opt_item.text.find("포켓몬") != -1 and opt_item.text.find("품절") == -1:
                    print(opt_item.text)
                    print("04/21 : " + one_url)
                    opt_item.click()
                    winsound.Beep(440, 1000) # 주문 버튼이 나타나면 경고음 발생.
                    exit()
            
        except Exception:
            # 이건 왜 에러나는 거지 -> 단일 상품인 듯.
            print("Exception Page :" + one_url)
            continue




# xpath = "//div[@class='OgETmrvExa N=a:pcs.buy']/a"
# aa = driver.find_element_by_xpath(xpath).get_attribute("class")
# print("안 나오나 aa:{0}".format(aa))

# 이 밑에는 일단 의미 없음.
exit() # 프로그램 실행 종료

while True:
    try:
        xpath = "//div[@class='OgETmrvExa N=a:pcs.buy']/a"
        aa = driver.find_element_by_xpath(xpath).get_attribute("class")            

        if aa == '_2-uvQuRWK5':
            winsound.Beep(440, 1000) # 주문 버튼이 나타나면 경고음 발생.
            print("주문 버튼 찾았음." + time.strftime('%Y.%m.%d - %H:%M:%S'))
            break
        else:
            driver.refresh() # 브라우저 새로 고침
            print("브라우져 새로 고침." + time.strftime('%Y.%m.%d - %H:%M:%S'))
            time.sleep(1)

    except Exception:
        driver.refresh()  # 브라우저 새로 고침.
        print("in Exception 브라우져 새로 고침." + time.strftime('%Y.%m.%d - %H:%M:%S'))
        time.sleep(0.7) # 와.. 한번을 안 걸리네;;;


