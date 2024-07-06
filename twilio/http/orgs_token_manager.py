
from twilio.base.version import Version
from twilio.rest.preview_iam.organizations.token import TokenList

class OrgTokenManager():
    """
    Orgs Token Manager
    """

    def __init__(self, grant_type: str, client_id: str, client_secret: str, code: str = None, redirect_uri: str = None, audience: str = None, refreshToken: str = None, scope: str = None):
        self.grant_type = grant_type
        self.client_id = client_id
        self.client_secret = client_secret
        self.code = code
        self.redirect_uri = redirect_uri
        self.audience = audience
        self.refreshToken = refreshToken
        self.scope = scope

    def fetch_access_token(self, version: Version):
        token_list = TokenList(version)
        token_instance = token_list.create(
            grant_type=self.grant_type,
            client_id=self.client_id,
            client_secret=self.client_secret,
            code=self.code,
            redirect_uri=self.redirect_uri,
            audience=self.audience,
            scope=self.scope
        )
        return token_instance.access_token
