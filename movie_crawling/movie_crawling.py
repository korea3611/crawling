import urllib.request

url = "http://www.naver.com/"
req = urllib.request.urlopen(url)
res = req.read()
print(res)