import winsound
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pyperclip
import configparser
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def wait_until(xpath_str):
    WebDriverWait(driver, 30).until(EC.presence_of_all_elements_located((By.XPATH, xpath_str)))

config = configparser.ConfigParser()
config.read('macro_test/config.ini')

# 네이버 로그인 정보
login_id = config['NAVER']['ID']
login_pw = config['NAVER']['PW']

# url = 'https://smartstore.naver.com/allchanfood/'

url = 'https://smartstore.naver.com/allchanfood/products/6362403787'

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

# 로그인 버튼
driver.find_element(by=By.XPATH, value="//div[@class='btn_login_wrap']").click()
time.sleep(1)

today_link = ''
str_today = time.strftime('/%d')
print(str_today)

# str_today = '/13'
bTodayEnd = False

while True:

    # 쇼핑몰 판매 사이트로 이동.
    driver.get(url)
    #driver.set_window_size(400, 1080)

    # 판매링크 찾기
    # xpath = '//div[@class="_1M8sTqCNYM"]'
    # wait_until(xpath)
    # today_link = driver.find_element(by=By.XPATH, value=xpath)

    try:
        xpath = '//div[@class="se-module se-module-text"]'
        wait_until(xpath)
        today_link = driver.find_element(by=By.XPATH, value=xpath)
        # print(today_link.text)
        text_inform = today_link.text
        list_text = text_inform.split('\n')
        # print(list_text)
        # print(list_text[len(list_text)-1])

        if text_inform.find('종료') >= 0 and text_inform.find(str_today) >= 0 :
            driver.execute_script("window.scrollTo(0, 3500)")
            print("오늘 판매 종료")
            bTodayEnd = True
            break
            exit()
        if text_inform.find(str_today) >= 0: # 오늘자 공지가 있음.
            today_link = list_text[len(list_text)-1]
            print(today_link)
            break    
        else :
            print("아직 오늘자 공지 없음..." + time.strftime('%Y.%m.%d - %H:%M:%S'))
            time.sleep(0.3)
    except Exception:
        # 가끔 페이지 안 뜨는 경우 있음.
        print("페이지 이상...1-" + time.strftime('%Y.%m.%d - %H:%M:%S'))
        time.sleep(0.3)

if bTodayEnd == True:
    exit()
print("여기 왔나? " + today_link)

while True:
    driver.get(today_link)

    try:
        # 체크박스 확인
        xpath = '//a[@class="bd_1fhc9 N=a:pcs.opopen"]'
        wait_until(xpath)
        check_button = driver.find_element(by=By.XPATH, value=xpath)    
        check_button.click()

        # 품절여부 확인
        xpath = '//a[@class="bd_3iRne N=a:pcs.opone"]'
        wait_until(xpath)
        items = driver.find_elements(by=By.XPATH, value=xpath)
        for opt_item in items:
            if opt_item.text.find("포켓몬") != -1:
                    print(opt_item.text)
            if opt_item.text.find("포켓몬") != -1 and opt_item.text.find("품절") == -1:
                print(opt_item.text)
                opt_item.click()
                
                #winsound.Beep(440, 1000) # 주문 버튼이 나타나면 경고음 발생.

                # 구매버튼 클릭.
                pur_button = driver.find_element(by=By.XPATH, value='//a[@class="_2-uvQuRWK5"]')
                pur_button.click()

                # 결제하기 버튼이 나타날 때까지 대기.
                pay_value = '//button[text()="결제하기"]'
                wait_until(pay_value)

                # 일반 결제로 변경
                xpath = '//label[text()="일반결제"]'
                aa = driver.find_element(by=By.XPATH, value=xpath)
                aa.click()
                time.sleep(0.5)

                # 나중 결제로 변경
                xpath = '//label[@class="_payMeanSkipLabel"]'
                wait_until(xpath)
                aa = driver.find_element(by=By.XPATH, value=xpath)
                aa.click()
                #time.sleep(0.5)

                #dum = input("아무키나 누르시오")
                # r
                pay_value = '//button[text()="주문하기"]' # 결제 방식에 따라 주문하기 또는 결제하기로 Text 바뀜.
                wait_until(pay_value)
                pay_button = driver.find_element(by=By.XPATH, value=pay_value)
                pay_button.click()

                winsound.Beep(440, 1000) # 주문 버튼이 나타나면 경고음 발생.
                break
    except Exception:
        print("페이지 이상...2-" + time.strftime('%Y.%m.%d - %H:%M:%S'))
        time.sleep(0.3)
