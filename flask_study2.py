# -*- coding: utf-8 -*-
"""
Created on Sat May  6 17:33:18 2017

@author: hongming
"""

from flask import Flask
app = Flask(__name__)

@app.route('/login',methods =['Get','POST'])
def login():
    if request.method == 'POST':
        do_the_login()
    else:
        show_the_login_form()
        
if __name__ =='__main__':
    app.run(host = '0.0.0.0')