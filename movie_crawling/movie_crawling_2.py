from bs4 import BeautifulSoup
from urllib.request import urlopen

###source = BeautifulSoup(webpage,'html.parser', from_encoding='utf-8')
webpage = urlopen(' https://movie.naver.com/movie/point/af/list.nhn?st=mcode&sword=136873&target=after&page=1')
source = BeautifulSoup(webpage,'html.parser', from_encoding='utf-8')
review_list = source.findAll('td',{'class':'title'})

print(review_list)