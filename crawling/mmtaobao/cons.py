# -*- coding: utf-8 -*-
#!/usr/bin/env python
import random
headerstr = '''Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11
Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; The World)'''

def headers():
    header =headerstr.split('\n')
    length =len(header)
    return header[random.randint(0,length-1)]