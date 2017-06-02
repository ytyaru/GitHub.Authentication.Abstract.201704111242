#!python3
#encoding:utf-8
from abc import ABCMeta, abstractmethod
import Authentication
class OAuthAuthentication(Authentication.Authentication):
    def __init__(self, token):
        self.__token = token
    
    @property
    def AccessToken(self):
        return self.__token

    """
    requestsライブラリのAPIで使うheadersを生成する。
    """
    def GetHeaders(self):
        headers = super().GetHeaders()
        headers.update({"Authorization": "token " + self.AccessToken})
        return headers

    """
    requestsライブラリのAPIで使う**kwargsを生成する。
    requests.get(url, **this.GetRequestParameters())
    """
    def GetRequestParameters(self):
        params = super().GetRequestParameters()
        params.update({'headers': self.GetHeaders()})
        return params

