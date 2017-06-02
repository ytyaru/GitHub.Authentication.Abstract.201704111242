#!python3
#encoding:utf-8
import argparse
import Authentication
import BasicAuthentication
import OAuthAuthentication
import TwoFactorAuthentication
class Main:
    def __init__(self):
        pass

    def Run(self):
        parser = argparse.ArgumentParser(
            description='GitHub Authentication User Create Test.',
        )
        parser.add_argument('-u', '--username')
        parser.add_argument('-p', '--password')
        parser.add_argument('-t', '--token')
        parser.add_argument('-s', '--two-factor-secret')
        args = parser.parse_args()

        user = None
        if (None is not args.token):
            user = OAuthAuthentication.OAuthAuthentication(args.token)
        elif (None is not args.username) and (None is not args.password) and (None is not args.two_factor_secret):
            user = TwoFactorAuthentication.TwoFactorAuthentication(args.username, args.password, args.two_factor_secret)
        elif (None is not args.username) and (None is not args.password):
            user = BasicAuthentication.BasicAuthentication(args.username, args.password)
        else:
            raise Exception('認証データ生成エラー。以下の組合せのみ有効です。Basic: username, password, TwoFactor: username, password, two-factor-secret, OAuthNonWebApp: token')
        self.__RunApi(user)

    def __RunApi(self, user):
        print(user.GetRequestParameters())
        # requests.get(url, **user.GetRequestParameters())
        
if __name__ == '__main__':
    main = Main()
    main.Run()
