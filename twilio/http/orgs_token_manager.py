from twilio.rest.preview_iam.organizations_openapi.token import TokenList
from twilio.http.http_client import TwilioHttpClient

class OrgTokenManager:
    """
    Orgs Token Manager
    """
    def __init__(self, grant_type: str, client_id: str, client_secret: str):
        self.grant_type = grant_type
        self.client_id = client_id
        self.client_secret = client_secret

    def __init__(self, grant_type: str, client_id: str, client_secret: str, code: str, redirect_uri: str, audience: str, refreshToken: str, scope: str):
        self.grant_type = grant_type
        self.client_id = client_id
        self.client_secret = client_secret
        self.code = code
        self.redirect_uri = redirect_uri
        self.audience = audience
        self.refreshToken = refreshToken
        self.scope = scope

    def fetch_access_token(self):
        token_list = TokenList()
        token_list.create(
            grant_type=self.grant_type,
            client_id=self.client_id,
            client_secret=self.client_secret,
            code=self.code,
            redirect_uri=self.redirect_uri,
            audience=self.audience,
            scope=self.scope
        )
