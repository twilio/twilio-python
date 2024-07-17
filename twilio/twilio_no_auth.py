import os
from threading import Lock


class NoAuthTwilioRestClient:
    pass


class TwilioNoAuth:
    _lock = Lock()
    no_auth_twilio_rest_client = None
    user_agent_extensions = None
    region = os.getenv("TWILIO_REGION")
    edge = os.getenv("TWILIO_EDGE")

    @classmethod
    def get_rest_client(cls):
        with cls._lock:
            if cls.no_auth_twilio_rest_client is None:
                cls.no_auth_twilio_rest_client = cls.build_oauth_rest_client()
        return cls.no_auth_twilio_rest_client

    @classmethod
    def build_oauth_rest_client(cls):
        builder = NoAuthTwilioRestClient.Builder()

        if cls.user_agent_extensions is not None:
            builder.user_agent_extensions(cls.user_agent_extensions)

        builder.region(cls.region)
        builder.edge(cls.edge)

        return builder.build()
