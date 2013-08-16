from twilio.rest.resources import InstanceResource, ListResource
from twilio.rest.resources.util import normalize_dates, parse_date


class Image(InstanceResource):
    pass


class Images(ListResource):
    name = "Images"
    key = "images"
    instance = Image


class Media(InstanceResource):
    subresources = [Images]


class MediaList(ListResource):
    name = "Media"
    key = "media"
    instance = Media

    @normalize_dates
    def list(self, before=None, after=None, date_created=None, **kw):
        """
        Returns a page of :class:`Media` resources as a list. For
        paging information see :class:`ListResource`.

        :param date after: Only list media created after this date.
        :param date before: Only list media created before this date.
        :param date date_created: Only list media created on this date.
        :param sid message_sid: Only list media created by the given MessageSid
        """
        kw["DateCreated<"] = before
        kw["DateCreated>"] = after
        kw["DateCreated"] = parse_date(date_created)
        return self.get_instances(kw)
