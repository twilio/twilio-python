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


class PreviewIam(PreviewIamBase):
    @property
    def organization(self) -> OrganizationList:
        return self.versionless.organization

    @property
    def authorize(self) -> AuthorizeList:
        return self.v1.authorize

    @property
    def token(self) -> TokenList:
        return self.v1.token
