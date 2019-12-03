'''
getFaves.py
Twitterからいいね画像を集め、リストとして返す。
'''
import os
import datetime as dt
import json
import twitter
from conf_secret import keys_and_tokens
from conf import faves, cached_faves_name
from util import makeJson2dict, makeDict2json
from util import isDatetimeFormat, makeDatetime2string, makeString2datetime

# apiの初期化
api = twitter.Api(**keys_and_tokens)

# ツイート取得用クエリ
args = []
kwargs = {
    'api' : api,
    'screen_name' : 'wakadori_Mk2',
    #'last_id' : 1161675517847715840,  # このツイートIDより古い物を探す
}

# load JSON for monitoring Rate Limit
jsonpath = 'rate_status.json'
rate_status = makeJson2dict(jsonpath)

class FavoritesGenerator(object):
    ''' あるユーザがいいねした画像を取得する。
    callする度に[self.count_per_request]枚のStatusリストが返される '''
    def __init__(self, *args, **kwargs):
        self.args = args  # set parameters
        self.kwargs = kwargs
        self.count_per_request = 200  # max value
        if 'last_id' not in kwargs:
            self.last_id = -1
        else:
            self.last_id = kwargs['last_id']
        self.view_pointer = 0

        if os.path.exists(cached_faves_name):  # read a cache if it exists
            with open(cached_faves_name, 'r') as f:
                self.cached_faves = json.load(f)
        else:
            self.cached_faves = {}

    def __call__(self):
        kwargs = {  # パラメータ設定
            'screen_name' : self.kwargs['screen_name'],
            'count' : self.count_per_request,
        }

        # 取得開始ID指定(マイナスであれば指定なし)
        if self.last_id >= 0:
            kwargs['max_id'] = self.last_id

        # check rate limit AND count API
        if rate_status['current'] >= rate_status['limit']:
            fav_list = self.cached_faves
            print('used cache!!!')  # debug
        else:  # If use API, refresh rate status
            #fav_list = self.kwargs['api'].GetFavorites(**kwargs)
            #fav_list = [fav.AsDict() for fav in fav_list]  # convert to a list of dict
            fav_list = self.cached_faves
            print('called GetFavorites!!!')  # debug

            # set API used time
            now = dt.datetime.now()
            if not isDatetimeFormat(rate_status['start']):  # init
                rate_status['start'] = makeDatetime2string(now)
            else:
                start = makeString2datetime(rate_status['start'])
                elapsed_time = now - start
                if elapsed_time.seconds > rate_status['interval']:  # refresh
                    rate_status['start'] = makeDatetime2string(now)
                    rate_status['current'] = 0
                rate_status['current'] += 1  # increment API count

            # save rate status
            makeDict2json(rate_status, jsonpath)

        print(rate_status)  # debug

        # make or refresh cache
        existNew = True  # temporarily force making cache
        if existNew:
            self.cached_faves = fav_list
            with open(cached_faves_name, 'w') as f:
                json.dump(self.cached_faves, f)

        # prepare for next call
        self.last_id = fav_list[-1]['id']

        # return top 20 tweets
        top_num = 20
        residual_len = len(fav_list) - self.view_pointer
        if residual_len < top_num :
            top = fav_list[self.view_pointer:]
        else:
            top = fav_list[self.view_pointer:self.view_pointer + top_num]
        self.view_pointer += top_num
        return top

gen = FavoritesGenerator(*args, **kwargs)

def getFaves():
    ret = gen()
    for e, j in zip(ret, range(len(ret))):
        if 'media' not in e.keys():
            continue
        media = e['media'][0]
        url = media['media_url_https'].replace('.jpg', '.png')
        id = e['id']
        faves.append({
            'id' : id,
            'src' : url,
            'text' : e['text'],
            'sizes' : media['sizes'],
            'favorite_count' : e['favorite_count'],
            'retweet_count' : e['retweet_count'],
            'created_at' : e['created_at']
        })
    return faves

if __name__ == '__main__':
    faves = getFaves()