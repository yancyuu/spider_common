# -*- coding: utf-8 -*-
from actor_proxy_client import ActorProxyClient
from http_client import HttpClient


class SpiderClient(HttpClient):

    def __init__(self, builder):
        super().__init__(builder)
        self.actor_proxy = ActorProxyClient(SpiderClient.__name__)

    def get_search(self):
        return self.make_get_request()


