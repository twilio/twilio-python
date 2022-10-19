# coding=utf-8
r"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.page import Page


class OauthList(ListResource):

    def __init__(self, version):
        """
        Initialize the OauthList

        :param Version version: Version that contains the resource

        :returns: twilio.rest.oauth.v1.oauth.OauthList
        :rtype: twilio.rest.oauth.v1.oauth.OauthList
        """
        super(OauthList, self).__init__(version)

        # Path Solution
        self._solution = {}

    def get(self):
        """
        Constructs a OauthContext

        :returns: twilio.rest.oauth.v1.oauth.OauthContext
        :rtype: twilio.rest.oauth.v1.oauth.OauthContext
        """
        return OauthContext(self._version, )

    def __call__(self):
        """
        Constructs a OauthContext

        :returns: twilio.rest.oauth.v1.oauth.OauthContext
        :rtype: twilio.rest.oauth.v1.oauth.OauthContext
        """
        return OauthContext(self._version, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Oauth.V1.OauthList>'


class OauthPage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the OauthPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.oauth.v1.oauth.OauthPage
        :rtype: twilio.rest.oauth.v1.oauth.OauthPage
        """
        super(OauthPage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of OauthInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.oauth.v1.oauth.OauthInstance
        :rtype: twilio.rest.oauth.v1.oauth.OauthInstance
        """
        return OauthInstance(self._version, payload, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Oauth.V1.OauthPage>'


class OauthContext(InstanceContext):

    def __init__(self, version):
        """
        Initialize the OauthContext

        :param Version version: Version that contains the resource

        :returns: twilio.rest.oauth.v1.oauth.OauthContext
        :rtype: twilio.rest.oauth.v1.oauth.OauthContext
        """
        super(OauthContext, self).__init__(version)

        # Path Solution
        self._solution = {}
        self._uri = '/certs'.format(**self._solution)

    def fetch(self):
        """
        Fetch the OauthInstance

        :returns: The fetched OauthInstance
        :rtype: twilio.rest.oauth.v1.oauth.OauthInstance
        """
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return OauthInstance(self._version, payload, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Oauth.V1.OauthContext {}>'.format(context)


class OauthInstance(InstanceResource):

    def __init__(self, version, payload):
        """
        Initialize the OauthInstance

        :returns: twilio.rest.oauth.v1.oauth.OauthInstance
        :rtype: twilio.rest.oauth.v1.oauth.OauthInstance
        """
        super(OauthInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {'keys': payload.get('keys'), 'url': payload.get('url'), }

        # Context
        self._context = None
        self._solution = {}

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context

        :returns: OauthContext for this OauthInstance
        :rtype: twilio.rest.oauth.v1.oauth.OauthContext
        """
        if self._context is None:
            self._context = OauthContext(self._version, )
        return self._context

    @property
    def keys(self):
        """
        :returns: A collection of certificates
        :rtype: dict
        """
        return self._properties['keys']

    @property
    def url(self):
        """
        :returns: The url
        :rtype: unicode
        """
        return self._properties['url']

    def fetch(self):
        """
        Fetch the OauthInstance

        :returns: The fetched OauthInstance
        :rtype: twilio.rest.oauth.v1.oauth.OauthInstance
        """
        return self._proxy.fetch()

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Oauth.V1.OauthInstance {}>'.format(context)