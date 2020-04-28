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
import os
import csv

driver = wd.Chrome('chromedriver.exe')

driver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')

time.sleep(3) #웹 페이지 로드를 보장하기 위해 3초 쉬기
#

id = 'jam_factory_0'
password = 'tlssksek12!'
id_input = driver.find_elements_by_css_selector('#react-root > section > main > div > article > div > div > div > form > div > div > label > input')[0]
id_input.send_keys(id)
password_input = driver.find_elements_by_css_selector('#react-root > section > main > div > article > div > div > div > form > div > div > label > input')[1]
password_input.send_keys(password)
password_input.submit()

time.sleep(3)
instagram_tags = []
# instagram_tag_dates = []

driver.get('https://www.instagram.com/explore/tags/대중교통')

time.sleep(3)

driver.find_element_by_css_selector('div.v1Nh3.kIKUG._bz0w').click()
try :
    for i in range(5):
        time.sleep(1)
        data = driver.find_element_by_css_selector('.C7I1f.X7jCj') # C7I1f X7jCj
        tag_raw = data.text
        tags = re.findall('#[A-Za-z0-9가-힣]+', tag_raw)
        tag = ''.join(tags).replace("#"," ") # "#" 제거
        tag_data = tag.split()

        for tag_one in tag_data:
            instagram_tags.append(tag_one)
        print(instagram_tags)
        driver.find_element_by_css_selector('a._65Bje.coreSpriteRightPaginationArrow').click()
        time.sleep(3)
except : pass
driver.close()

dataframe = pd.DataFrame(instagram_tags)
dataframe.to_csv("인스타크롤링결과2.csv", encoding='cp949')



#####################################################

# driver.find_element_by_css_selector('div.v1Nh3.kIKUG._bz0w').click()
# for i in range(76086):
#     time.sleep(1)
#     try:
#         data = driver.find_element_by_css_selector('.C7I1f.X7jCj') # C7I1f X7jCj
#         tag_raw = data.text
#         tags = re.findall('#[A-Za-z0-9가-힣]+', tag_raw)
#         tag = ''.join(tags).replace("#"," ") # "#" 제거
#         tag_data = tag.split()
#
#         for tag_one in tag_data:
#             instagram_tags.append(tag_one)
#             print(instagram_tags)
#             date = driver.find_element_by_css_selector("time.FH9sR.Nzb55" ).text # 날짜 선택
#             if date.find('시간') != -1 or date.find('일') != -1 or date.find('분') != -1:
#                 instagram_tag_dates.append('0주')
#             else:
#                 instagram_tag_dates.append(date)
#             print(instagram_tag_dates)
#     except:
#         instagram_tags.append("error")
#         instagram_tag_dates.append('error')
#     try:
#         WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a.HBoOv.coreSpriteRightPaginationArrow')))
#         driver.find_element_by_css_selector('a.HBoOv.coreSpriteRightPaginationArrow').click()
#     except:
#         driver.close()
#         # date = datum2.text
#         # #print(date)
#         time.sleep(3)
# driver.close()

#############################################################################

#
# soup = BeautifulSoup(text, 'html.parser')
#
# for div in soup.select('div.v1Nh3.kIKUG._bz0w'):
#     #url = 'https://www.instagram.com' + div.a['href']
#     image_url = div.img['src']
#     #print(url, image_url)
#
#     #print(image_url) #https://instagram.ficn6-1.fna.fbcdn.net/v/t51.2885-15/e35/c236.0.608.608a/81887242_134904677995894_2593890246933116496_n.jpg?_nc_ht=instagram.ficn6-1.fna.fbcdn.net&_nc_cat=110&_nc_ohc=PyFoOauFOggAX_qoFU8&oh=29c19b7ff0fb0c2b13304279f77566d7&oe=5ED361DB
#     file_name = image_url[image_url.rindex('/')+1:]
#     file_name = file_name[:file_name.index('?')]
#     print(file_name)
#     folder = '게임'
#     if not os.path.exists(folder):
#         os.makedirs(folder)
#     urllib.request.urlretrieve(image_url, folder + '/' + file_name)
#
# #driver.quit()