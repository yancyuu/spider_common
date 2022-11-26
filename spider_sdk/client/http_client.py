# -*- coding: utf-8 -*-
from common_sdk.logging.logger import logger
from urllib.parse import urlencode

import httpx

"""
    通用的http处理类
"""


class HttpClient(object):

    def __init__(self, builder):
        self._client = None
        self._builder = builder.url

    '''
        post请求关注返回值
    '''

    def make_post_request(self):
        url = 'http://{}/'.format(self._builder.url)
        try:
            if self._builder.proxy:
                self._client = httpx.AsyncClient(proxies=self._builder.proxy)
                logger.info("发送POST请求---->url={}   proxy---->{}".format(url, self._builder.proxy))
            else:
                self._client = httpx.AsyncClient()
                logger.info("发送POST请求---->url={}".format(url))
            res_json = self._client.post(url, json=self._builder.param, headers=self._builder.headers)
            logger.info("接受返回值---->res_json={}".format(res_json))
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
                self._client = httpx.AsyncClient(proxies=self._builder.proxy)
                logger.info("发送GET请求---->url{}   proxy---->{}".format(url, self._builder.proxy))
            else:
                self._client = httpx.AsyncClient()
                logger.info("发送GET请求---->url{}".format(url))
            res = self._client.get(url, headers=self._builder.headers)
            logger.info("接受返回值---->{}".format(res))
            if res:
                return res
            else:
                return ""
        except Exception as e:
            logger.info("请求失败{}".format(e))
            return False
