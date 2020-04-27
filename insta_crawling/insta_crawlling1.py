
import urllib
from urllib.request import urlopen, Request

import requests
from bs4 import BeautifulSoup
from selenium import webdriver as wd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import re
import pandas as pd
import urllib.parse
from selenium.webdriver.common.keys import Keys

# 인스타그램 로그인 URL
loginUrl = "https://www.instagram.com/accounts/login/"      # 로그인 페이지 설정

# driver load

options = wd.ChromeOptions()             # webdriver 옵션 설정
mobile_emulation = {"deviceName": "Nexus 5"}    # -- 여기서는 모바일 버전(넥서스5)으로 들어가도록 설정함
options.add_experimental_option("mobileEmulation", mobile_emulation)

driver = wd.Chrome('chromedriver.exe', chrome_options=options)       # webdriver 띄우고
driver.get(loginUrl)        # 로그인 페이지로 이동하도록 함

time.sleep(2)       # 잠시 쉬는타임

driver.find_elements_by_name("username")[0].send_keys("jam_factory_0")        # find_elements_by_name과 send_keys를 이용해서 값을 입력
driver.find_elements_by_name("password")[0].send_keys("tlssksek12!")

driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div/div/div/form/div[7]/button").submit()      # Login 버튼 누르기
time.sleep(2)

driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div/button").click()       # "로그인 정보를 저장하시겠습니까? (아니오)' 누르기
time.sleep(2)

driver.find_element_by_xpath("/html/body/div[4]/div/div/div[3]/button[2]").click()              # 홈화면 설정 -> 취소
time.sleep(2)

# search_box = driver.find_element_by_css_selector("input.XTCLo x3qfX")
# search_box.send_keys("오색시장")
# driver.find_element_by_name("Value").send_keys(Keys.ENTER)



# search = input("검색어를 입력하시오")
# search = urllib.parse.quote(search)
# url = 'https://www.instagram.com/explore/tags/'+str(search)+'/'
# driver = wd.Chrome('chromedriver.exe')
# driver.get(url)
#
# SCROLL_PAUSE_TIME = 1.0
# reallink = []
#
# while True:
#     pageString = driver.page_source
#     bsObj = BeautifulSoup(pageString, "lxml")
#
#     for link1 in bsObj.find_all(name="div", attrs={"class":"Nnq7C weEfm"}):
#         title = link1.select('a')[0]
#         real = title.attrs['href']
#         reallink.append(real)
#         title = link1.select('a')[1]
#         real = title.attrs['href']
#         reallink.append(real)
#         title = link1.select('a')[2]
#         real = title.attrs['href']
#         reallink.append(real)
#
#     last_height = driver.execute_script("return document.body.scrollHeight")
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#     time.sleep(SCROLL_PAUSE_TIME)
#     new_height = driver.execute_script("return document.body.scrollHeight")
#
#
#     if new_height == last_height:
#         driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#         time.sleep(SCROLL_PAUSE_TIME)
#         new_height = driver.execute_script("return document.body.scrollHeight")
#         if new_height == last_height:
#             break
#
#         else:
#             last_height == new_height
#             continue
#
#     for i in range(0, len(reallink)):
#         csvtext.append([])
#         req = Request('https://www.instagram.com/p' + reallink[i], headers = {'User-Agent' : 'Mozilla/5.0'})
#
#         webpage = urlopen(req).read()
#         soup = BeautifulSoup(webpage,"lxml", from_encoding='utf-8')
#         soup1 = soup.find("meta", attrs={"property":"og:description"})
#
#         reallink1 = soup1['content']
#         reallink1 = reallink1[reallink1.find('@')+1:reallink1.find(")")]
#         reallink1 = reallink1[:20]
#         if reallink1 == '':
#             reallink1 = 'Null'
#         csvtext[i].append(reallink1)
#
#         for reallink2 in soup.find_all("meta", attrs={"property":"instapp:hashtags"}):
#             reallink2 = reallink2['content']
#             csvtext[i].append(reallink2)
#
#     data = pd.DataFrame(csvtext)
#     data.to_csv('insta.txt', encoding='utf-8')