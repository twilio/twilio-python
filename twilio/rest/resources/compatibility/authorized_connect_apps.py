from six import iteritems
from twilio.rest.resources.base import InstanceResource, ListResource


class AuthorizedConnectApp(InstanceResource):

    def load(self, entries):
        """ Translate certain parameters into others"""
        result = {}

        for k, v in iteritems(entries):
            k = k.replace("connect_app_", "")
            result[k] = v

        super(AuthorizedConnectApp, self).load(result)


class AuthorizedConnectApps(ListResource):
    pass
