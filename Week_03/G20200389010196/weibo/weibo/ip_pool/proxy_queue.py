# -*- coding: utf-8 -*-
from proxy_util import logger
import json
import redis
from ipproxy import IPProxy
from proxy_util import proxy_to_dict, proxy_from_dict, _is_proxy_available
from proxy_settings import PROXIES_REDIS_EXISTED, PROXIES_REDIS_FORMATTER, MAX_CONTINUOUS_TIMES, PROXY_CHECK_BEFOREADD
 
"""
Proxy Queue Base Class
"""
class BaseQueue(object):
 
    def __init__(self, server):
        """Initialize the proxy queue instance
        Parameters
        ----------
        server : StrictRedis
            Redis client instance
        """
        self.server = server
 
    def _serialize_proxy(self, proxy):
        """Serialize proxy instance"""
        return proxy_to_dict(proxy)
 
    def _deserialize_proxy(self, serialized_proxy):
        """deserialize proxy instance"""
        return proxy_from_dict(eval(serialized_proxy))
 
    def __len__(self, schema='http'):
        """Return the length of the queue"""
        raise NotImplementedError
 
    def push(self, proxy, need_check):
        """Push a proxy"""
        raise NotImplementedError
 
    def pop(self, schema='http', timeout=0):
        """Pop a proxy"""
        raise NotImplementedError
 
 
class FifoQueue(BaseQueue):
    """First in first out queue"""
 
    def __len__(self, schema='http'):
        """Return the length of the queue"""
        return self.server.llen(PROXIES_REDIS_FORMATTER.format(schema))
 
    def push(self, proxy, need_check=PROXY_CHECK_BEFOREADD):
        """Push a proxy"""
        if need_check and not _is_proxy_available(proxy):
            return
        elif proxy.continuous_failed < MAX_CONTINUOUS_TIMES and not self._is_existed(proxy):
            key = PROXIES_REDIS_FORMATTER.format(proxy.schema)
            self.server.rpush(key, json.dumps(self._serialize_proxy(proxy),ensure_ascii=False))
 
    def pop(self, schema='http', timeout=0):
        """Pop a proxy"""
        if timeout > 0:
            p = self.server.blpop(PROXIES_REDIS_FORMATTER.format(schema.lower()), timeout)
            if isinstance(p, tuple):
                p = p[1]
        else:
            p = self.server.lpop(PROXIES_REDIS_FORMATTER.format(schema.lower()))
        if p:
            p = self._deserialize_proxy(p)
            self.server.srem(PROXIES_REDIS_EXISTED, p._get_url())
            return p
 
    def _is_existed(self, proxy):
        added = self.server.sadd(PROXIES_REDIS_EXISTED, proxy._get_url())
        return added == 0
 
 
if __name__ == '__main__':
    r = redis.StrictRedis(host='localhost', port=6379)
    queue = FifoQueue(r)
    proxy = IPProxy('http', '218.66.253.144', '80')
    queue.push(proxy)
    proxy = queue.pop(schema='http')
    print(proxy._get_url())