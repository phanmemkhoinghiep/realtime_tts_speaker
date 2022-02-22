#!/usr/bin/env python
# -*- coding: utf-8 -*-
#-*-coding:gb2312-*-
from flask import Flask, request, jsonify, render_template, render_template_string
import time
# import imp
import sys
import json
import tts
app = Flask(__name__)


@app.route('/')

def text_input():
    return render_template('input.html')

@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    processed_text = text.lower()    
    try:
        tts.main(True,text)
        speak_result = 'Not OK'
    except:
        speak_result = 'Not OK'
    return render_template('input.html')

        
@app.route('/api', methods=['GET', 'POST'])

def api_input():
    if request.method == 'GET':
        return jsonify({'message' : 'Realtime Speaker API v1.0'})          
    if request.method == 'POST':        
        payload = request.get_json()
        text=payload['data']
        speak_result =''
        try:
            tts.main(True,text)
            speak_result = 'Not OK'
        except:
            speak_result = 'Not OK'
        return speak_result

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True, host='0.0.0.0', port=5000)
