#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, request
from flask import render_template
import json
import datetime
import os
from termcolor import colored
import time
import tts

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def speaking():
    """
    Send a POST request to localhost:5000/webhook with a JSON body with a "p" key
    to print that message in the server console.
    """
    payload = request.get_json()
    text=payload['data']
    speak_result =''
    try:
        tts.tts_vietnamese(False,text)
        speak_result = 'Not OK'
    except:
        speak_result = 'Not OK'
    return speak_result

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
