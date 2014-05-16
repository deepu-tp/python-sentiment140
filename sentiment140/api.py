import requests
import json
import urllib2


def chunkify(_list, chunk_size):
    for i in xrange(0, len(_list), chunk_size):
        yield _list[i: i + chunk_size]


class Sentiment140API(object):

    BASE_URL = "http://www.sentiment140.com/api"

    def __init__(self, appid=None, per_bulk_request=5000):
        self.appid = appid
        self.per_bulk_request = per_bulk_request


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


    def bulk_classify_json(self, data):

        results = []

        for chunk in chunkify(data, self.per_bulk_request):
            url = self._build_url('bulkClassifyJson')

            results.extend(self._fetch_url(url, data=json.dumps(
                           {'data' : data}), method='POST').json()['data'])

        return results