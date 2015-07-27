from twilio.rest.resources.available_phone_numbers import AvailablePhoneNumbers
from twilio.rest.resources.base import ListResource, InstanceResource
from twilio.rest.resources.incoming_phone_numbers import IncomingPhoneNumbers


class Account(InstanceResource):
    def __init__(self, *args, **kwargs):
        super(Account, self).__init__(*args, **kwargs)

        # AvailablePhoneNumbers require incoming phone numbers
        # in its constructor to allow purchase directly
        # from the instance itself
        self.subresources = [
            subresource for subresource in self.subresources
            if subresource is not AvailablePhoneNumbers
        ]

    def load_subresources(self):
        """
        Load all subresources
        """
        for resource in self.subresources:
            list_resource = resource(
                self.uri,
                self.parent.auth,
                self.parent.timeout
            )
            self.__dict__[list_resource.key] = list_resource

        available_phone_numbers = AvailablePhoneNumbers(
            self.uri, self.parent.auth, self.parent.timeout,
            self.__dict__[IncomingPhoneNumbers.key])
        self.__dict__[available_phone_numbers.key] = available_phone_numbers


class Accounts(ListResource):
    pass
