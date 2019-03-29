# coding=utf-8
r"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from twilio.base.domain import Domain
from twilio.rest.studio.v1 import V1


class Studio(Domain):

    def __init__(self, twilio):
        """
        Initialize the Studio Domain

        :returns: Domain for Studio
        :rtype: twilio.rest.studio.Studio
        """
        super(Studio, self).__init__(twilio)

        self.base_url = 'https://studio.twilio.com'

        # Versions
        self._v1 = None

    @property
    def v1(self):
        """
        :returns: Version v1 of studio
        :rtype: twilio.rest.studio.v1.V1
        """
        if self._v1 is None:
            self._v1 = V1(self)
        return self._v1

    @property
    def flows(self):
        """
        :rtype: twilio.rest.studio.v1.flow.FlowList
        """
        return self.v1.flows

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Studio>'
