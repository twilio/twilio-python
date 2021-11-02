# coding=utf-8
r"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from twilio.base.domain import Domain
from twilio.rest.media.v1 import V1


class Media(Domain):

    def __init__(self, twilio):
        """
        Initialize the Media Domain

        :returns: Domain for Media
        :rtype: twilio.rest.media.Media
        """
        super(Media, self).__init__(twilio)

        self.base_url = 'https://media.twilio.com'

        # Versions
        self._v1 = None

    @property
    def v1(self):
        """
        :returns: Version v1 of media
        :rtype: twilio.rest.media.v1.V1
        """
        if self._v1 is None:
            self._v1 = V1(self)
        return self._v1

    @property
    def media_processor(self):
        """
        :rtype: twilio.rest.media.v1.media_processor.MediaProcessorList
        """
        return self.v1.media_processor

    @property
    def player_streamer(self):
        """
        :rtype: twilio.rest.media.v1.player_streamer.PlayerStreamerList
        """
        return self.v1.player_streamer

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Media>'
