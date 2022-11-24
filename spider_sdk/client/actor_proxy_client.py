import os

from dapr.actor import ActorProxy, ActorId
from handel.cookie.cookie_actor_interface import CookieActorInterface
from handel.proxy.proxy_actor_interface import ProxyActorInterface

"""
    通用的边车服务代理类
"""


class ActorProxyClient:

    def __init__(self, actor_id):
        self._actor_id = actor_id

    @property
    def actor_id(self):
        return self._actor_id

    def create_cookie_actor_proxy(self):
        return ActorProxy.create('CookieActor', ActorId(self.actor_id), CookieActorInterface)

    def create_proxy_actor_proxy(self):
        return ActorProxy.create('ProxyActor', ActorId(self.actor_id), ProxyActorInterface)

