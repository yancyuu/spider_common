from sdk.client.actor_proxy_client import ActorProxyClient
from conf.spider_config import spider_config
from faker import Faker
from base_builder import BaseBuilder
"""
    用于处理请求时的内容封装(根据配置和特殊页面封装)
"""


class SpiderBuilder(BaseBuilder):
    def __init__(self):
        super().__init__()
        self.param = None
        self.proxy = None
        self.header = None
        self.actor_proxy = ActorProxyClient(SpiderBuilder.__name__)

    # 查询页面
    def get_search(self, param):
        self.param = param
        self.header = {
            "content-type": "text/html; charset=utf-8"
        }
        if spider_config.USE_COOKIE_POOL:
            actor_proxy = self.actor_proxy.create_cookie_actor_proxy()
            cookie = await actor_proxy.getCookie()
            # 在builder中增加cookie
            if cookie:
                self.header.update({"cookie": cookie.get("cookie")})
        if spider_config.RANDOM_AGENT:
            # 在builder中增加随机agent
            faker_handel = Faker()
            self.header.update({"agent": faker_handel.user_agent()})
        if spider_config.USE_PROXY:
            actor_proxy = self.actor_proxy.create_proxy_actor_proxy()
            proxy = await actor_proxy.getProxy()
            self.proxy = proxy
