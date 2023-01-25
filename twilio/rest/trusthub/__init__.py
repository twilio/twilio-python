from twilio.rest.trusthub import TrusthubBase
from warnings import warn


class Trusthub(TrusthubBase):

    @property
    def customer_profiles(self):
        warn('customer_profiles() is deprecated. Use v1.customer_profiles() instead.', DeprecationWarning, stacklevel=2)
        return self.v1.customer_profiles

    @property
    def end_users(self):
        warn('end_users() is deprecated. Use v1.end_users() instead.', DeprecationWarning, stacklevel=2)
        return self.v1.end_users

    @property
    def end_user_types(self):
        warn('end_user_types() is deprecated. Use v1.end_user_types() instead.', DeprecationWarning, stacklevel=2)
        return self.v1.end_user_types

    @property
    def policies(self):
        warn('policies() is deprecated. Use v1.policies() instead.', DeprecationWarning, stacklevel=2)
        return self.v1.policies

    @property
    def supporting_documents(self):
        warn('supporting_documents() is deprecated. Use v1.supporting_documents() instead.', DeprecationWarning, stacklevel=2)
        return self.v1.supporting_documents

    @property
    def supporting_document_types(self):
        warn('supporting_document_types() is deprecated. Use v1.supporting_document_types() instead.', DeprecationWarning, stacklevel=2)
        return self.v1.supporting_document_types

    @property
    def trust_products(self):
        warn('trust_products() is deprecated. Use v1.trust_products() instead.', DeprecationWarning, stacklevel=2)
        return self.v1.trust_products
