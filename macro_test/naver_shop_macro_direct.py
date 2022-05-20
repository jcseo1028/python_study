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
from selenium.webdriver.common.alert import Alert

def wait_until(xpath_str):
    WebDriverWait(driver, 30).until(EC.presence_of_all_elements_located((By.XPATH, xpath_str)))
 
config = configparser.ConfigParser()
config.read('macro_test/config.ini')

# 네이버 로그인 정보
login_id = config['NAVER']['ID']
login_pw = config['NAVER']['PW']

# 구매 물품 link

# 아래 링크 사용하면 구매하기 버튼 안 기다리고 바로 주문화면으로 들어갈 수 있음.  판매자 ID(510440774) 는 어떻게 알 수 있지? 
# https://m.pay.naver.com/o/products/510440774/6510954368/purchase?from=https://m.pay.naver.com/

url = 'https://m.pay.naver.com/o/products/510440774/6510954368/purchase?from=https://m.pay.naver.com/'

# url = 'https://m.pay.naver.com/o/products/510440774/5841865395/purchase?from=https://m.pay.naver.com/' # 다른 상품 테스트

# 6040884446, 짱구
url = 'https://m.pay.naver.com/o/products/510440774/6040884446/purchase?from=https://m.pay.naver.com/'

# 브라우저 기동 후 네이버 이동.
driver = webdriver.Chrome('D:/chromedriver')
driver.get('https://naver.com')
time.sleep(1)

# 네이버 로그인 과정
xpath = '//a[@class="link_login"]'
#driver.find_element_by_xpath("//a[@class='link_login']").click()
log_btn = driver.find_element(by=By.XPATH, value=xpath)
log_btn.click()
time.sleep(1)

tag_id = driver.find_element(by=By.NAME, value='id')
tag_id.clear()
tag_id.click()
pyperclip.copy(login_id)  ## 네이버 아이디
tag_id.send_keys(Keys.CONTROL, 'v')

tag_pw = driver.find_element(by=By.NAME, value='pw')
tag_pw.clear()
tag_pw.click()
pyperclip.copy(login_pw)  ## 네이버 패스워드
tag_pw.send_keys(Keys.CONTROL, 'v')
#time.sleep(1)

# 로그인 버튼을 못 찾는데...
#driver.find_element_by_id('log.ligin').click()
driver.find_element(by=By.XPATH, value="//div[@class='btn_login_wrap']").click()
time.sleep(1)

while True:
    # 쇼핑몰 판매 사이트로 이동.
    driver.get(url)
    #driver.set_window_size(1200, 1080) # 알람 떴을 때 제어하면 에러.

    try:
        msg = Alert(driver) # 알람이 안 떴을 경우에는 해당 구문에서 Exception 발생함.
        msg.accept() # 경고창 확인

        time.sleep(0.5)
        print("in Alert Accepted..." + time.strftime('%Y.%m.%d - %H:%M:%S'))
        
    except Exception:
        #확인 버튼 찾기.
        xpath = '//div[text()="확인"]'
        wait_until(xpath)
        btn = driver.find_element(by=By.XPATH, value=xpath)
        btn.click()
        #time.sleep(0.5)

        
        #driver.set_window_size(400,1080)
        #driver.execute_script("window.scrollTo(0, 1000)")
        
        # 일반 결제로 변경
        # xpath = '//label[text()="일반결제"]'
        xpath = '//label[@class="N=a:ode.paygeneral radio_label _payment_label _click(checkout.mobile.order.order_sheet.switchPaymentMethodTab(GENERAL)) _stopDefault"]'

        wait_until(xpath)
        ab = driver.find_element(by=By.XPATH, value=xpath)
        ab.click()
        #time.sleep(0.5)
        

        # 나중 결제로 변경
        xpath = '//strong[text()="나중에 결제"]'
        wait_until(xpath)
        aa = driver.find_element(by=By.XPATH, value=xpath)
        aa.click()
        #time.sleep(0.5)
        

        #dum = input("아무키나 누르시오")
        # pay_value = '//button[text()="주문하기"]'
        pay_value = '//a[@class="N=a:ode.pay btm_button _click(checkout.mobile.order.order_sheet.create()) _stopDefault _doPayButton"]'
        wait_until(pay_value)
        pay_button = driver.find_element(by=By.XPATH, value=pay_value)
        pay_button.click()

        winsound.Beep(440, 1000)
        exit()

        break









