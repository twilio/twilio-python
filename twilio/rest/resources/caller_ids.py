from . import transform_params
from . import InstanceResource, ListResource

from v2010.account.outgoing_caller_id import (
    OutgoingCallerId as CallerId,
    OutgoingCallerIds as BaseCallerIds,
)


class CallerIds(BaseCallerIds):

    def validate(self, phone_number, **kwargs):
        """
        Begin the validation process for the given number.

        Returns a dictionary with the following keys

        **account_sid**:
        The unique id of the Account to which the Validation Request belongs.

        **phone_number**: The incoming phone number being validated,
        formatted with a '+' and country code e.g., +16175551212

        **friendly_name**: The friendly name you provided, if any.

        **validation_code**: The 6 digit validation code that must be entered
        via the phone to validate this phone number for Caller ID.

        :param phone_number: The phone number to call and validate
        :param friendly_name: A description for the new caller ID
        :param call_delay: Number of seconds to delay the validation call.
        :param extension: Digits to dial after connecting the validation call.
        :returns: A response dictionary
        """
        kwargs["phone_number"] = phone_number
        params = transform_params(kwargs)
        resp, validation = self.request("POST", self.uri, data=params)
        return validation
