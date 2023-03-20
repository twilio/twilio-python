r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Voice
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""


from twilio.base import deserialize, values

from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version


class BulkCountryUpdateInstance(InstanceResource):
    def __init__(self, version, payload):
        """
        Initialize the BulkCountryUpdateInstance

        :returns: twilio.rest.voice.v1.dialing_permissions.bulk_country_update.BulkCountryUpdateInstance
        :rtype: twilio.rest.voice.v1.dialing_permissions.bulk_country_update.BulkCountryUpdateInstance
        """
        super().__init__(version)

        self._properties = {
            "update_count": deserialize.integer(payload.get("update_count")),
            "update_request": payload.get("update_request"),
        }

        self._solution = {}

    @property
    def update_count(self):
        """
        :returns: The number of countries updated
        :rtype: int
        """
        return self._properties["update_count"]

    @property
    def update_request(self):
        """
        :returns: A bulk update request to change voice dialing country permissions stored as a URL-encoded, JSON array of update objects. For example : `[ { \"iso_code\": \"GB\", \"low_risk_numbers_enabled\": \"true\", \"high_risk_special_numbers_enabled\":\"true\", \"high_risk_tollfraud_numbers_enabled\": \"false\" } ]`
        :rtype: str
        """
        return self._properties["update_request"]

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Voice.V1.BulkCountryUpdateInstance {}>".format(context)


class BulkCountryUpdateList(ListResource):
    def __init__(self, version: Version):
        """
        Initialize the BulkCountryUpdateList

        :param Version version: Version that contains the resource

        :returns: twilio.rest.voice.v1.dialing_permissions.bulk_country_update.BulkCountryUpdateList
        :rtype: twilio.rest.voice.v1.dialing_permissions.bulk_country_update.BulkCountryUpdateList
        """
        super().__init__(version)

        self._uri = "/DialingPermissions/BulkCountryUpdates"

    def create(self, update_request):
        """
        Create the BulkCountryUpdateInstance

        :param str update_request: URL encoded JSON array of update objects. example : `[ { \\\"iso_code\\\": \\\"GB\\\", \\\"low_risk_numbers_enabled\\\": \\\"true\\\", \\\"high_risk_special_numbers_enabled\\\":\\\"true\\\", \\\"high_risk_tollfraud_numbers_enabled\\\": \\\"false\\\" } ]`

        :returns: The created BulkCountryUpdateInstance
        :rtype: twilio.rest.voice.v1.dialing_permissions.bulk_country_update.BulkCountryUpdateInstance
        """
        data = values.of(
            {
                "UpdateRequest": update_request,
            }
        )

        payload = self._version.create(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return BulkCountryUpdateInstance(self._version, payload)

    async def create_async(self, update_request):
        """
        Asynchronously create the BulkCountryUpdateInstance

        :param str update_request: URL encoded JSON array of update objects. example : `[ { \\\"iso_code\\\": \\\"GB\\\", \\\"low_risk_numbers_enabled\\\": \\\"true\\\", \\\"high_risk_special_numbers_enabled\\\":\\\"true\\\", \\\"high_risk_tollfraud_numbers_enabled\\\": \\\"false\\\" } ]`

        :returns: The created BulkCountryUpdateInstance
        :rtype: twilio.rest.voice.v1.dialing_permissions.bulk_country_update.BulkCountryUpdateInstance
        """
        data = values.of(
            {
                "UpdateRequest": update_request,
            }
        )

        payload = await self._version.create_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return BulkCountryUpdateInstance(self._version, payload)

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return "<Twilio.Voice.V1.BulkCountryUpdateList>"
