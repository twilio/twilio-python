from twilio.rest.preview_iam.PreviewIamBase import PreviewIamBase

from twilio.rest.preview_iam.v1.authorize import (
    AuthorizeList,
)
from twilio.rest.preview_iam.v1.token import (
    TokenList,
)
from twilio.rest.preview_iam.versionless.organization import (
    OrganizationList,
)
from twilio.rest.preview_iam.versionless import Versionless


class PreviewIam(PreviewIamBase):
    @property
    def organization(self) -> OrganizationList:
        return Versionless(self).organization

    @property
    def authorize(self) -> AuthorizeList:
        return self.v1.authorize

    @property
    def token(self) -> TokenList:
        return self.v1.token
