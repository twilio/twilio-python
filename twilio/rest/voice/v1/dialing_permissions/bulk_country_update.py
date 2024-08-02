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


from datetime import date, datetime
from decimal import Decimal
from typing import Any, Dict, List, Optional, Union, Iterator, AsyncIterator
from twilio.base import deserialize, serialize, values

from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version



class BulkCountryUpdateInstance(InstanceResource):

    """
    :ivar update_count: The number of countries updated
    :ivar update_request: A bulk update request to change voice dialing country permissions stored as a URL-encoded, JSON array of update objects. For example : `[ { \"iso_code\": \"GB\", \"low_risk_numbers_enabled\": \"true\", \"high_risk_special_numbers_enabled\":\"true\", \"high_risk_tollfraud_numbers_enabled\": \"false\" } ]`
    """

    def __init__(self, version: Version, payload: Dict[str, Any]):
        super().__init__(version)

        
        self.update_count: Optional[int] = deserialize.integer(payload.get("update_count"))
        self.update_request: Optional[str] = payload.get("update_request")

        
        
    
    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        
        return '<Twilio.Voice.V1.BulkCountryUpdateInstance>'




class BulkCountryUpdateList(ListResource):
    
    def __init__(self, version: Version):
        """
        Initialize the BulkCountryUpdateList

        :param version: Version that contains the resource
        
        """
        super().__init__(version)

        
        self._uri = '/DialingPermissions/BulkCountryUpdates'
        
        
    
    def create(self, update_request: str) -> BulkCountryUpdateInstance:
        """
        Create the BulkCountryUpdateInstance

        :param update_request: URL encoded JSON array of update objects. example : `[ { \\\"iso_code\\\": \\\"GB\\\", \\\"low_risk_numbers_enabled\\\": \\\"true\\\", \\\"high_risk_special_numbers_enabled\\\":\\\"true\\\", \\\"high_risk_tollfraud_numbers_enabled\\\": \\\"false\\\" } ]`
        
        :returns: The created BulkCountryUpdateInstance
        """
        
        data = values.of({ 
            'UpdateRequest': update_request,
        })
        headers = values.of({
                'Content-Type': 'application/x-www-form-urlencoded'
            })
        
        
        payload = self._version.create(method='POST', uri=self._uri, data=data, headers=headers)

        return BulkCountryUpdateInstance(self._version, payload)

    async def create_async(self, update_request: str) -> BulkCountryUpdateInstance:
        """
        Asynchronously create the BulkCountryUpdateInstance

        :param update_request: URL encoded JSON array of update objects. example : `[ { \\\"iso_code\\\": \\\"GB\\\", \\\"low_risk_numbers_enabled\\\": \\\"true\\\", \\\"high_risk_special_numbers_enabled\\\":\\\"true\\\", \\\"high_risk_tollfraud_numbers_enabled\\\": \\\"false\\\" } ]`
        
        :returns: The created BulkCountryUpdateInstance
        """
        
        data = values.of({ 
            'UpdateRequest': update_request,
        })
        headers = values.of({
                'Content-Type': 'application/x-www-form-urlencoded'
            })
        
        
        payload = await self._version.create_async(method='POST', uri=self._uri, data=data, headers=headers)

        return BulkCountryUpdateInstance(self._version, payload)
    



    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return '<Twilio.Voice.V1.BulkCountryUpdateList>'

