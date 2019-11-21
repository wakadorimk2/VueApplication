'''
getFaves.py
Twitterからいいね画像を集め、リストとして返す。
'''
import twitter
from conf_secret import keys_and_tokens
from conf import faves

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
        self.count_per_request = 20
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