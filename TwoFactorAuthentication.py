#!python3
#encoding:utf-8
from abc import ABCMeta, abstractmethod
import Authentication
import BasicAuthentication
import pyotp
class TwoFactorAuthentication(BasicAuthentication.BasicAuthentication):
    def __init__(self, username, password, secret):
        super().__init__(username, password)
        self.__secret = secret
        self.__totp = pyotp.TOTP(self.__secret)
    
    @property
    def OneTimePassword(self):
        return self.__totp.now()

    """
    requestsライブラリのAPIで使うheadersを生成する。
    """
    def GetHeaders(self):
        headers = super().GetHeaders()
        headers.update({'headers': {"X-GitHub-OTP": self.OneTimePassword}})
        return headers
 
    """
    requestsライブラリのAPIで使う**kwargsを生成する。
    requests.get(url, **this.GetRequestParameters())
    """
    def GetRequestParameters(self):
        params = super().GetRequestParameters()
        params.update({'headers': self.GetHeaders()})
        return params

