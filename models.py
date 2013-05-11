import json
import time
import tornado.database
from config import DATABASE 

FEED_TYPE = {
        'location': 0,
        }

class Model:
    def __init__(self):
        self.db = tornado.database.Connection(**DATABASE)

    def create_location(self, owner, lat, lon):
        c = json.dumps({'lat':lat, 'lon':lon})
        t = int(time.time())
        sql = "INSERT INTO feed(create_time, owner, typ, content) VALUES (%d, %d, %d, '%s')"
        print type(t), type(owner), type(FEED_TYPE['location'])
        self.db.execute(sql%(t, owner, FEED_TYPE['location'], c))
        #self.db.execute(sql, t, owner, FEED_TYPE['location'], c)

    def get_feed(self):
        sql = 'SELECT * FROM feed ORDER BY create_time DESC LIMIT 50'
        return self.db.query(sql)

