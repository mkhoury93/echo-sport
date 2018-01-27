import httplib2
import json
from flask import Flask, jsonify, request, url_for, abort, g, render_template, redirect
import requests
app = Flask(__name__)

@app.route('/demo')
def demo():
    output = "<html><body><h1>Hello</h1></body></html>"
    return output


# def getAstuceCity(cityName):
#     url = ('http://conu.astuce.media/api/cities/query?short_name=%s' % (cityName))
#     h = httplib2.Http()
#     result = json.loads(h.request(url,'GET')[1])
#     template = json.dumps(result)
#     render_template('index.html', template = template)
#     return result
#     # print result
#
# getAstuceCity('Amsterdam')



# @app.route('/index', methods=['POST', 'GET'])
# def function():
#     if request.method == 'POST':
#         # # pseudo
#         # if request['sport'] == 'Basketball':
#         #     if request['use_case'] == 'PlayerStats':
#         #         # parse the necessary data from front-end
#         #         # make api call
#         #         # get json file
#         #         # return json file via flask
#         #
#         # elif request['sport'] == 'Hockey':
#         #
#         # elif request['sport'] == 'Football'
#         return null
#
#     else:
#         return render_template('index.html')
#


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
