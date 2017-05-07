# -*- coding: utf-8 -*-
"""
Created on Sat May  6 16:13:31 2017

@author: hongming
"""
from flask import Flask

# virtualenv 的安装

# sudo apt-get install python-virtualenv

# 激活

'''
1. 建立文件夹  mkdir project_name

2. 进入相应的文件夹 cd project_name

3. 激活 . enve/bin/activate

4.然后可以在该系统安装所需第三方库


'''

app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')

def hello():
    return 'Hello homing'

if __name__ =='__main__':
    app.run(host = '0.0.0.0')
