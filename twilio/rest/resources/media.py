from .util import normalize_dates, parse_date

from twilio.rest.v2010.account.message.media import (
    Media,
    MediaList as BaseMediaList,
)


class MediaList(BaseMediaList):

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
