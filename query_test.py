import httplib2
import json

def getWeatherGroup():
    url = ('http://conu.astuce.media/api/weather')
    h = httplib2.Http()
    result = json.loads(h.request(url,'GET')[1])
    print result
    return result

getWeatherGroup()
