r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Api
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""


from datetime import date
from twilio.base import deserialize
from twilio.base import serialize
from twilio.base import values

from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version



class TokenList(ListResource):

    def __init__(self, version: Version, account_sid: str):
        """
        Initialize the TokenList

        :param Version version: Version that contains the resource
        :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that will create the resource.
        
        :returns: twilio.rest.api.v2010.account.token.TokenList
        :rtype: twilio.rest.api.v2010.account.token.TokenList
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 'account_sid': account_sid,  }
        self._uri = '/Accounts/{account_sid}/Tokens.json'.format(**self._solution)
        
        
    
    def create(self, ttl=values.unset):
        """
        Create the TokenInstance

        :param int ttl: The duration in seconds for which the generated credentials are valid. The default value is 86400 (24 hours).
        
        :returns: The created TokenInstance
        :rtype: twilio.rest.api.v2010.account.token.TokenInstance
        """
        data = values.of({ 
            'Ttl': ttl,
        })
        
        payload = self._version.create(method='POST', uri=self._uri, data=data,)

        return TokenInstance(self._version, payload, account_sid=self._solution['account_sid'])

    async def create_async(self, ttl=values.unset):
        """
        Asynchronous coroutine to create the TokenInstance

        :param int ttl: The duration in seconds for which the generated credentials are valid. The default value is 86400 (24 hours).
        
        :returns: The created TokenInstance
        :rtype: twilio.rest.api.v2010.account.token.TokenInstance
        """
        data = values.of({ 
            'Ttl': ttl,
        })
        
        payload = await self._version.create_async(method='POST', uri=self._uri, data=data,)

        return TokenInstance(self._version, payload, account_sid=self._solution['account_sid'])
    


    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.TokenList>'

class TokenInstance(InstanceResource):

    def __init__(self, version, payload, account_sid: str):
        """
        Initialize the TokenInstance
        :returns: twilio.rest.api.v2010.account.token.TokenInstance
        :rtype: twilio.rest.api.v2010.account.token.TokenInstance
        """
        super().__init__(version)

        self._properties = { 
            'account_sid': payload.get('account_sid'),
            'date_created': deserialize.rfc2822_datetime(payload.get('date_created')),
            'date_updated': deserialize.rfc2822_datetime(payload.get('date_updated')),
            'ice_servers': payload.get('ice_servers'),
            'password': payload.get('password'),
            'ttl': payload.get('ttl'),
            'username': payload.get('username'),
        }

        self._context = None
        self._solution = { 'account_sid': account_sid,  }
    
    
    @property
    def account_sid(self):
        """
        :returns: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Token resource.
        :rtype: str
        """
        return self._properties['account_sid']
    
    @property
    def date_created(self):
        """
        :returns: The date and time in GMT that the resource was created specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format.
        :rtype: datetime
        """
        return self._properties['date_created']
    
    @property
    def date_updated(self):
        """
        :returns: The date and time in GMT that the resource was last updated specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format.
        :rtype: datetime
        """
        return self._properties['date_updated']
    
    @property
    def ice_servers(self):
        """
        :returns: An array representing the ephemeral credentials and the STUN and TURN server URIs.
        :rtype: list[ApiV2010AccountTokenIceServers]
        """
        return self._properties['ice_servers']
    
    @property
    def password(self):
        """
        :returns: The temporary password that the username will use when authenticating with Twilio.
        :rtype: str
        """
        return self._properties['password']
    
    @property
    def ttl(self):
        """
        :returns: The duration in seconds for which the username and password are valid.
        :rtype: str
        """
        return self._properties['ttl']
    
    @property
    def username(self):
        """
        :returns: The temporary username that uniquely identifies a Token.
        :rtype: str
        """
        return self._properties['username']
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Api.V2010.TokenInstance {}>'.format(context)



