r"""
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


from datetime import date, datetime
from decimal import Decimal
from typing import Any, Dict, List, Optional, Union, Iterator, AsyncIterator
from twilio.base import deserialize, serialize, values


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

        :param version: Version that contains the resource
        
        """
        super().__init__(version)

        
        self._uri = '/RegulatoryCompliance'
        
        self._bundles: Optional[BundleList] = None
        self._end_users: Optional[EndUserList] = None
        self._end_user_types: Optional[EndUserTypeList] = None
        self._regulations: Optional[RegulationList] = None
        self._supporting_documents: Optional[SupportingDocumentList] = None
        self._supporting_document_types: Optional[SupportingDocumentTypeList] = None
        



    @property
    def bundles(self) -> BundleList:
        """
        Access the bundles
        """
        if self._bundles is None:
            self._bundles = BundleList(self._version)
        return self._bundles



    @property
    def end_users(self) -> EndUserList:
        """
        Access the end_users
        """
        if self._end_users is None:
            self._end_users = EndUserList(self._version)
        return self._end_users



    @property
    def end_user_types(self) -> EndUserTypeList:
        """
        Access the end_user_types
        """
        if self._end_user_types is None:
            self._end_user_types = EndUserTypeList(self._version)
        return self._end_user_types



    @property
    def regulations(self) -> RegulationList:
        """
        Access the regulations
        """
        if self._regulations is None:
            self._regulations = RegulationList(self._version)
        return self._regulations



    @property
    def supporting_documents(self) -> SupportingDocumentList:
        """
        Access the supporting_documents
        """
        if self._supporting_documents is None:
            self._supporting_documents = SupportingDocumentList(self._version)
        return self._supporting_documents



    @property
    def supporting_document_types(self) -> SupportingDocumentTypeList:
        """
        Access the supporting_document_types
        """
        if self._supporting_document_types is None:
            self._supporting_document_types = SupportingDocumentTypeList(self._version)
        return self._supporting_document_types



    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return '<Twilio.Numbers.V2.RegulatoryComplianceList>'

