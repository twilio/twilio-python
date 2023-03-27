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


from datetime import datetime
from typing import Any, Dict, Optional
from twilio.base import deserialize, serialize, values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version


class PaymentInstance(InstanceResource):

    """
    :ivar account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Payments resource.
    :ivar call_sid: The SID of the [Call](https://www.twilio.com/docs/voice/api/call-resource) the Payments resource is associated with. This will refer to the call sid that is producing the payment card (credit/ACH) information thru DTMF.
    :ivar sid: The SID of the Payments resource.
    :ivar date_created: The date and time in GMT that the resource was created specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format.
    :ivar date_updated: The date and time in GMT that the resource was last updated specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format.
    :ivar uri: The URI of the resource, relative to `https://api.twilio.com`.
    """

    def __init__(
        self,
        version: Version,
        payload: Dict[str, Any],
        account_sid: str,
        call_sid: str,
        sid: Optional[str] = None,
    ):
        super().__init__(version)

        self.account_sid: Optional[str] = payload.get("account_sid")
        self.call_sid: Optional[str] = payload.get("call_sid")
        self.sid: Optional[str] = payload.get("sid")
        self.date_created: Optional[datetime] = deserialize.rfc2822_datetime(
            payload.get("date_created")
        )
        self.date_updated: Optional[datetime] = deserialize.rfc2822_datetime(
            payload.get("date_updated")
        )
        self.uri: Optional[str] = payload.get("uri")

        self._solution = {
            "account_sid": account_sid,
            "call_sid": call_sid,
            "sid": sid or self.sid,
        }
        self._context: Optional[PaymentContext] = None

    @property
    def _proxy(self) -> "PaymentContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: PaymentContext for this PaymentInstance
        """
        if self._context is None:
            self._context = PaymentContext(
                self._version,
                account_sid=self._solution["account_sid"],
                call_sid=self._solution["call_sid"],
                sid=self._solution["sid"],
            )
        return self._context

    def update(
        self,
        idempotency_key,
        status_callback,
        capture=values.unset,
        status=values.unset,
    ) -> "PaymentInstance":
        """
        Update the PaymentInstance

        :param str idempotency_key: A unique token that will be used to ensure that multiple API calls with the same information do not result in multiple transactions. This should be a unique string value per API call and can be a randomly generated.
        :param str status_callback: Provide an absolute or relative URL to receive status updates regarding your Pay session. Read more about the [Update](https://www.twilio.com/docs/voice/api/payment-resource#statuscallback-update) and [Complete/Cancel](https://www.twilio.com/docs/voice/api/payment-resource#statuscallback-cancelcomplete) POST requests.
        :param "PaymentInstance.Capture" capture:
        :param "PaymentInstance.Status" status:

        :returns: The updated PaymentInstance
        """
        return self._proxy.update(
            idempotency_key=idempotency_key,
            status_callback=status_callback,
            capture=capture,
            status=status,
        )

    async def update_async(
        self,
        idempotency_key,
        status_callback,
        capture=values.unset,
        status=values.unset,
    ) -> "PaymentInstance":
        """
        Asynchronous coroutine to update the PaymentInstance

        :param str idempotency_key: A unique token that will be used to ensure that multiple API calls with the same information do not result in multiple transactions. This should be a unique string value per API call and can be a randomly generated.
        :param str status_callback: Provide an absolute or relative URL to receive status updates regarding your Pay session. Read more about the [Update](https://www.twilio.com/docs/voice/api/payment-resource#statuscallback-update) and [Complete/Cancel](https://www.twilio.com/docs/voice/api/payment-resource#statuscallback-cancelcomplete) POST requests.
        :param "PaymentInstance.Capture" capture:
        :param "PaymentInstance.Status" status:

        :returns: The updated PaymentInstance
        """
        return await self._proxy.update_async(
            idempotency_key=idempotency_key,
            status_callback=status_callback,
            capture=capture,
            status=status,
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Api.V2010.PaymentInstance {}>".format(context)


class PaymentContext(InstanceContext):
    def __init__(self, version: Version, account_sid: str, call_sid: str, sid: str):
        """
        Initialize the PaymentContext

        :param version: Version that contains the resource
        :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that will update the resource.
        :param call_sid: The SID of the call that will update the resource. This should be the same call sid that was used to create payments resource.
        :param sid: The SID of Payments session that needs to be updated.
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "account_sid": account_sid,
            "call_sid": call_sid,
            "sid": sid,
        }
        self._uri = (
            "/Accounts/{account_sid}/Calls/{call_sid}/Payments/{sid}.json".format(
                **self._solution
            )
        )

    def update(
        self,
        idempotency_key,
        status_callback,
        capture=values.unset,
        status=values.unset,
    ) -> PaymentInstance:
        """
        Update the PaymentInstance

        :param str idempotency_key: A unique token that will be used to ensure that multiple API calls with the same information do not result in multiple transactions. This should be a unique string value per API call and can be a randomly generated.
        :param str status_callback: Provide an absolute or relative URL to receive status updates regarding your Pay session. Read more about the [Update](https://www.twilio.com/docs/voice/api/payment-resource#statuscallback-update) and [Complete/Cancel](https://www.twilio.com/docs/voice/api/payment-resource#statuscallback-cancelcomplete) POST requests.
        :param "PaymentInstance.Capture" capture:
        :param "PaymentInstance.Status" status:

        :returns: The updated PaymentInstance
        """
        data = values.of(
            {
                "IdempotencyKey": idempotency_key,
                "StatusCallback": status_callback,
                "Capture": capture,
                "Status": status,
            }
        )

        payload = self._version.update(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return PaymentInstance(
            self._version,
            payload,
            account_sid=self._solution["account_sid"],
            call_sid=self._solution["call_sid"],
            sid=self._solution["sid"],
        )

    async def update_async(
        self,
        idempotency_key,
        status_callback,
        capture=values.unset,
        status=values.unset,
    ) -> PaymentInstance:
        """
        Asynchronous coroutine to update the PaymentInstance

        :param str idempotency_key: A unique token that will be used to ensure that multiple API calls with the same information do not result in multiple transactions. This should be a unique string value per API call and can be a randomly generated.
        :param str status_callback: Provide an absolute or relative URL to receive status updates regarding your Pay session. Read more about the [Update](https://www.twilio.com/docs/voice/api/payment-resource#statuscallback-update) and [Complete/Cancel](https://www.twilio.com/docs/voice/api/payment-resource#statuscallback-cancelcomplete) POST requests.
        :param "PaymentInstance.Capture" capture:
        :param "PaymentInstance.Status" status:

        :returns: The updated PaymentInstance
        """
        data = values.of(
            {
                "IdempotencyKey": idempotency_key,
                "StatusCallback": status_callback,
                "Capture": capture,
                "Status": status,
            }
        )

        payload = await self._version.update_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return PaymentInstance(
            self._version,
            payload,
            account_sid=self._solution["account_sid"],
            call_sid=self._solution["call_sid"],
            sid=self._solution["sid"],
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Api.V2010.PaymentContext {}>".format(context)


class PaymentList(ListResource):
    def __init__(self, version: Version, account_sid: str, call_sid: str):
        """
        Initialize the PaymentList

        :param version: Version that contains the resource
        :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that will create the resource.
        :param call_sid: The SID of the call that will create the resource. Call leg associated with this sid is expected to provide payment information thru DTMF.

        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "account_sid": account_sid,
            "call_sid": call_sid,
        }
        self._uri = "/Accounts/{account_sid}/Calls/{call_sid}/Payments.json".format(
            **self._solution
        )

    def create(
        self,
        idempotency_key,
        status_callback,
        bank_account_type=values.unset,
        charge_amount=values.unset,
        currency=values.unset,
        description=values.unset,
        input=values.unset,
        min_postal_code_length=values.unset,
        parameter=values.unset,
        payment_connector=values.unset,
        payment_method=values.unset,
        postal_code=values.unset,
        security_code=values.unset,
        timeout=values.unset,
        token_type=values.unset,
        valid_card_types=values.unset,
    ) -> PaymentInstance:
        """
        Create the PaymentInstance

        :param str idempotency_key: A unique token that will be used to ensure that multiple API calls with the same information do not result in multiple transactions. This should be a unique string value per API call and can be a randomly generated.
        :param str status_callback: Provide an absolute or relative URL to receive status updates regarding your Pay session. Read more about the [expected StatusCallback values](https://www.twilio.com/docs/voice/api/payment-resource#statuscallback)
        :param &quot;PaymentInstance.BankAccountType&quot; bank_account_type:
        :param float charge_amount: A positive decimal value less than 1,000,000 to charge against the credit card or bank account. Default currency can be overwritten with `currency` field. Leave blank or set to 0 to tokenize.
        :param str currency: The currency of the `charge_amount`, formatted as [ISO 4127](http://www.iso.org/iso/home/standards/currency_codes.htm) format. The default value is `USD` and all values allowed from the Pay Connector are accepted.
        :param str description: The description can be used to provide more details regarding the transaction. This information is submitted along with the payment details to the Payment Connector which are then posted on the transactions.
        :param str input: A list of inputs that should be accepted. Currently only `dtmf` is supported. All digits captured during a pay session are redacted from the logs.
        :param int min_postal_code_length: A positive integer that is used to validate the length of the `PostalCode` inputted by the user. User must enter this many digits.
        :param object parameter: A single-level JSON object used to pass custom parameters to payment processors. (Required for ACH payments). The information that has to be included here depends on the <Pay> Connector. [Read more](https://www.twilio.com/console/voice/pay-connectors).
        :param str payment_connector: This is the unique name corresponding to the Pay Connector installed in the Twilio Add-ons. Learn more about [<Pay> Connectors](https://www.twilio.com/console/voice/pay-connectors). The default value is `Default`.
        :param &quot;PaymentInstance.PaymentMethod&quot; payment_method:
        :param bool postal_code: Indicates whether the credit card postal code (zip code) is a required piece of payment information that must be provided by the caller. The default is `true`.
        :param bool security_code: Indicates whether the credit card security code is a required piece of payment information that must be provided by the caller. The default is `true`.
        :param int timeout: The number of seconds that <Pay> should wait for the caller to press a digit between each subsequent digit, after the first one, before moving on to validate the digits captured. The default is `5`, maximum is `600`.
        :param &quot;PaymentInstance.TokenType&quot; token_type:
        :param str valid_card_types: Credit card types separated by space that Pay should accept. The default value is `visa mastercard amex`

        :returns: The created PaymentInstance
        """
        data = values.of(
            {
                "IdempotencyKey": idempotency_key,
                "StatusCallback": status_callback,
                "BankAccountType": bank_account_type,
                "ChargeAmount": charge_amount,
                "Currency": currency,
                "Description": description,
                "Input": input,
                "MinPostalCodeLength": min_postal_code_length,
                "Parameter": serialize.object(parameter),
                "PaymentConnector": payment_connector,
                "PaymentMethod": payment_method,
                "PostalCode": postal_code,
                "SecurityCode": security_code,
                "Timeout": timeout,
                "TokenType": token_type,
                "ValidCardTypes": valid_card_types,
            }
        )

        payload = self._version.create(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return PaymentInstance(
            self._version,
            payload,
            account_sid=self._solution["account_sid"],
            call_sid=self._solution["call_sid"],
        )

    async def create_async(
        self,
        idempotency_key,
        status_callback,
        bank_account_type=values.unset,
        charge_amount=values.unset,
        currency=values.unset,
        description=values.unset,
        input=values.unset,
        min_postal_code_length=values.unset,
        parameter=values.unset,
        payment_connector=values.unset,
        payment_method=values.unset,
        postal_code=values.unset,
        security_code=values.unset,
        timeout=values.unset,
        token_type=values.unset,
        valid_card_types=values.unset,
    ) -> PaymentInstance:
        """
        Asynchronously create the PaymentInstance

        :param str idempotency_key: A unique token that will be used to ensure that multiple API calls with the same information do not result in multiple transactions. This should be a unique string value per API call and can be a randomly generated.
        :param str status_callback: Provide an absolute or relative URL to receive status updates regarding your Pay session. Read more about the [expected StatusCallback values](https://www.twilio.com/docs/voice/api/payment-resource#statuscallback)
        :param &quot;PaymentInstance.BankAccountType&quot; bank_account_type:
        :param float charge_amount: A positive decimal value less than 1,000,000 to charge against the credit card or bank account. Default currency can be overwritten with `currency` field. Leave blank or set to 0 to tokenize.
        :param str currency: The currency of the `charge_amount`, formatted as [ISO 4127](http://www.iso.org/iso/home/standards/currency_codes.htm) format. The default value is `USD` and all values allowed from the Pay Connector are accepted.
        :param str description: The description can be used to provide more details regarding the transaction. This information is submitted along with the payment details to the Payment Connector which are then posted on the transactions.
        :param str input: A list of inputs that should be accepted. Currently only `dtmf` is supported. All digits captured during a pay session are redacted from the logs.
        :param int min_postal_code_length: A positive integer that is used to validate the length of the `PostalCode` inputted by the user. User must enter this many digits.
        :param object parameter: A single-level JSON object used to pass custom parameters to payment processors. (Required for ACH payments). The information that has to be included here depends on the <Pay> Connector. [Read more](https://www.twilio.com/console/voice/pay-connectors).
        :param str payment_connector: This is the unique name corresponding to the Pay Connector installed in the Twilio Add-ons. Learn more about [<Pay> Connectors](https://www.twilio.com/console/voice/pay-connectors). The default value is `Default`.
        :param &quot;PaymentInstance.PaymentMethod&quot; payment_method:
        :param bool postal_code: Indicates whether the credit card postal code (zip code) is a required piece of payment information that must be provided by the caller. The default is `true`.
        :param bool security_code: Indicates whether the credit card security code is a required piece of payment information that must be provided by the caller. The default is `true`.
        :param int timeout: The number of seconds that <Pay> should wait for the caller to press a digit between each subsequent digit, after the first one, before moving on to validate the digits captured. The default is `5`, maximum is `600`.
        :param &quot;PaymentInstance.TokenType&quot; token_type:
        :param str valid_card_types: Credit card types separated by space that Pay should accept. The default value is `visa mastercard amex`

        :returns: The created PaymentInstance
        """
        data = values.of(
            {
                "IdempotencyKey": idempotency_key,
                "StatusCallback": status_callback,
                "BankAccountType": bank_account_type,
                "ChargeAmount": charge_amount,
                "Currency": currency,
                "Description": description,
                "Input": input,
                "MinPostalCodeLength": min_postal_code_length,
                "Parameter": serialize.object(parameter),
                "PaymentConnector": payment_connector,
                "PaymentMethod": payment_method,
                "PostalCode": postal_code,
                "SecurityCode": security_code,
                "Timeout": timeout,
                "TokenType": token_type,
                "ValidCardTypes": valid_card_types,
            }
        )

        payload = await self._version.create_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return PaymentInstance(
            self._version,
            payload,
            account_sid=self._solution["account_sid"],
            call_sid=self._solution["call_sid"],
        )

    def get(self, sid) -> PaymentContext:
        """
        Constructs a PaymentContext

        :param sid: The SID of Payments session that needs to be updated.
        """
        return PaymentContext(
            self._version,
            account_sid=self._solution["account_sid"],
            call_sid=self._solution["call_sid"],
            sid=sid,
        )

    def __call__(self, sid) -> PaymentContext:
        """
        Constructs a PaymentContext

        :param sid: The SID of Payments session that needs to be updated.
        """
        return PaymentContext(
            self._version,
            account_sid=self._solution["account_sid"],
            call_sid=self._solution["call_sid"],
            sid=sid,
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Api.V2010.PaymentList>"
