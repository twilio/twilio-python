from twilio.rest.resources import InstanceResource, ListResource


class Media(InstanceResource):
    pass


class MediaList(ListResource):

    def __call__(self, message_sid):
        base_uri = "%s/Messages/%s" % (self.base_uri, message_sid)
        return MediaList(base_uri, self.auth, self.timeout)
