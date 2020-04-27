#######별점 뽑기#########
from bs4 import BeautifulSoup
from urllib.request import urlopen

test_url = "https://movie.naver.com/movie/point/af/list.nhn?st=mcode&sword=136873&target=after&page=%d"
page = urlopen(test_url)
soup = BeautifulSoup(page, 'html.parser')
for tag in soup.select('div[class=list_netizen_score]'):
    print(tag.text.strip())


