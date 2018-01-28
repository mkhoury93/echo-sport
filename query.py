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
        return render_template('index.html', hello = hello)

@app.route('/astuce/<string:cityName>', methods=['POST','GET'])
def astuce(cityName):
    if request.method == 'GET':
        url = ('http://conu.astuce.media/api/cities/query?long_name=%s' % (cityName))
        h = httplib2.Http()
        result = json.loads(h.request(url,'GET')[1])
        return jsonify(result)
        print result

@app.route('/requests/', methods=['GET','POST'])
def requestCity():
    if request.method == 'POST':
        cityName = request.form['cityName']
        return redirect(url_for('astuce', cityName = cityName))
    elif request.method =='GET':
        return render_template('requests.html')

@app.route('/hockey/player', methods=['GET','POST'])
def requestHockeyPlayerStats():
    if request.method == 'GET':
        return render_template('getHockeyPlayers.html')
    elif request.method == 'POST':
        games = request.form['games']
        points = request.form['points']
        age = request.form['age']
        return redirect(url_for('getHockeyPlayerStatus', age=age, games=games, points=points))

@app.route('/hockey/player/<int:age>/<int:games>/<int:points>')
def getHockeyPlayerStatus(games, age, points):
    url = ('http://conu.astuce.media/api/sports/hockey/gfx/statistic/person/ranking.json?Stat=SkatingGamesPlayed&SkatingGamesPlayed=%s&age=%s&SkatingPointsTotal=%s&take=2' % (games, age, points))
    h = httplib2.Http()
    result = json.loads(h.request(url,'GET')[1])
    print "what's going on "
    return jsonify(result)

#
# @app.route('/astuce/<string:cityName>')
# def getAstuceCity(cityName):
#     url = ('http://conu.astuce.media/api/cities/query?short_name=%s' % (cityName))
#     h = httplib2.Http()
#     result = json.loads(h.request(url,'GET')[1])
#     return result
    #template = json.dumps(result)
    #render_template('index.html', template = template)

    # print result
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
