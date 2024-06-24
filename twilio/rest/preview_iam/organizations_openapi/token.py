r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Organization Public API
    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

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
from twilio.http.http_client import TwilioHttpClient



class TokenInstance(InstanceResource):

    """
    :ivar access_token: Token which carries the necessary information to access a Twilio resource directly.
    :ivar refresh_token: Token which carries the information necessary to get a new access token.
    :ivar id_token: Token which carries the information necessary of user profile.
    :ivar token_type: Token type
    :ivar expires_in: 
    """

    def __init__(self, version: Version, payload: Dict[str, Any]):
        super().__init__(version)

        
        self.access_token: Optional[str] = payload.get("access_token")
        self.refresh_token: Optional[str] = payload.get("refresh_token")
        self.id_token: Optional[str] = payload.get("id_token")
        self.token_type: Optional[str] = payload.get("token_type")
        self.expires_in: Optional[int] = payload.get("expires_in")

        
        
    
    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        
        return '<Twilio.PreviewIam.Organizations_openapi.TokenInstance>'




class TokenList(ListResource):
    
    def __init__(self, version: Version):
        """
        Initialize the TokenList

        :param version: Version that contains the resource
        
        """
        super().__init__(version)

        
        self._uri = '/token'
        
        
    
    def create(self, grant_type: str, client_id: str, client_secret: Union[str, object]=values.unset, code: Union[str, object]=values.unset, redirect_uri: Union[str, object]=values.unset, audience: Union[str, object]=values.unset, refresh_token: Union[str, object]=values.unset, scope: Union[str, object]=values.unset) -> TokenInstance:
        """
        Create the TokenInstance

        :param grant_type: Grant type is a credential representing resource owner's authorization which can be used by client to obtain access token.
        :param client_id: A 34 character string that uniquely identifies this OAuth App.
        :param client_secret: The credential for confidential OAuth App.
        :param code: JWT token related to the authorization code grant type.
        :param redirect_uri: The redirect uri
        :param audience: The targeted audience uri
        :param refresh_token: JWT token related to refresh access token.
        :param scope: The scope of token
        
        :returns: The created TokenInstance
        """
        
        data = values.of({ 
            'grant_type': grant_type,
            'client_id': client_id,
            'client_secret': client_secret,
            'code': code,
            'redirect_uri': redirect_uri,
            'audience': audience,
            'refresh_token': refresh_token,
            'scope': scope,
        })
        
        twilioHttpClient = TwilioHttpClient()
        retries = 0
        while retries < 5:
            try:
                response = twilioHttpClient.request(
                    'POST',
                    'https://preview-iam.twilio.com',
                    data=data,
                    headers= {'content-type': 'json'},
                )
                if response.status_code >= 400 or response.status_code < 500:
                    retries += 1
                    continue
                return response.status_code['data']
            except Exception as e:
                if retries == 5:
                    raise e
                continue
