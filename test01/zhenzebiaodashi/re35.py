import re
text = input("Please input your email address:\n")
if re.match(r'[0-9a-zA-Z_]{0,19}@163.com',text):
    print('Email address is right!!!!')
else:
    print('Please reset your right Email address!!!!')