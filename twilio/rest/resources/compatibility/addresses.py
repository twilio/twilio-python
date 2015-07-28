from twilio import TwilioException
from twilio.rest.resources import InstanceResource
from twilio.rest.resources import ListResource


class Address(InstanceResource):
    pass

class Addresses(ListResource):

    def update(self, sid, **kwargs):
        if 'iso_country' in kwargs:
            raise TwilioException(
                'Canont update iso_country on an existing Address'
            )

        return self.update_instance(sid, kwargs)
