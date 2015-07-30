from .util import normalize_dates, parse_date

from v2010.account.message.media import (
    Media,
    MediaList as BaseMediaList,
)


class MediaList(BaseMediaList):

    def __call__(self, message_sid):
        # `Media` is a word of ambiguous plurality. This causes issues.
        # To match the rest of the library:
        # `client.media` needs to return a new MediaList.
        # `client.media('message_sid')` needs to return a MediaList
        # for a given message.

        base_uri = "%s/Messages/%s" % (self.base_uri, message_sid)
        return MediaList(base_uri, self.auth, self.timeout)

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
