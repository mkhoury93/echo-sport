import httplib2
import json

def getAstuceCity(cityName):
    url = ('http://conu.astuce.media/api/cities/query?short_name=%s' % (cityName))
    h = httplib2.Http()
    result = json.loads(h.request(url,'GET')[1])
    print result

getAstuceCity('Amsterdam')
