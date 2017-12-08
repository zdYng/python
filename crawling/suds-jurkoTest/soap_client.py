from suds.client import Client

url = 'http://ws.webxml.com.cn/WebServices/MobileCodeWS.asmx?wsdl'
client = Client(url)
for d in range(100,999):
 result = client.service.getMobileCodeInfo('130%s78927'%d)
 print result