from bs4 import BeautifulSoup
import requests
import json

news_id_li = []
test = ''
def get_news_id():
    key_word = str(input('key_word : '))
    key_word = '"' + key_word + '"'
    print('ex) 2020-02-16')
    start_date = str(input('start date : '))
    start_date = '"' + start_date + '"'
    end_date = str(input('end date : '))
    end_date = '"' + end_date + '"'
    url = "https://www.bigkinds.or.kr/api/news/search.do"
    params = '''{"indexName": "news", "searchKey": %s, "searchKeys": [{}], "byLine": "", "searchFilterType": "1", "searchScopeType": "1", "mainTodayPersonYn": "", "startDate": %s, "endDate": %s, "newsIds": [], "categoryCodes": [], "incidentCodes": [], "networkNodeType": "", "topicOrigin": "", "startNo": "1", "resultNumber": "1"}''' %(key_word, start_date, end_date)
    req = requests.post(url, data = json.dumps(eval(params)))
    sol = req.json()
    t_count =  '"' + str(sol['totalCount']) + '"'
    go_params = '''{"indexName": "news", "searchKey": %s, "searchKeys": [{}], "byLine": "", "searchFilterType": "1", "searchScopeType": "1", "mainTodayPersonYn": "", "startDate": %s, "endDate": %s, "newsIds": [], "categoryCodes": [], "incidentCodes": [], "networkNodeType": "", "topicOrigin": "", "startNo": "1", "resultNumber": %s}''' %(key_word, start_date, end_date, t_count)
    go_req = requests.post(url, data = json.dumps(eval(go_params)))
    go_sol = go_req.json()

    for tag in go_sol['resultList']:
        news_id = tag['NEWS_ID']
        news_id_li.append(news_id)

def crawl(the_list):
    for n_id in the_list:
        cl_url = "https://www.bigkinds.or.kr/news/detailView.do?docId=%s&returnCnt=1&sectionDiv=1000" %n_id
        cl_req = requests.get(cl_url)
        json_cl = cl_req.json()
        print(json_cl['detail']['CONTENT'])

get_news_id()
#print(*news_id_li, sep='\n')
#print(len(news_id_li))
#print(len(set(news_id_li)))
crawl(news_id_li)