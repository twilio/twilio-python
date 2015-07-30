from six import iteritems

from twilio.rest.v2010.account.connect_app import (
    ConnectApp,
    ConnectApps as BaseConnectApps,
)

from twilio.rest.v2010.account.authorized_connect_app import (
    AuthorizedConnectApp as BaseAuthorizedConnectApp,
    AuthorizedConnectApps as BaseAuthorizedConnectApps
)


class ConnectApps(BaseConnectApps):

    def update(self, sid, **kwargs):
        raise AttributeError('Update is not allowed on connect apps')


class AuthorizedConnectApp(BaseAuthorizedConnectApp):

    def load(self, entries):
        """ Translate certain parameters into others"""
        result = {}

        for k, v in iteritems(entries):
            k = k.replace("connect_app_", "")
            result[k] = v

        super(AuthorizedConnectApp, self).load(result)


class AuthorizedConnectApps(BaseAuthorizedConnectApps):
    instance = AuthorizedConnectApp
