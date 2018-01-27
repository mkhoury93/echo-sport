import httplib2
import json
from flask import Flask, jsonify, request, url_for, abort, g, render_template, redirect
import requests
import string
app = Flask(__name__)

@app.route('/demo')
def demo():
    output = "<html><body><h1>Hello</h1></body></html>"
    return output

@app.route('/index', methods=['GET','POST'])
def index():
    if request.method == 'GET':
        hello = "hello"
        return render_template('build/index.html', hello = hello)
    else:
        return null

@app.route('/astuce/<string:cityName>')
def astuce(cityName):
    url = ('http://conu.astuce.media/api/cities/query?long_name=%s' % (cityName))
=======
def getAstuceCity(cityName):
    url = ('http://conu.astuce.media/api/cities/query?short_name=%s' % (cityName))>>>>>>> kim
    h = httplib2.Http()
    result = json.loads(h.request(url,'GET')[1])
    return jsonify(result)
    print result

