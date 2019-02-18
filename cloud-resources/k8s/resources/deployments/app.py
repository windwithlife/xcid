#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Goddy <wuchuansheng@yeah.net> 2018/11/5
# Desc: 

from flask import Flask, request
from flask_cors import *
import requests

app = Flask(__name__)
CORS(app, supports_credentials=True)


@app.route("/")
def test1():
    return "hi,wcm"


@app.route("/login", methods=['POST'])
def login():
    username = request.args.get('username')
    password = request.args.get('password')
    if username != "goddy" or password != "123456":
        raise Exception("用户名或密码错误")
    data = requests.post("http://127.0.0.1:31125/oauth2/token", headers={
        'Content-Type': 'application/x-www-form-urlencoded',
        'Host': 'kong-resource'
    }, data={
        'grant_type': 'password',
        'client_id': 'student-client',
        'client_secret': 'student-secret',
        'username': username,
        'password': password,
        'authenticated_userid': '123',
        'scope': 'read',
        'provision_key': 'XUscyiloz2Z19UTV8je4iFvLNGJK00j2'
    }, verify=False).text
    return data


@app.route("/test")
def test2():
    return "test111"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6000, debug=True)
