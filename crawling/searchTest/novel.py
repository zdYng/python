# coding: utf-8
#v:python2.7
import urllib2,re
import MySQLdb
import os

class Sql(object):
    conn = MySQLdb.connect(host='localhost',
                           port=3306,
                           user='root',
                           passwd='qzd123321',
                           db='booknovel',
                           charset='utf8')
    def addnovels(self,sort,novelname):
        cur = self.conn.cursor()
        cur.execute("insert into xs(sort,novelname) values(%s,'%s')" %(sort,novelname))
        cur.close()
        self.conn.commit()

    def addchapters(self,novelid,chaptername,content):
        cur =self.conn.cursor()
        cur.execute("insert into chapter(novelid,chaptername,content) values(%s,'%s','%s')" %(novelid,chaptername,content))
        cur.close()
        self.conn.commit()




headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36'
}


def getTypeList(pn=1):
    rs = r'http://www.quanshuwang.com/list/%s_1.html'%pn
    req = urllib2.Request(rs)
    # print rs
    req.headers = headers
    res = urllib2.urlopen(req)
    html = res.read().decode('gbk')
    reg = r'<a target="_blank" title="(.*?)" href="(http://www.quanshuwang.com/book.*?)" class="clearfix stitle">'
    reg = re.compile(reg)  #增加匹配速度
    # print html
    return re.findall(reg,html)
    # return html

def getNovelList(url):

    req = urllib2.Request(url)
    # print rs
    req.headers = headers
    res = urllib2.urlopen(req)
    html = res.read().decode('gbk')
    reg = r'<a href="(http://www.quanshuwang.com/book/.*?)"  class="l mr11">'
    reg=re.compile(reg)
    return re.findall(reg,html)
def getNovelList2(url):
    req = urllib2.Request(url)
    # print rs
    req.headers = headers
    res = urllib2.urlopen(req)
    html = res.read().decode('gbk')
    reg =r'<li><a href="(.*?)" title="(.*?)">'
    reg=re.compile(reg)
    return re.findall(reg,html)

def getNovelContent(url):
    req = urllib2.Request(url)
    req.headers = headers
    res = urllib2.urlopen(req)
    html =res.read().decode('gbk').encode('utf-8')
    # print html
    reg = r'&nbsp;&nbsp;&nbsp;&nbsp;(.*?)<br />'
    reg=re.compile(reg)
    return re.findall(reg,html)
if __name__ == '__main__':
    a = Sql()
    # print getTypeList(1)
    for type in range(1,10):
        # getTypeList(type)
        # print getTypeList(type)
        for title,url in getTypeList(type):
            print url,title
            t=getNovelList(url)
            # a.addnovels(type,title)
            for url2 in t:
                print url2
                # getNovelList2(url2)
                f=open('%s.txt'%title,'wb')

                for url3,chapter in getNovelList2(url2):
                    print chapter
                    url4=url2+'/'+url3
                    try:
                    # print url4
                    # try:
                    #     with open('F;\\%s\\%s.txt'%title%title,'wb')as f :
                    #       # f=open('%s.txt' %chapter, 'wb')
                       print 'loading......%s' % chapter
                       for content in getNovelContent(url4):
                               f.write(content)
                               f.write("\n")
                               f
                    except Exception,e:
                        pass
                f.close()

                        #  a.addchapters(title,chapter,content)






