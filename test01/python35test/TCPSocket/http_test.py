import urllib.request


try:
    response = urllib.request.urlopen('http://www.baidu.com').read()
    #isRed = response.geturl()
    #print(isRed)
except urllib.request.HTTPError as e:
    if hasattr(e,'code'):
        print('Error code:',e.code)