import urllib
import chardet
fo = urllib.urlopen('http://ts.kuwo.cn/service/getlist.v31.php?act=cat&id=50&encode=%27utf-8').read()
chardit1 = chardet.detect(fo)
print chardit1['encoding']