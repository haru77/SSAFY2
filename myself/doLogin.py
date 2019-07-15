import requests
import bs4
from selenium import webdriver
from decouple import config

chromedriver_dir = r'C:\Users\student\Downloads\chromedriver_win32\chromedriver.exe'
driver = webdriver.Chrome(chromedriver_dir)

inputusername = config("USER_ID") #사용자이름
inputuserpwd  = config("USER_PWD") #사용자 비밀번호

loginurl = "https://edu.ssafy.com/comm/login/SecurityLoginForm.do"
driver.get(loginurl)
username = driver.find_element_by_id("userId")
username.clear()
username.send_keys(inputusername)
password = driver.find_element_by_id("userPwd")
password.clear()
password.send_keys(inputuserpwd)

#driver.find_element_by_name("로그인").click()
#driver.find_element_by_link_text("로그인").click()
#driver.find_element_by_class_name("form-btn").click()
driver.find_element_by_css_selector("#wrap > div > div > div.section > form > div > div.field-set.log-in > div.form-btn > a").click()

#로그인 과정 완료
sessionurl = "http://edu.ssafy.com/edu/main/index.do"
driver.get(sessionurl)

xpath = '//*[@id="_mainComunityId"]/div[2]/div[1]/article/a/span' # 알림

xpath = '//*[@id="checkIn"]/span' #입실
#xpath = '//*[@id="checkOut"]/span'   #퇴실

#checkoutkey = driver.find_element_by_id("checkOut").click()


btn = driver.find_element_by_xpath(xpath)
# 자바 스크립트가 있을 경우에는 실행 코드를 넣어줘야함.
# http://blog.naver.com/PostView.nhn?blogId=kiddwannabe&logNo=221430636045&categoryNo=0&parentCategoryNo=0&viewDate=&currentPage=1&postListTopCurrentPage=1&from=postView
driver.execute_script("arguments[0].click();", btn)
