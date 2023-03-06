"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Numbers
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""


from datetime import date
from twilio.base import deserialize
from twilio.base import serialize
from twilio.base import values


from twilio.base.list_resource import ListResource
from twilio.base.version import Version

from twilio.rest.numbers.v2.regulatory_compliance.bundle import BundleList
from twilio.rest.numbers.v2.regulatory_compliance.end_user import EndUserList
from twilio.rest.numbers.v2.regulatory_compliance.end_user_type import EndUserTypeList
from twilio.rest.numbers.v2.regulatory_compliance.regulation import RegulationList
from twilio.rest.numbers.v2.regulatory_compliance.supporting_document import SupportingDocumentList
from twilio.rest.numbers.v2.regulatory_compliance.supporting_document_type import SupportingDocumentTypeList


class RegulatoryComplianceList(ListResource):

    def __init__(self, version: Version):
        """
        Initialize the RegulatoryComplianceList

        :param Version version: Version that contains the resource
        
        :returns: twilio.rest.numbers.v2.regulatory_compliance.RegulatoryComplianceList
        :rtype: twilio.rest.numbers.v2.regulatory_compliance.RegulatoryComplianceList
        """
        super().__init__(version)

        # Path Solution
        self._solution = {  }
        self._uri = '/RegulatoryCompliance'.format(**self._solution)
        
        self._bundles = None
        self._end_users = None
        self._end_user_types = None
        self._regulations = None
        self._supporting_documents = None
        self._supporting_document_types = None
        

    @property
    def bundles(self):
        """
        Access the bundles

        :returns: twilio.rest.numbers.v2.regulatory_compliance.BundleList
        :rtype: twilio.rest.numbers.v2.regulatory_compliance.BundleList
        """
        if self._bundles is None:
            self._bundles = BundleList(self._version)
        return self._bundles

    @property
    def end_users(self):
        """
        Access the end_users

        :returns: twilio.rest.numbers.v2.regulatory_compliance.EndUserList
        :rtype: twilio.rest.numbers.v2.regulatory_compliance.EndUserList
        """
        if self._end_users is None:
            self._end_users = EndUserList(self._version)
        return self._end_users

    @property
    def end_user_types(self):
        """
        Access the end_user_types

        :returns: twilio.rest.numbers.v2.regulatory_compliance.EndUserTypeList
        :rtype: twilio.rest.numbers.v2.regulatory_compliance.EndUserTypeList
        """
        if self._end_user_types is None:
            self._end_user_types = EndUserTypeList(self._version)
        return self._end_user_types

    @property
    def regulations(self):
        """
        Access the regulations

        :returns: twilio.rest.numbers.v2.regulatory_compliance.RegulationList
        :rtype: twilio.rest.numbers.v2.regulatory_compliance.RegulationList
        """
        if self._regulations is None:
            self._regulations = RegulationList(self._version)
        return self._regulations

    @property
    def supporting_documents(self):
        """
        Access the supporting_documents

        :returns: twilio.rest.numbers.v2.regulatory_compliance.SupportingDocumentList
        :rtype: twilio.rest.numbers.v2.regulatory_compliance.SupportingDocumentList
        """
        if self._supporting_documents is None:
            self._supporting_documents = SupportingDocumentList(self._version)
        return self._supporting_documents

    @property
    def supporting_document_types(self):
        """
        Access the supporting_document_types

        :returns: twilio.rest.numbers.v2.regulatory_compliance.SupportingDocumentTypeList
        :rtype: twilio.rest.numbers.v2.regulatory_compliance.SupportingDocumentTypeList
        """
        if self._supporting_document_types is None:
            self._supporting_document_types = SupportingDocumentTypeList(self._version)
        return self._supporting_document_types


    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Numbers.V2.RegulatoryComplianceList>'




