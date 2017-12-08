import urllib2
import requests
headers={"user-agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36"}
html ="https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90"
req = urllib2.Request(html)
req.headers=headers
psot_param = {'action':'','start':'1','limit':'2'}
return_data =requests.get(html,psot_param,verify=False)
print return_data.text
