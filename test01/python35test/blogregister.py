import requests
import re
import json
from bs4 import BeautifulSoup

s =requests.Session()

headers = {
    'Accept': 'application/json, text/javascript, */*;q =0.01',
    'Referer': 'http://passport.cnblogs.com/user/signin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
    'Cookie': '__gads=ID=fc58354935efbd89:T=1458638388:S=ALNI_MYEtsucyem4nWeL9mdxvQmfAZlTgQ; _ga=GA1.2.111229817.1458781632; .CNBlogsCookie=39EB7C846FF5A6CA5D762D210B954E55CE77A24D11C5203F6055DCAC93DFFF8EA7E405568F2D8CC9F00AFE43A859E71DE55AE6E79A030F7E74C231CECF7DA2DD88B734EA2ECA22DFED8C2ECAB85717B45434AABFE1202DA8266C7440562114D99D9C6767'
}

login_data = {'input1':'你的用户名加密后内容',
              'input2':'你的密码加密后内容',
              'remember': 'false'

              }
url = 'http://passport.cnblogs.com/user/signin'
req =s.post(url,data =login_data,headers=headers)
print(req.status_code)
print(req.content.decode())

f=s.get('http://home.cnblogs.com/u/whatbeg/followers/1',headers=headers)
print(f.status_code)
print(f.text)