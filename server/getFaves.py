
'''
correctimage.py
Twitterからいいね画像を集める
'''
import twitter
from conf_secret import keys_and_tokens
from conf import faves
import datetime as dt
import time
from pprint import pprint
from PIL import Image
import requests
from io import BytesIO
from pdb import set_trace as trace

# apiの初期化
api = twitter.Api(**keys_and_tokens)

# ツイート取得用クエリ
args = []
kwargs = {
    'api' : api,
    'screen_name' : 'wakadori_Mk2',
    #'last_id' : 1161675517847715840,  # このツイートIDより古い物を探す
}

class FavoritesGenerator(object):
    ''' あるユーザがいいねした画像を取得する。
    callする度に[self.count_per_request]枚のStatusリストが返される '''
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs
        self.now_count = 0
        self.count_per_request = 200
        if 'last_id' not in kwargs:
            self.last_id = -1
        else:
            self.last_id = kwargs['last_id']

    def __call__(self):
        kwargs = {
            'screen_name' : self.kwargs['screen_name'],
            'count' : self.count_per_request,
        }
        if self.last_id >= 0:
            kwargs['max_id'] = self.last_id                
        fav_list = self.kwargs['api'].GetFavorites(**kwargs)
        self.last_id = fav_list[-1].AsDict()['id']
        return fav_list

gen = FavoritesGenerator(*args, **kwargs)

def getFaves():
    for i in range(1):
        ret = gen()
        for e, j in zip(ret, range(len(ret))):
            e = e.AsDict()
            if 'media' not in e.keys():
                continue
            url = e['media'][0]['media_url_https'].replace('.jpg', '.png')
            id = e['id']
            faves.append({
                'id' : id,
                'url' : url
            })
    return faves

if __name__ == '__main__':
    getFaves()