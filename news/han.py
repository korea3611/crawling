import requests
from bs4 import BeautifulSoup


url_front = 'http://search.hani.co.kr/Search?command=query&keyword=%EC%BD%94%EB%A1%9C%EB%82%98&media=news&submedia=&sort=d&period=all&datefrom=2000.01.01&dateto=2020.04.17&pageseq=1'
url_page_num = 0
full_url = url_front + str(url_page_num)
req = requests.get(full_url)
html = req.text
soup = BeautifulSoup(html, 'html.parser')
for tag in soup.select('dd.detail'):
    sol = tag.text
    print(sol)