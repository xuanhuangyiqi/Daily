from config import baidu_key
import json
import time
import math
import urllib

baidu_api_url = 'http://api.map.baidu.com/geocoder/v2/?ak=%s&callback=renderReverse&location=%s,%s&output=json&pois=1'

def time_generator(t):
    return time.strftime("%m-%d %H:%M",time.localtime(t)) 

def addr_generator(dict_resp):
    res = ''
    d = dict_resp['result']
    if d['formatted_address']:
        res += d['formatted_address']
    else:
        res += d['addressComponent']['city']
    if d['pois']:
        res += d['pois'][0]['name']
    return res

def to_baidu(mars_dict):
    x_pi = 3.14159265358979324 * 3000.0 / 180.0
    res = {}
    y = float(mars_dict['lat'])
    x = float(mars_dict['lon'])
    z = math.sqrt(x * x + y * y) + 0.00002 * math.sin(y * x_pi)
    theta = math.atan2(y, x) + 0.000003 * math.cos(x * x_pi)
    bd_lon = z * math.cos(theta) + 0.006
    bd_lat = z * math.sin(theta) + 0.0165
    bd_lon, bd_lat = bd_lat, bd_lon
    return {'lon':str(bd_lat), 'lat':str(bd_lon)}

def location_filter(locs):
    res = []
    for x in locs:
        it = to_baidu(json.loads(x['content']))
        json_resp = urllib.urlopen(baidu_api_url%(baidu_key, it['lon'], it['lat'])).read()[29:-1]
        addr = addr_generator(json.loads(json_resp))
        t = time_generator(x['create_time'])
        if not res or addr != res[-1][0]: 
            res.append((addr, t, it['lon'], it['lat']))
    return res 
        
