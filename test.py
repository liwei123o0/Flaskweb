# -*- coding: utf-8 -*-
#! /usr/bin/env python
from flask import Flask
import json
app =Flask(__name__)

@app.route("/")
def list():
    a = [1,2,3,4]
    print type(json.dumps(a))
    return json.dumps(a)
if __name__=="__main__":
    app.run(host='127.0.0.1',debug=True)