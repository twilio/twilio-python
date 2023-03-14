"""
  This code was generated by
  ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
   |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
   |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

  NOTE: This class is auto generated by OpenAPI Generator.
  https://openapi-generator.tech
  Do not edit the class manually.
"""
from twilio.base.domain import Domain
from twilio.rest.api.v2010 import V2010


class ApiBase(Domain):
    def __init__(self, twilio):
        """
        Initialize the Api Domain

        :returns: Domain for Api
        :rtype: twilio.rest.api.Api
        """
        super().__init__(twilio)
        self.base_url = "https://api.twilio.com"
        self._v2010 = None

    @property
    def v2010(self):
        """
        :returns: Versions v2010 of Api
        :rtype: twilio.rest.api.v2010.V2010
        """
        if self._v2010 is None:
            self._v2010 = V2010(self)
        return self._v2010

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return "<Twilio.Api>"
