# -*- coding: utf-8 -*-
import json
import time
from common_sdk.logging.logger import logger
from common_sdk.data_transform import protobuf_transformer
from manager.proxy_manager import ProxyManager
import proto.proxy_pb2 as proxy_pb

'''
    用于生成代理的handel
'''


class ProxyHandel:

    def __init__(self, actor_id):
        self.actor_id = actor_id
        self.proxy_id = actor_id.id
        self.__load_time = None
        self.__manager = ProxyManager()

    async def get_proxy(self):
        message_list = await self.__manager.list_proxies(proxy_pb.ProxyMessage.INIT)
        # 随机返回一个

    '''
        创建一条普通proxy
    '''

    async def generate_proxy(self, proxy_url):
        message = proxy_pb.ProxyMessage()
        self.__manager.create_proxy(message)
        message.url = proxy_url
        await self.__manager.add_or_update_proxy(message)
        return message
