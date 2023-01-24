from twilio.rest.media import MediaBase
from warnings import warn


class Media(MediaBase):

    @property
    def media_processor(self):
        warn('media_processor() is deprecated. Use v1.media_processor() instead.', DeprecationWarning, stacklevel=2)
        return self.v1.media_processor

    @property
    def media_recording(self):
        warn('media_recording() is deprecated. Use v1.media_recording() instead.', DeprecationWarning, stacklevel=2)
        return self.v1.media_recording

    @property
    def player_streamer(self):
        warn('player_streamer() is deprecated. Use v1.player_streamer() instead.', DeprecationWarning, stacklevel=2)
        return self.v1.player_streamer
