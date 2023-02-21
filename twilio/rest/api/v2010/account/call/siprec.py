"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Api
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""


from twilio.base import deserialize
from twilio.base import serialize
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version



class SiprecList(ListResource):

    def __init__(self, version: Version, account_sid: str, call_sid: str):
        """
        Initialize the SiprecList
        :param Version version: Version that contains the resource
        :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created this Siprec resource.
        :param call_sid: The SID of the [Call](https://www.twilio.com/docs/voice/api/call-resource) the Siprec resource is associated with.
        
        :returns: twilio.api.v2010.siprec..SiprecList
        :rtype: twilio.api.v2010.siprec..SiprecList
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 'account_sid': account_sid, 'call_sid': call_sid,  }
        self._uri = '/Accounts/${account_sid}/Calls/${call_sid}/Siprec.json'.format(**self._solution)
        
        
    
    
    def create(self, name=values.unset, connector_name=values.unset, track=values.unset, status_callback=values.unset, status_callback_method=values.unset, parameter1_name=values.unset, parameter1_value=values.unset, parameter2_name=values.unset, parameter2_value=values.unset, parameter3_name=values.unset, parameter3_value=values.unset, parameter4_name=values.unset, parameter4_value=values.unset, parameter5_name=values.unset, parameter5_value=values.unset, parameter6_name=values.unset, parameter6_value=values.unset, parameter7_name=values.unset, parameter7_value=values.unset, parameter8_name=values.unset, parameter8_value=values.unset, parameter9_name=values.unset, parameter9_value=values.unset, parameter10_name=values.unset, parameter10_value=values.unset, parameter11_name=values.unset, parameter11_value=values.unset, parameter12_name=values.unset, parameter12_value=values.unset, parameter13_name=values.unset, parameter13_value=values.unset, parameter14_name=values.unset, parameter14_value=values.unset, parameter15_name=values.unset, parameter15_value=values.unset, parameter16_name=values.unset, parameter16_value=values.unset, parameter17_name=values.unset, parameter17_value=values.unset, parameter18_name=values.unset, parameter18_value=values.unset, parameter19_name=values.unset, parameter19_value=values.unset, parameter20_name=values.unset, parameter20_value=values.unset, parameter21_name=values.unset, parameter21_value=values.unset, parameter22_name=values.unset, parameter22_value=values.unset, parameter23_name=values.unset, parameter23_value=values.unset, parameter24_name=values.unset, parameter24_value=values.unset, parameter25_name=values.unset, parameter25_value=values.unset, parameter26_name=values.unset, parameter26_value=values.unset, parameter27_name=values.unset, parameter27_value=values.unset, parameter28_name=values.unset, parameter28_value=values.unset, parameter29_name=values.unset, parameter29_value=values.unset, parameter30_name=values.unset, parameter30_value=values.unset, parameter31_name=values.unset, parameter31_value=values.unset, parameter32_name=values.unset, parameter32_value=values.unset, parameter33_name=values.unset, parameter33_value=values.unset, parameter34_name=values.unset, parameter34_value=values.unset, parameter35_name=values.unset, parameter35_value=values.unset, parameter36_name=values.unset, parameter36_value=values.unset, parameter37_name=values.unset, parameter37_value=values.unset, parameter38_name=values.unset, parameter38_value=values.unset, parameter39_name=values.unset, parameter39_value=values.unset, parameter40_name=values.unset, parameter40_value=values.unset, parameter41_name=values.unset, parameter41_value=values.unset, parameter42_name=values.unset, parameter42_value=values.unset, parameter43_name=values.unset, parameter43_value=values.unset, parameter44_name=values.unset, parameter44_value=values.unset, parameter45_name=values.unset, parameter45_value=values.unset, parameter46_name=values.unset, parameter46_value=values.unset, parameter47_name=values.unset, parameter47_value=values.unset, parameter48_name=values.unset, parameter48_value=values.unset, parameter49_name=values.unset, parameter49_value=values.unset, parameter50_name=values.unset, parameter50_value=values.unset, parameter51_name=values.unset, parameter51_value=values.unset, parameter52_name=values.unset, parameter52_value=values.unset, parameter53_name=values.unset, parameter53_value=values.unset, parameter54_name=values.unset, parameter54_value=values.unset, parameter55_name=values.unset, parameter55_value=values.unset, parameter56_name=values.unset, parameter56_value=values.unset, parameter57_name=values.unset, parameter57_value=values.unset, parameter58_name=values.unset, parameter58_value=values.unset, parameter59_name=values.unset, parameter59_value=values.unset, parameter60_name=values.unset, parameter60_value=values.unset, parameter61_name=values.unset, parameter61_value=values.unset, parameter62_name=values.unset, parameter62_value=values.unset, parameter63_name=values.unset, parameter63_value=values.unset, parameter64_name=values.unset, parameter64_value=values.unset, parameter65_name=values.unset, parameter65_value=values.unset, parameter66_name=values.unset, parameter66_value=values.unset, parameter67_name=values.unset, parameter67_value=values.unset, parameter68_name=values.unset, parameter68_value=values.unset, parameter69_name=values.unset, parameter69_value=values.unset, parameter70_name=values.unset, parameter70_value=values.unset, parameter71_name=values.unset, parameter71_value=values.unset, parameter72_name=values.unset, parameter72_value=values.unset, parameter73_name=values.unset, parameter73_value=values.unset, parameter74_name=values.unset, parameter74_value=values.unset, parameter75_name=values.unset, parameter75_value=values.unset, parameter76_name=values.unset, parameter76_value=values.unset, parameter77_name=values.unset, parameter77_value=values.unset, parameter78_name=values.unset, parameter78_value=values.unset, parameter79_name=values.unset, parameter79_value=values.unset, parameter80_name=values.unset, parameter80_value=values.unset, parameter81_name=values.unset, parameter81_value=values.unset, parameter82_name=values.unset, parameter82_value=values.unset, parameter83_name=values.unset, parameter83_value=values.unset, parameter84_name=values.unset, parameter84_value=values.unset, parameter85_name=values.unset, parameter85_value=values.unset, parameter86_name=values.unset, parameter86_value=values.unset, parameter87_name=values.unset, parameter87_value=values.unset, parameter88_name=values.unset, parameter88_value=values.unset, parameter89_name=values.unset, parameter89_value=values.unset, parameter90_name=values.unset, parameter90_value=values.unset, parameter91_name=values.unset, parameter91_value=values.unset, parameter92_name=values.unset, parameter92_value=values.unset, parameter93_name=values.unset, parameter93_value=values.unset, parameter94_name=values.unset, parameter94_value=values.unset, parameter95_name=values.unset, parameter95_value=values.unset, parameter96_name=values.unset, parameter96_value=values.unset, parameter97_name=values.unset, parameter97_value=values.unset, parameter98_name=values.unset, parameter98_value=values.unset, parameter99_name=values.unset, parameter99_value=values.unset):
        """
        Create the SiprecInstance
         :param str name: The user-specified name of this Siprec, if one was given when the Siprec was created. This may be used to stop the Siprec.
         :param str connector_name: Unique name used when configuring the connector via Marketplace Add-on.
         :param SiprecTrack track: 
         :param str status_callback: Absolute URL of the status callback.
         :param str status_callback_method: The http method for the status_callback (one of GET, POST).
         :param str parameter1_name: Parameter name
         :param str parameter1_value: Parameter value
         :param str parameter2_name: Parameter name
         :param str parameter2_value: Parameter value
         :param str parameter3_name: Parameter name
         :param str parameter3_value: Parameter value
         :param str parameter4_name: Parameter name
         :param str parameter4_value: Parameter value
         :param str parameter5_name: Parameter name
         :param str parameter5_value: Parameter value
         :param str parameter6_name: Parameter name
         :param str parameter6_value: Parameter value
         :param str parameter7_name: Parameter name
         :param str parameter7_value: Parameter value
         :param str parameter8_name: Parameter name
         :param str parameter8_value: Parameter value
         :param str parameter9_name: Parameter name
         :param str parameter9_value: Parameter value
         :param str parameter10_name: Parameter name
         :param str parameter10_value: Parameter value
         :param str parameter11_name: Parameter name
         :param str parameter11_value: Parameter value
         :param str parameter12_name: Parameter name
         :param str parameter12_value: Parameter value
         :param str parameter13_name: Parameter name
         :param str parameter13_value: Parameter value
         :param str parameter14_name: Parameter name
         :param str parameter14_value: Parameter value
         :param str parameter15_name: Parameter name
         :param str parameter15_value: Parameter value
         :param str parameter16_name: Parameter name
         :param str parameter16_value: Parameter value
         :param str parameter17_name: Parameter name
         :param str parameter17_value: Parameter value
         :param str parameter18_name: Parameter name
         :param str parameter18_value: Parameter value
         :param str parameter19_name: Parameter name
         :param str parameter19_value: Parameter value
         :param str parameter20_name: Parameter name
         :param str parameter20_value: Parameter value
         :param str parameter21_name: Parameter name
         :param str parameter21_value: Parameter value
         :param str parameter22_name: Parameter name
         :param str parameter22_value: Parameter value
         :param str parameter23_name: Parameter name
         :param str parameter23_value: Parameter value
         :param str parameter24_name: Parameter name
         :param str parameter24_value: Parameter value
         :param str parameter25_name: Parameter name
         :param str parameter25_value: Parameter value
         :param str parameter26_name: Parameter name
         :param str parameter26_value: Parameter value
         :param str parameter27_name: Parameter name
         :param str parameter27_value: Parameter value
         :param str parameter28_name: Parameter name
         :param str parameter28_value: Parameter value
         :param str parameter29_name: Parameter name
         :param str parameter29_value: Parameter value
         :param str parameter30_name: Parameter name
         :param str parameter30_value: Parameter value
         :param str parameter31_name: Parameter name
         :param str parameter31_value: Parameter value
         :param str parameter32_name: Parameter name
         :param str parameter32_value: Parameter value
         :param str parameter33_name: Parameter name
         :param str parameter33_value: Parameter value
         :param str parameter34_name: Parameter name
         :param str parameter34_value: Parameter value
         :param str parameter35_name: Parameter name
         :param str parameter35_value: Parameter value
         :param str parameter36_name: Parameter name
         :param str parameter36_value: Parameter value
         :param str parameter37_name: Parameter name
         :param str parameter37_value: Parameter value
         :param str parameter38_name: Parameter name
         :param str parameter38_value: Parameter value
         :param str parameter39_name: Parameter name
         :param str parameter39_value: Parameter value
         :param str parameter40_name: Parameter name
         :param str parameter40_value: Parameter value
         :param str parameter41_name: Parameter name
         :param str parameter41_value: Parameter value
         :param str parameter42_name: Parameter name
         :param str parameter42_value: Parameter value
         :param str parameter43_name: Parameter name
         :param str parameter43_value: Parameter value
         :param str parameter44_name: Parameter name
         :param str parameter44_value: Parameter value
         :param str parameter45_name: Parameter name
         :param str parameter45_value: Parameter value
         :param str parameter46_name: Parameter name
         :param str parameter46_value: Parameter value
         :param str parameter47_name: Parameter name
         :param str parameter47_value: Parameter value
         :param str parameter48_name: Parameter name
         :param str parameter48_value: Parameter value
         :param str parameter49_name: Parameter name
         :param str parameter49_value: Parameter value
         :param str parameter50_name: Parameter name
         :param str parameter50_value: Parameter value
         :param str parameter51_name: Parameter name
         :param str parameter51_value: Parameter value
         :param str parameter52_name: Parameter name
         :param str parameter52_value: Parameter value
         :param str parameter53_name: Parameter name
         :param str parameter53_value: Parameter value
         :param str parameter54_name: Parameter name
         :param str parameter54_value: Parameter value
         :param str parameter55_name: Parameter name
         :param str parameter55_value: Parameter value
         :param str parameter56_name: Parameter name
         :param str parameter56_value: Parameter value
         :param str parameter57_name: Parameter name
         :param str parameter57_value: Parameter value
         :param str parameter58_name: Parameter name
         :param str parameter58_value: Parameter value
         :param str parameter59_name: Parameter name
         :param str parameter59_value: Parameter value
         :param str parameter60_name: Parameter name
         :param str parameter60_value: Parameter value
         :param str parameter61_name: Parameter name
         :param str parameter61_value: Parameter value
         :param str parameter62_name: Parameter name
         :param str parameter62_value: Parameter value
         :param str parameter63_name: Parameter name
         :param str parameter63_value: Parameter value
         :param str parameter64_name: Parameter name
         :param str parameter64_value: Parameter value
         :param str parameter65_name: Parameter name
         :param str parameter65_value: Parameter value
         :param str parameter66_name: Parameter name
         :param str parameter66_value: Parameter value
         :param str parameter67_name: Parameter name
         :param str parameter67_value: Parameter value
         :param str parameter68_name: Parameter name
         :param str parameter68_value: Parameter value
         :param str parameter69_name: Parameter name
         :param str parameter69_value: Parameter value
         :param str parameter70_name: Parameter name
         :param str parameter70_value: Parameter value
         :param str parameter71_name: Parameter name
         :param str parameter71_value: Parameter value
         :param str parameter72_name: Parameter name
         :param str parameter72_value: Parameter value
         :param str parameter73_name: Parameter name
         :param str parameter73_value: Parameter value
         :param str parameter74_name: Parameter name
         :param str parameter74_value: Parameter value
         :param str parameter75_name: Parameter name
         :param str parameter75_value: Parameter value
         :param str parameter76_name: Parameter name
         :param str parameter76_value: Parameter value
         :param str parameter77_name: Parameter name
         :param str parameter77_value: Parameter value
         :param str parameter78_name: Parameter name
         :param str parameter78_value: Parameter value
         :param str parameter79_name: Parameter name
         :param str parameter79_value: Parameter value
         :param str parameter80_name: Parameter name
         :param str parameter80_value: Parameter value
         :param str parameter81_name: Parameter name
         :param str parameter81_value: Parameter value
         :param str parameter82_name: Parameter name
         :param str parameter82_value: Parameter value
         :param str parameter83_name: Parameter name
         :param str parameter83_value: Parameter value
         :param str parameter84_name: Parameter name
         :param str parameter84_value: Parameter value
         :param str parameter85_name: Parameter name
         :param str parameter85_value: Parameter value
         :param str parameter86_name: Parameter name
         :param str parameter86_value: Parameter value
         :param str parameter87_name: Parameter name
         :param str parameter87_value: Parameter value
         :param str parameter88_name: Parameter name
         :param str parameter88_value: Parameter value
         :param str parameter89_name: Parameter name
         :param str parameter89_value: Parameter value
         :param str parameter90_name: Parameter name
         :param str parameter90_value: Parameter value
         :param str parameter91_name: Parameter name
         :param str parameter91_value: Parameter value
         :param str parameter92_name: Parameter name
         :param str parameter92_value: Parameter value
         :param str parameter93_name: Parameter name
         :param str parameter93_value: Parameter value
         :param str parameter94_name: Parameter name
         :param str parameter94_value: Parameter value
         :param str parameter95_name: Parameter name
         :param str parameter95_value: Parameter value
         :param str parameter96_name: Parameter name
         :param str parameter96_value: Parameter value
         :param str parameter97_name: Parameter name
         :param str parameter97_value: Parameter value
         :param str parameter98_name: Parameter name
         :param str parameter98_value: Parameter value
         :param str parameter99_name: Parameter name
         :param str parameter99_value: Parameter value
        
        :returns: The created SiprecInstance
        :rtype: twilio.rest.api.v2010.siprec.SiprecInstance
        """
        data = values.of({ 
            'Name': name,
            'ConnectorName': connector_name,
            'Track': track,
            'StatusCallback': status_callback,
            'StatusCallbackMethod': status_callback_method,
            'Parameter1.Name': parameter1_name,
            'Parameter1.Value': parameter1_value,
            'Parameter2.Name': parameter2_name,
            'Parameter2.Value': parameter2_value,
            'Parameter3.Name': parameter3_name,
            'Parameter3.Value': parameter3_value,
            'Parameter4.Name': parameter4_name,
            'Parameter4.Value': parameter4_value,
            'Parameter5.Name': parameter5_name,
            'Parameter5.Value': parameter5_value,
            'Parameter6.Name': parameter6_name,
            'Parameter6.Value': parameter6_value,
            'Parameter7.Name': parameter7_name,
            'Parameter7.Value': parameter7_value,
            'Parameter8.Name': parameter8_name,
            'Parameter8.Value': parameter8_value,
            'Parameter9.Name': parameter9_name,
            'Parameter9.Value': parameter9_value,
            'Parameter10.Name': parameter10_name,
            'Parameter10.Value': parameter10_value,
            'Parameter11.Name': parameter11_name,
            'Parameter11.Value': parameter11_value,
            'Parameter12.Name': parameter12_name,
            'Parameter12.Value': parameter12_value,
            'Parameter13.Name': parameter13_name,
            'Parameter13.Value': parameter13_value,
            'Parameter14.Name': parameter14_name,
            'Parameter14.Value': parameter14_value,
            'Parameter15.Name': parameter15_name,
            'Parameter15.Value': parameter15_value,
            'Parameter16.Name': parameter16_name,
            'Parameter16.Value': parameter16_value,
            'Parameter17.Name': parameter17_name,
            'Parameter17.Value': parameter17_value,
            'Parameter18.Name': parameter18_name,
            'Parameter18.Value': parameter18_value,
            'Parameter19.Name': parameter19_name,
            'Parameter19.Value': parameter19_value,
            'Parameter20.Name': parameter20_name,
            'Parameter20.Value': parameter20_value,
            'Parameter21.Name': parameter21_name,
            'Parameter21.Value': parameter21_value,
            'Parameter22.Name': parameter22_name,
            'Parameter22.Value': parameter22_value,
            'Parameter23.Name': parameter23_name,
            'Parameter23.Value': parameter23_value,
            'Parameter24.Name': parameter24_name,
            'Parameter24.Value': parameter24_value,
            'Parameter25.Name': parameter25_name,
            'Parameter25.Value': parameter25_value,
            'Parameter26.Name': parameter26_name,
            'Parameter26.Value': parameter26_value,
            'Parameter27.Name': parameter27_name,
            'Parameter27.Value': parameter27_value,
            'Parameter28.Name': parameter28_name,
            'Parameter28.Value': parameter28_value,
            'Parameter29.Name': parameter29_name,
            'Parameter29.Value': parameter29_value,
            'Parameter30.Name': parameter30_name,
            'Parameter30.Value': parameter30_value,
            'Parameter31.Name': parameter31_name,
            'Parameter31.Value': parameter31_value,
            'Parameter32.Name': parameter32_name,
            'Parameter32.Value': parameter32_value,
            'Parameter33.Name': parameter33_name,
            'Parameter33.Value': parameter33_value,
            'Parameter34.Name': parameter34_name,
            'Parameter34.Value': parameter34_value,
            'Parameter35.Name': parameter35_name,
            'Parameter35.Value': parameter35_value,
            'Parameter36.Name': parameter36_name,
            'Parameter36.Value': parameter36_value,
            'Parameter37.Name': parameter37_name,
            'Parameter37.Value': parameter37_value,
            'Parameter38.Name': parameter38_name,
            'Parameter38.Value': parameter38_value,
            'Parameter39.Name': parameter39_name,
            'Parameter39.Value': parameter39_value,
            'Parameter40.Name': parameter40_name,
            'Parameter40.Value': parameter40_value,
            'Parameter41.Name': parameter41_name,
            'Parameter41.Value': parameter41_value,
            'Parameter42.Name': parameter42_name,
            'Parameter42.Value': parameter42_value,
            'Parameter43.Name': parameter43_name,
            'Parameter43.Value': parameter43_value,
            'Parameter44.Name': parameter44_name,
            'Parameter44.Value': parameter44_value,
            'Parameter45.Name': parameter45_name,
            'Parameter45.Value': parameter45_value,
            'Parameter46.Name': parameter46_name,
            'Parameter46.Value': parameter46_value,
            'Parameter47.Name': parameter47_name,
            'Parameter47.Value': parameter47_value,
            'Parameter48.Name': parameter48_name,
            'Parameter48.Value': parameter48_value,
            'Parameter49.Name': parameter49_name,
            'Parameter49.Value': parameter49_value,
            'Parameter50.Name': parameter50_name,
            'Parameter50.Value': parameter50_value,
            'Parameter51.Name': parameter51_name,
            'Parameter51.Value': parameter51_value,
            'Parameter52.Name': parameter52_name,
            'Parameter52.Value': parameter52_value,
            'Parameter53.Name': parameter53_name,
            'Parameter53.Value': parameter53_value,
            'Parameter54.Name': parameter54_name,
            'Parameter54.Value': parameter54_value,
            'Parameter55.Name': parameter55_name,
            'Parameter55.Value': parameter55_value,
            'Parameter56.Name': parameter56_name,
            'Parameter56.Value': parameter56_value,
            'Parameter57.Name': parameter57_name,
            'Parameter57.Value': parameter57_value,
            'Parameter58.Name': parameter58_name,
            'Parameter58.Value': parameter58_value,
            'Parameter59.Name': parameter59_name,
            'Parameter59.Value': parameter59_value,
            'Parameter60.Name': parameter60_name,
            'Parameter60.Value': parameter60_value,
            'Parameter61.Name': parameter61_name,
            'Parameter61.Value': parameter61_value,
            'Parameter62.Name': parameter62_name,
            'Parameter62.Value': parameter62_value,
            'Parameter63.Name': parameter63_name,
            'Parameter63.Value': parameter63_value,
            'Parameter64.Name': parameter64_name,
            'Parameter64.Value': parameter64_value,
            'Parameter65.Name': parameter65_name,
            'Parameter65.Value': parameter65_value,
            'Parameter66.Name': parameter66_name,
            'Parameter66.Value': parameter66_value,
            'Parameter67.Name': parameter67_name,
            'Parameter67.Value': parameter67_value,
            'Parameter68.Name': parameter68_name,
            'Parameter68.Value': parameter68_value,
            'Parameter69.Name': parameter69_name,
            'Parameter69.Value': parameter69_value,
            'Parameter70.Name': parameter70_name,
            'Parameter70.Value': parameter70_value,
            'Parameter71.Name': parameter71_name,
            'Parameter71.Value': parameter71_value,
            'Parameter72.Name': parameter72_name,
            'Parameter72.Value': parameter72_value,
            'Parameter73.Name': parameter73_name,
            'Parameter73.Value': parameter73_value,
            'Parameter74.Name': parameter74_name,
            'Parameter74.Value': parameter74_value,
            'Parameter75.Name': parameter75_name,
            'Parameter75.Value': parameter75_value,
            'Parameter76.Name': parameter76_name,
            'Parameter76.Value': parameter76_value,
            'Parameter77.Name': parameter77_name,
            'Parameter77.Value': parameter77_value,
            'Parameter78.Name': parameter78_name,
            'Parameter78.Value': parameter78_value,
            'Parameter79.Name': parameter79_name,
            'Parameter79.Value': parameter79_value,
            'Parameter80.Name': parameter80_name,
            'Parameter80.Value': parameter80_value,
            'Parameter81.Name': parameter81_name,
            'Parameter81.Value': parameter81_value,
            'Parameter82.Name': parameter82_name,
            'Parameter82.Value': parameter82_value,
            'Parameter83.Name': parameter83_name,
            'Parameter83.Value': parameter83_value,
            'Parameter84.Name': parameter84_name,
            'Parameter84.Value': parameter84_value,
            'Parameter85.Name': parameter85_name,
            'Parameter85.Value': parameter85_value,
            'Parameter86.Name': parameter86_name,
            'Parameter86.Value': parameter86_value,
            'Parameter87.Name': parameter87_name,
            'Parameter87.Value': parameter87_value,
            'Parameter88.Name': parameter88_name,
            'Parameter88.Value': parameter88_value,
            'Parameter89.Name': parameter89_name,
            'Parameter89.Value': parameter89_value,
            'Parameter90.Name': parameter90_name,
            'Parameter90.Value': parameter90_value,
            'Parameter91.Name': parameter91_name,
            'Parameter91.Value': parameter91_value,
            'Parameter92.Name': parameter92_name,
            'Parameter92.Value': parameter92_value,
            'Parameter93.Name': parameter93_name,
            'Parameter93.Value': parameter93_value,
            'Parameter94.Name': parameter94_name,
            'Parameter94.Value': parameter94_value,
            'Parameter95.Name': parameter95_name,
            'Parameter95.Value': parameter95_value,
            'Parameter96.Name': parameter96_name,
            'Parameter96.Value': parameter96_value,
            'Parameter97.Name': parameter97_name,
            'Parameter97.Value': parameter97_value,
            'Parameter98.Name': parameter98_name,
            'Parameter98.Value': parameter98_value,
            'Parameter99.Name': parameter99_name,
            'Parameter99.Value': parameter99_value,
        })

        payload = self._version.create(method='POST', uri=self._uri, data=data)
        return SiprecInstance(self._version, payload, account_sid=self._solution['account_sid'], call_sid=self._solution['call_sid'])
    

    def get(self, sid):
        """
        Constructs a SiprecContext
        
        :param sid: The SID of the Siprec resource, or the `name` used when creating the resource
        
        :returns: twilio.rest.api.v2010.siprec.SiprecContext
        :rtype: twilio.rest.api.v2010.siprec.SiprecContext
        """
        return SiprecContext(self._version, account_sid=self._solution['account_sid'], call_sid=self._solution['call_sid'], sid=sid)

    def __call__(self, sid):
        """
        Constructs a SiprecContext
        
        :param sid: The SID of the Siprec resource, or the `name` used when creating the resource
        
        :returns: twilio.rest.api.v2010.siprec.SiprecContext
        :rtype: twilio.rest.api.v2010.siprec.SiprecContext
        """
        return SiprecContext(self._version, account_sid=self._solution['account_sid'], call_sid=self._solution['call_sid'], sid=sid)

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.SiprecList>'


class SiprecContext(InstanceContext):
    def __init__(self, version: Version, account_sid: str, call_sid: str, sid: str):
        # TODO: needs autogenerated docs
        super().__init__(version)

        # Path Solution
        self._solution = { 'account_sid': account_sid, 'call_sid': call_sid, 'sid': sid,  }
        self._uri = '/Accounts/${account_sid}/Calls/${call_sid}/Siprec/${sid}.json'
        
    
    def update(self, status):
        data = values.of({
            'status': status,
        })

        payload = self._version.update(method='post', uri=self._uri, data=data, )

        return SiprecInstance(self._version, payload, account_sid=self._solution['account_sid'], call_sid=self._solution['call_sid'], sid=self._solution['sid'], )
        
        

        
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.SiprecContext>'



class SiprecInstance(InstanceResource):
    def __init__(self, version, payload, account_sid: str, call_sid: str, sid: str):
        super().__init__(version)
        self._properties = { 
            'sid' : payload.get('sid'),
            'account_sid' : payload.get('account_sid'),
            'call_sid' : payload.get('call_sid'),
            'name' : payload.get('name'),
            'status' : payload.get('status'),
            'date_updated' : payload.get('date_updated'),
            'uri' : payload.get('uri'),
        }

        self._context = None
        self._solution = {
            'account_sid': account_sid or self._properties['account_sid'],'call_sid': call_sid or self._properties['call_sid'],'sid': sid or self._properties['sid'],
        }

    @property
    def _proxy(self):
        if self._context is None:
            self._context = SiprecContext(
                self._version,
                account_sid=self._solution['account_sid'],call_sid=self._solution['call_sid'],sid=self._solution['sid'],
            )
        return self._context

    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Api.V2010.SiprecInstance {}>'.format(context)



