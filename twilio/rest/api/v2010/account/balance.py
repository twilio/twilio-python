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


from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version


class BalanceList(ListResource):
    def __init__(self, version: Version, account_sid: str):
        """
        Initialize the BalanceList

        :param Version version: Version that contains the resource
        :param account_sid: The unique SID identifier of the Account.

        :returns: twilio.rest.api.v2010.account.balance.BalanceList
        :rtype: twilio.rest.api.v2010.account.balance.BalanceList
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "account_sid": account_sid,
        }
        self._uri = "/Accounts/{account_sid}/Balance.json".format(**self._solution)

    def fetch(self):
        """
        Asynchronously fetch the BalanceInstance

        :returns: The fetched BalanceInstance
        :rtype: twilio.rest.api.v2010.account.balance.BalanceInstance
        """
        payload = self._version.fetch(method="GET", uri=self._uri)

        return BalanceInstance(
            self._version, payload, account_sid=self._solution["account_sid"]
        )

    async def fetch_async(self):
        """
        Asynchronously fetch the BalanceInstance

        :returns: The fetched BalanceInstance
        :rtype: twilio.rest.api.v2010.account.balance.BalanceInstance
        """
        payload = await self._version.fetch_async(method="GET", uri=self._uri)

        return BalanceInstance(
            self._version, payload, account_sid=self._solution["account_sid"]
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return "<Twilio.Api.V2010.BalanceList>"


class BalanceInstance(InstanceResource):
    def __init__(self, version, payload, account_sid: str):
        """
        Initialize the BalanceInstance

        :returns: twilio.rest.api.v2010.account.balance.BalanceInstance
        :rtype: twilio.rest.api.v2010.account.balance.BalanceInstance
        """
        super().__init__(version)

        self._properties = {
            "account_sid": payload.get("account_sid"),
            "balance": payload.get("balance"),
            "currency": payload.get("currency"),
        }

        self._context = None
        self._solution = {
            "account_sid": account_sid,
        }

    @property
    def account_sid(self):
        """
        :returns: The unique SID identifier of the Account.
        :rtype: str
        """
        return self._properties["account_sid"]

    @property
    def balance(self):
        """
        :returns: The balance of the Account, in units specified by the unit parameter. Balance changes may not be reflected immediately. Child accounts do not contain balance information
        :rtype: str
        """
        return self._properties["balance"]

    @property
    def currency(self):
        """
        :returns: The units of currency for the account balance
        :rtype: str
        """
        return self._properties["currency"]

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Api.V2010.BalanceInstance {}>".format(context)
