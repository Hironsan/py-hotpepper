# -*- coding: utf-8 -*-


import requests

__version__ = '0.0.1'


class HotPepperError(Exception):
    """ Exception """
    pass


class HotPepperInterface(object):

    DEFAULT_HOST = 'webservice.recruit.co.jp'

    url_prefix = 'http://{0}'.format(DEFAULT_HOST)
    
    api_key = None

    def __init__(self, api_key):
        self.api_key = api_key

    def _send(self, url, params):
        """
        Send request to API.
        
        :param url: API URL 
        :param params: Request params
        :return response: Response object 
        """
        response = requests.get(url, params=params)
        if response.status_code == 200:
            return response
        
        raise HotPepperError('Status is {0}, params is {1}.'.format(response.status_code, params))

    def send(self, **kwargs):
        url = '{0}{1}?key={2}'.format(self.url_prefix, self.PATH, self.api_key)
        kwargs['format'] = 'json'

        response = self._send(url, kwargs)
        response_json = response.json()

        return response_json

