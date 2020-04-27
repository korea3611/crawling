#######별점과 리뷰 출력하기###########
from bs4 import BeautifulSoup
from urllib.request import urlopen

test_url = "https://movie.naver.com/movie/point/af/list.nhn?st=mcode&sword=136873&target=after&page=1"
page = urlopen(test_url)
soup = BeautifulSoup(page, 'html.parser')
for tag in soup.select('td[class=title]'):
    print(tag.text.strip())
