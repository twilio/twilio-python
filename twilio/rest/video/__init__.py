from twilio.rest.video import VideoBase
from warnings import warn


class Video(VideoBase):

    @property
    def compositions(self):
        warn('compositions() is deprecated. Use v1.compositions() instead.', DeprecationWarning, stacklevel=2)
        return self.v1.compositions

    @property
    def composition_hooks(self):
        warn('composition_hooks() is deprecated. Use v1.composition_hooks() instead.', DeprecationWarning, stacklevel=2)
        return self.v1.composition_hooks

    @property
    def composition_settings(self):
        warn('composition_settings() is deprecated. Use v1.composition_settings() instead.', DeprecationWarning, stacklevel=2)
        return self.v1.composition_settings

    @property
    def recordings(self):
        warn('recordings() is deprecated. Use v1.recordings() instead.', DeprecationWarning, stacklevel=2)
        return self.v1.recordings

    @property
    def recording_settings(self):
        warn('recording_settings() is deprecated. Use v1.recording_settings() instead.', DeprecationWarning, stacklevel=2)
        return self.v1.recording_settings

    @property
    def rooms(self):
        warn('rooms() is deprecated. Use v1.rooms() instead.', DeprecationWarning, stacklevel=2)
        return self.v1.rooms



