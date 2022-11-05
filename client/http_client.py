# -*- coding: utf-8 -*-
from common_sdk.logging.logger import logger
from urllib.parse import urlencode

import requests

"""
    通用的http处理类
"""


class HttpClient(object):

    def __init__(self, builder):
        self._builder = builder.url

    '''
        post请求关注返回值
    '''

    def make_post_request(self):
        url = 'http://{}/'.format(self._builder.url)
        try:
            if self._builder.proxy:
                logger.info("发送POST请求---->url{}   proxy---->{}".format(url, self._builder.proxy))
                res_json = requests.post(url, json=self._builder.param, headers=self._builder.headers, proxies=self._builder.proxy)
            else:
                logger.info("发送POST请求---->url{}".format(url))
                res_json = requests.post(url, json=self._builder.param, headers=self._builder.headers)
            if res_json:
                return res_json
            else:
                return {}
        except Exception as e:
            logger.info("请求失败{}".format(e))
            return False
    '''
        get请求关注返回的content（做解析）
    '''

    def make_get_request(self):
        url = 'http://{}'.format(self._builder.url)
        if self._builder.param:
            url += "?" + urlencode(self._builder.param())
        try:
            if self._builder.proxy:
                logger.info("发送GET请求---->url{}   proxy---->{}".format(url, self._builder.proxy))
                res = requests.get(url, headers=self._builder.headers, proxies=self._builder.proxy)
            else:
                logger.info("发送GET请求---->url{}".format(url))
                res = requests.get(url, headers=self._builder.headers)
            if res:
                return res.content
            else:
                return ""
        except Exception as e:
            logger.info("请求失败{}".format(e))
            return False
