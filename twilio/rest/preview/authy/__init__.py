# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from twilio.base.version import Version
from twilio.rest.preview.authy.service import ServiceList


class Authy(Version):

    def __init__(self, domain):
        """
        Initialize the Authy version of Preview

        :returns: Authy version of Preview
        :rtype: twilio.rest.preview.authy.Authy.Authy
        """
        super(Authy, self).__init__(domain)
        self.version = 'Authy'
        self._services = None

    @property
    def services(self):
        """
        :rtype: twilio.rest.preview.authy.service.ServiceList
        """
        if self._services is None:
            self._services = ServiceList(self)
        return self._services

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Preview.Authy>'