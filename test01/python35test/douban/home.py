import urllib.request

url = "http://www.douban.com"

request = urllib.request.Request(url)
response = urllib.request.urlopen(request)
data = response.read().decode('utf-8')
#print(data)
urllib.request.urlretrieve(url,"text.html")


