import requests
import json
import urllib2

class Sentiment140API(object):

    BASE_URL = "http://www.sentiment140.com/api"

    def __init__(self, appid=None):
        self.appid = appid


    def _build_url(self, api_method):
        return '/'.join([self.BASE_URL, api_method])


    def _fetch_url(self, url, data=None, params=None, method='GET'):
        if params is None:
            params = {}

        # if self.appid:
        #     params['appid'] = self.appid
        url = url+'?appid='+self.appid

        return requests.request(method=method, url=url,
                               data=data, params=params)


    def classify(self, text):
        url = self._build_url('classify')
        return self._fetch_url(url, params={'text' : text}).json()['results']


    def bulk_classify_json(self, tweets):
        url = self._build_url('bulkClassifyJson')
        return self._fetch_url(url, data=json.dumps(
                                {'data' : tweets}),
                                method='POST').json()['data']