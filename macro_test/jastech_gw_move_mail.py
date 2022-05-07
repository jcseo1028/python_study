from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
import pyperclip
import configparser
from selenium.webdriver.common.by import By
 
config = configparser.ConfigParser()
config.read('macro_test/config.ini')

# 그룹웨어 로그인 정보
login_id = config['JAS_GW']['ID']
login_pw = config['JAS_GW']['PW']

# 브라우저 기동 후 그룹웨어 이동.
driver = webdriver.Chrome('D:/chromedriver')


driver.get('http://gw.jastech.co.kr/')
time.sleep(1)

#//*[@id="login_b1_type"]/div[2]/div[2]/form/fieldset

#//*[@id="userId"]

# 로그인 과정


# tag_id = driver.find_element_by_name('id')
tag_id = driver.find_element(by=By.NAME, value='id')

tag_id.clear()
tag_id.click()
pyperclip.copy(login_id)  ## ID
tag_id.send_keys(Keys.CONTROL, 'v')

tag_pw = driver.find_element(by=By.NAME, value='password')
tag_pw.clear()
tag_pw.click()
pyperclip.copy(login_pw)  ## PW
tag_pw.send_keys(Keys.CONTROL, 'v')
#time.sleep(1)

tag_loginbtn = driver.find_element(by=By.CLASS_NAME, value='login_submit')
tag_loginbtn.click()
time.sleep(0.5)

# 메일함 가기
tag_mail = driver.find_element(by=By.ID, value='topMenu200000000')
tag_mail.click()
time.sleep(0.5)

# 특정 text 를 가지는 Button 찾기
find_button = driver.find_element(by=By.XPATH, '//button[text() = "가는날"]') # 전체 Element(//) 에서 Text 가 "가는 날" 인 button element 찾기

# 내 편지함 가기
# tag_mymail = driver.find_element(by=By.CLASS_NAME, value='lbl_mymailbox')
# tag_mymail = driver.find_element_by_class_name('lbl_mymailbox')

# tag_mymail = driver.find_element(by=By.ID, value='myMailBox')
# //*[@id="myMailBox"]/span
# //*[@id='myMailBox']
# //*[@id="myMailBox"]/span/em[1]
# //*[@id="allbox"]
# //*[@id="sub_nav_jstree"]
# tag_mymail = driver.find_elements(by=By.XPATH, value='//*[@id="sub_nav_jstree"]')
# print("어디갔니? ")
# print(tag_mymail)

# Java Scrip 로 생성된 Tag 를 찾는 방법?

html = driver.page_source
# print(html)
soup = BeautifulSoup(html, 'html.parser')

menus = soup.select('div.sub_nav_jstree > div.elements')
print(menus)

exit()


tag_mymail.click()
time.sleep(0.5)

# 기존 메일함 이동
tag_old_mail = driver.find_element(by=By.ID, value='1779_sel')
tag_old_mail.click()
time.sleep(0.5)