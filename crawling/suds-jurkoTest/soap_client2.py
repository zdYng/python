# coding:utf-8

import numpy
import sys
reload(sys)
sys.setdefaultencoding('utf8')


from suds.client import Client
from suds.xsd.doctor import ImportDoctor,Import

url = 'http://www.webxml.com.cn/WebServices/WeatherWebService.asmx?wsdl'
imp = Import('http://www.w3.org/2001/XMLSchema.xsd',
             location='http://www.w3.org/2001/XMLSchema.xsd')
imp.filter.add('http://WebXml.com.cn/')

client = Client(url,plugins=[ImportDoctor(imp)])
result = client.service.getWeatherbyCityName("杭州")
# f = numpy.loadtxt('Weather.txt')

# f =open("Weather.txt","a")
# f.write(result)
# f.close()
print result