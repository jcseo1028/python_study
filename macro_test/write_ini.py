
import configparser

config = configparser.ConfigParser()

config['NAVER'] = {}
config['NAVER']['ID'] = "ID"
config['NAVER']['PW'] = "PW"

with open('macro_test/config.ini', 'w') as configfile:
    config.write(configfile)

# 출처: https://devnauts.tistory.com/197 [devnauts]