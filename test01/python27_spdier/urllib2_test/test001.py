import urllib
try:
   response = urllib.request.urlopen('http://www.baidu.com')
   print(response