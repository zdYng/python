import re
text = input("input email address: \n")
if re.match(r'^[0-9a-zA-Z_]{0,19}@[0-9a-zA-Z]{1,13}\.[com,cn,net]{1,3}$',text):
    print('Email address is Right!!!!')
else:
    print('please reset your Email address!!!')