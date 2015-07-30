from .util import normalize_dates
from v2010.account.recording import (
    Recording as BaseRecording,
    Recordings as BaseRecordings,
)


class Recording(BaseRecording):

    def __init__(self, *args, **kwargs):
        super(Recording, self).__init__(*args, **kwargs)
        self.formats = {
            "mp3": self.uri + ".mp3",
            "wav": self.uri + ".wav",
        }


class Recordings(BaseRecordings):

    instance = Recording

    @normalize_dates
    def list(self, before=None, after=None, **kwargs):
        """
        Returns a page of :class:`Recording` resources as a list.
        For paging information see :class:`ListResource`.

        :param date after: Only list recordings logged after this datetime
        :param date before: Only list recordings logger before this datetime
        :param call_sid: Only list recordings from this :class:`Call`
        """
        kwargs["DateCreated<"] = before
        kwargs["DateCreated>"] = after
        return self.get_instances(kwargs)
