from .util import parse_date, normalize_dates

from twilio.rest.v2010.account.conference.participant import (
    Participant,
    Participants,
)
from twilio.rest.v2010.account.conference import (
    Conference,
    Conferences as BaseConferences,
)


class Conferences(BaseConferences):

    @normalize_dates
    def list(self, updated_before=None, updated_after=None, created_after=None,
             created_before=None, updated=None, created=None, **kwargs):
        """
        Return a list of :class:`Conference` resources

        :param status: Show conferences with this status
        :param friendly_name: Show conferences with this exact friendly_name
        :param date updated_after: List conferences updated after this date
        :param date updated_before: List conferences updated before this date
        :param date created_after: List conferences created after this date
        :param date created_before: List conferences created before this date
        """
        kwargs["DateUpdated"] = parse_date(kwargs.get("date_updated", updated))
        kwargs["DateCreated"] = parse_date(kwargs.get("date_created", created))
        kwargs["DateUpdated<"] = updated_before
        kwargs["DateUpdated>"] = updated_after
        kwargs["DateCreated<"] = created_before
        kwargs["DateCreated>"] = created_after
        return self.get_instances(kwargs)
