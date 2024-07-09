from twilio.base.version import Version
from twilio.http.orgs_token_manager import OrgTokenManager
class TokenManager:
    org_token_manager = None

    @classmethod
    def init(cls, grant_type: str, client_id: str, client_secret: str, code: str = None, redirect_uri: str = None, audience: str = None, refreshToken: str = None, scope: str = None, tokenManager: OrgTokenManager = None):
        if tokenManager is None:
            cls.org_token_manager = OrgTokenManager(grant_type, client_id, client_secret, code, redirect_uri, audience, refreshToken, scope)
        else:
            cls.org_token_manager = tokenManager

    @classmethod
    def get_token_manager(cls, version: Version):
        if cls.org_token_manager is None:
            raise Exception("Token Manager not initialized")
        cls.org_token_manager.version = version
        return cls.org_token_manager
