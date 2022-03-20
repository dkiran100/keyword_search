import json
from flask import Flask, render_template, current_app, request
import requests
from script import runScript

app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/', methods = ['GET','POST'])

def index():
    if request.method == 'POST':
        keyword = request.form.get('keyword')
        ans = runScript(keyword)
    return render_template('index.html', text = ans)