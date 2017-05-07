# -*- coding: utf-8 -*-
"""
Created on Sat May  6 17:01:55 2017

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

@app.route('/user/<username>')

def show_user_profile(username):
    return 'User %s' %username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return 'Post: %d'%post_id



if __name__ =='__main__':
    app.run(debug= True)
