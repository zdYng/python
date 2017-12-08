import urllib,httplib2
github_url = 'www.github/'
h = httplib2.Http(".cache")
h.add_credent.ials("user","******",""
data = urllib.urlencode({"name":"test"})
resp,content = h.request(github_url,"POST",data)
print(content)