
# 네이버 쇼핑몰 자동구매 매크로

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

# 구매 물품 link
url = 'https://brand.naver.com/samlip/products/6510954368' # 삼립 포켓몬 빵

# url = 'https://smartstore.naver.com/allchanfood/products/6362403787' # 샤니

# url = 'https://brand.naver.com/samlip/products/5841865395' #  자동 나중 결제 테스트

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

# xpath = "//div[@class='OgETmrvExa N=a:pcs.buy']/a"
# aa = driver.find_element_by_xpath(xpath).get_attribute("class")
# print("안 나오나 aa:{0}".format(aa))

# exit() # 프로그램 실행 종료

while True:
    try:
        xpath = '//a[@class="_2-uvQuRWK5"]'
        # wait_until(xpath)
        aa = driver.find_element(by=By.XPATH, value=xpath)
        # 주문 버튼 보이면 일단 주문 버튼 클릭
        aa.click()

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
        pay_value = '//button[text()="주문하기"]'
        wait_until(pay_value)
        pay_button = driver.find_element(by=By.XPATH, value=pay_value)
        pay_button.click()

        winsound.Beep(440, 1000)
        dum = input("아무키나 누르시오")
        break

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


