# coding:utf-8
import re,threading,time
from ScrolledText import ScrolledText
import urllib2,urllib


url_name=[]
def get():
   headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36'
}
   req= urllib2.Request('http://www.budejie.com/video/')
   req.add_header('user-agent',headers)
   res =urllib2.urlopen(req)
   html =res.read()
   # print html
# meg =r'<video x-webkit-airplay="allow" webkit-playsinline="" src="(.*?)"></video>'
   meg=re.compile(r'(<div class="j-r-list-c">.*?</div>.*?</div>)',re.S)
   meg2=re.findall(meg,html)
   url_reg = r'data-mp4="(.*?)">'

   for iterm in meg2:
     url_items =re.findall(url_reg,iterm)
     # print url_items
     if url_items:
         name_reg =re.compile(r'data-title="(.*?)"',re.S)
         name_items=re.findall(name_reg,iterm)
         for name,url in zip(name_items,url_items):
             url_name.append([name,url])
             print name,url

   return url_name



if __name__ =='__main__':
    a=get()
    for iterm in a:
        urllib.urlretrieve(iterm[1],'%s.mp4'%(iterm[0].decode('utf-8').encode('gbk')))
        print 'loading....%s'%iterm[0]
