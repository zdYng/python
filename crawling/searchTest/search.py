# -*- coding: utf-8 -*-
from flask import Flask

app = Flask(__name__)  #__name__ == '__main__'

@app.route('/')  #装饰器 给函数增加功能
def index():
    return 'HelloWorld!!'

@app.route('/home')
def home():
    return 'Hello Home'

if __name__ =='__main__':
    app.run ()
