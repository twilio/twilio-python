# coding=utf-8
r"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from twilio.base import deserialize
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.page import Page


class StreamList(ListResource):

    def __init__(self, version, account_sid, call_sid):
        """
        Initialize the StreamList

        :param Version version: Version that contains the resource
        :param account_sid: The SID of the Account that created this resource
        :param call_sid: The SID of the Call the resource is associated with

        :returns: twilio.rest.api.v2010.account.call.stream.StreamList
        :rtype: twilio.rest.api.v2010.account.call.stream.StreamList
        """
        super(StreamList, self).__init__(version)

        # Path Solution
        self._solution = {'account_sid': account_sid, 'call_sid': call_sid, }
        self._uri = '/Accounts/{account_sid}/Calls/{call_sid}/Streams.json'.format(**self._solution)

    def create(self, name=values.unset, url=values.unset, track=values.unset,
               status_callback=values.unset, status_callback_method=values.unset,
               parameter1_name=values.unset, parameter1_value=values.unset,
               parameter2_name=values.unset, parameter2_value=values.unset,
               parameter3_name=values.unset, parameter3_value=values.unset,
               parameter4_name=values.unset, parameter4_value=values.unset,
               parameter5_name=values.unset, parameter5_value=values.unset,
               parameter6_name=values.unset, parameter6_value=values.unset,
               parameter7_name=values.unset, parameter7_value=values.unset,
               parameter8_name=values.unset, parameter8_value=values.unset,
               parameter9_name=values.unset, parameter9_value=values.unset,
               parameter10_name=values.unset, parameter10_value=values.unset,
               parameter11_name=values.unset, parameter11_value=values.unset,
               parameter12_name=values.unset, parameter12_value=values.unset,
               parameter13_name=values.unset, parameter13_value=values.unset,
               parameter14_name=values.unset, parameter14_value=values.unset,
               parameter15_name=values.unset, parameter15_value=values.unset,
               parameter16_name=values.unset, parameter16_value=values.unset,
               parameter17_name=values.unset, parameter17_value=values.unset,
               parameter18_name=values.unset, parameter18_value=values.unset,
               parameter19_name=values.unset, parameter19_value=values.unset,
               parameter20_name=values.unset, parameter20_value=values.unset,
               parameter21_name=values.unset, parameter21_value=values.unset,
               parameter22_name=values.unset, parameter22_value=values.unset,
               parameter23_name=values.unset, parameter23_value=values.unset,
               parameter24_name=values.unset, parameter24_value=values.unset,
               parameter25_name=values.unset, parameter25_value=values.unset,
               parameter26_name=values.unset, parameter26_value=values.unset,
               parameter27_name=values.unset, parameter27_value=values.unset,
               parameter28_name=values.unset, parameter28_value=values.unset,
               parameter29_name=values.unset, parameter29_value=values.unset,
               parameter30_name=values.unset, parameter30_value=values.unset,
               parameter31_name=values.unset, parameter31_value=values.unset,
               parameter32_name=values.unset, parameter32_value=values.unset,
               parameter33_name=values.unset, parameter33_value=values.unset,
               parameter34_name=values.unset, parameter34_value=values.unset,
               parameter35_name=values.unset, parameter35_value=values.unset,
               parameter36_name=values.unset, parameter36_value=values.unset,
               parameter37_name=values.unset, parameter37_value=values.unset,
               parameter38_name=values.unset, parameter38_value=values.unset,
               parameter39_name=values.unset, parameter39_value=values.unset,
               parameter40_name=values.unset, parameter40_value=values.unset,
               parameter41_name=values.unset, parameter41_value=values.unset,
               parameter42_name=values.unset, parameter42_value=values.unset,
               parameter43_name=values.unset, parameter43_value=values.unset,
               parameter44_name=values.unset, parameter44_value=values.unset,
               parameter45_name=values.unset, parameter45_value=values.unset,
               parameter46_name=values.unset, parameter46_value=values.unset,
               parameter47_name=values.unset, parameter47_value=values.unset,
               parameter48_name=values.unset, parameter48_value=values.unset,
               parameter49_name=values.unset, parameter49_value=values.unset,
               parameter50_name=values.unset, parameter50_value=values.unset,
               parameter51_name=values.unset, parameter51_value=values.unset,
               parameter52_name=values.unset, parameter52_value=values.unset,
               parameter53_name=values.unset, parameter53_value=values.unset,
               parameter54_name=values.unset, parameter54_value=values.unset,
               parameter55_name=values.unset, parameter55_value=values.unset,
               parameter56_name=values.unset, parameter56_value=values.unset,
               parameter57_name=values.unset, parameter57_value=values.unset,
               parameter58_name=values.unset, parameter58_value=values.unset,
               parameter59_name=values.unset, parameter59_value=values.unset,
               parameter60_name=values.unset, parameter60_value=values.unset,
               parameter61_name=values.unset, parameter61_value=values.unset,
               parameter62_name=values.unset, parameter62_value=values.unset,
               parameter63_name=values.unset, parameter63_value=values.unset,
               parameter64_name=values.unset, parameter64_value=values.unset,
               parameter65_name=values.unset, parameter65_value=values.unset,
               parameter66_name=values.unset, parameter66_value=values.unset,
               parameter67_name=values.unset, parameter67_value=values.unset,
               parameter68_name=values.unset, parameter68_value=values.unset,
               parameter69_name=values.unset, parameter69_value=values.unset,
               parameter70_name=values.unset, parameter70_value=values.unset,
               parameter71_name=values.unset, parameter71_value=values.unset,
               parameter72_name=values.unset, parameter72_value=values.unset,
               parameter73_name=values.unset, parameter73_value=values.unset,
               parameter74_name=values.unset, parameter74_value=values.unset,
               parameter75_name=values.unset, parameter75_value=values.unset,
               parameter76_name=values.unset, parameter76_value=values.unset,
               parameter77_name=values.unset, parameter77_value=values.unset,
               parameter78_name=values.unset, parameter78_value=values.unset,
               parameter79_name=values.unset, parameter79_value=values.unset,
               parameter80_name=values.unset, parameter80_value=values.unset,
               parameter81_name=values.unset, parameter81_value=values.unset,
               parameter82_name=values.unset, parameter82_value=values.unset,
               parameter83_name=values.unset, parameter83_value=values.unset,
               parameter84_name=values.unset, parameter84_value=values.unset,
               parameter85_name=values.unset, parameter85_value=values.unset,
               parameter86_name=values.unset, parameter86_value=values.unset,
               parameter87_name=values.unset, parameter87_value=values.unset,
               parameter88_name=values.unset, parameter88_value=values.unset,
               parameter89_name=values.unset, parameter89_value=values.unset,
               parameter90_name=values.unset, parameter90_value=values.unset,
               parameter91_name=values.unset, parameter91_value=values.unset,
               parameter92_name=values.unset, parameter92_value=values.unset,
               parameter93_name=values.unset, parameter93_value=values.unset,
               parameter94_name=values.unset, parameter94_value=values.unset,
               parameter95_name=values.unset, parameter95_value=values.unset,
               parameter96_name=values.unset, parameter96_value=values.unset,
               parameter97_name=values.unset, parameter97_value=values.unset,
               parameter98_name=values.unset, parameter98_value=values.unset,
               parameter99_name=values.unset, parameter99_value=values.unset):
        """
        Create the StreamInstance

        :param unicode name: The name of this resource
        :param unicode url: Url where WebSocket connection will be established.
        :param StreamInstance.Track track: One of `inbound_track`, `outbound_track`, `both_tracks`.
        :param unicode status_callback: Absolute URL of the status callback.
        :param unicode status_callback_method: The http method for the status_callback.
        :param unicode parameter1_name: Parameter name
        :param unicode parameter1_value: Parameter value
        :param unicode parameter2_name: Parameter name
        :param unicode parameter2_value: Parameter value
        :param unicode parameter3_name: Parameter name
        :param unicode parameter3_value: Parameter value
        :param unicode parameter4_name: Parameter name
        :param unicode parameter4_value: Parameter value
        :param unicode parameter5_name: Parameter name
        :param unicode parameter5_value: Parameter value
        :param unicode parameter6_name: Parameter name
        :param unicode parameter6_value: Parameter value
        :param unicode parameter7_name: Parameter name
        :param unicode parameter7_value: Parameter value
        :param unicode parameter8_name: Parameter name
        :param unicode parameter8_value: Parameter value
        :param unicode parameter9_name: Parameter name
        :param unicode parameter9_value: Parameter value
        :param unicode parameter10_name: Parameter name
        :param unicode parameter10_value: Parameter value
        :param unicode parameter11_name: Parameter name
        :param unicode parameter11_value: Parameter value
        :param unicode parameter12_name: Parameter name
        :param unicode parameter12_value: Parameter value
        :param unicode parameter13_name: Parameter name
        :param unicode parameter13_value: Parameter value
        :param unicode parameter14_name: Parameter name
        :param unicode parameter14_value: Parameter value
        :param unicode parameter15_name: Parameter name
        :param unicode parameter15_value: Parameter value
        :param unicode parameter16_name: Parameter name
        :param unicode parameter16_value: Parameter value
        :param unicode parameter17_name: Parameter name
        :param unicode parameter17_value: Parameter value
        :param unicode parameter18_name: Parameter name
        :param unicode parameter18_value: Parameter value
        :param unicode parameter19_name: Parameter name
        :param unicode parameter19_value: Parameter value
        :param unicode parameter20_name: Parameter name
        :param unicode parameter20_value: Parameter value
        :param unicode parameter21_name: Parameter name
        :param unicode parameter21_value: Parameter value
        :param unicode parameter22_name: Parameter name
        :param unicode parameter22_value: Parameter value
        :param unicode parameter23_name: Parameter name
        :param unicode parameter23_value: Parameter value
        :param unicode parameter24_name: Parameter name
        :param unicode parameter24_value: Parameter value
        :param unicode parameter25_name: Parameter name
        :param unicode parameter25_value: Parameter value
        :param unicode parameter26_name: Parameter name
        :param unicode parameter26_value: Parameter value
        :param unicode parameter27_name: Parameter name
        :param unicode parameter27_value: Parameter value
        :param unicode parameter28_name: Parameter name
        :param unicode parameter28_value: Parameter value
        :param unicode parameter29_name: Parameter name
        :param unicode parameter29_value: Parameter value
        :param unicode parameter30_name: Parameter name
        :param unicode parameter30_value: Parameter value
        :param unicode parameter31_name: Parameter name
        :param unicode parameter31_value: Parameter value
        :param unicode parameter32_name: Parameter name
        :param unicode parameter32_value: Parameter value
        :param unicode parameter33_name: Parameter name
        :param unicode parameter33_value: Parameter value
        :param unicode parameter34_name: Parameter name
        :param unicode parameter34_value: Parameter value
        :param unicode parameter35_name: Parameter name
        :param unicode parameter35_value: Parameter value
        :param unicode parameter36_name: Parameter name
        :param unicode parameter36_value: Parameter value
        :param unicode parameter37_name: Parameter name
        :param unicode parameter37_value: Parameter value
        :param unicode parameter38_name: Parameter name
        :param unicode parameter38_value: Parameter value
        :param unicode parameter39_name: Parameter name
        :param unicode parameter39_value: Parameter value
        :param unicode parameter40_name: Parameter name
        :param unicode parameter40_value: Parameter value
        :param unicode parameter41_name: Parameter name
        :param unicode parameter41_value: Parameter value
        :param unicode parameter42_name: Parameter name
        :param unicode parameter42_value: Parameter value
        :param unicode parameter43_name: Parameter name
        :param unicode parameter43_value: Parameter value
        :param unicode parameter44_name: Parameter name
        :param unicode parameter44_value: Parameter value
        :param unicode parameter45_name: Parameter name
        :param unicode parameter45_value: Parameter value
        :param unicode parameter46_name: Parameter name
        :param unicode parameter46_value: Parameter value
        :param unicode parameter47_name: Parameter name
        :param unicode parameter47_value: Parameter value
        :param unicode parameter48_name: Parameter name
        :param unicode parameter48_value: Parameter value
        :param unicode parameter49_name: Parameter name
        :param unicode parameter49_value: Parameter value
        :param unicode parameter50_name: Parameter name
        :param unicode parameter50_value: Parameter value
        :param unicode parameter51_name: Parameter name
        :param unicode parameter51_value: Parameter value
        :param unicode parameter52_name: Parameter name
        :param unicode parameter52_value: Parameter value
        :param unicode parameter53_name: Parameter name
        :param unicode parameter53_value: Parameter value
        :param unicode parameter54_name: Parameter name
        :param unicode parameter54_value: Parameter value
        :param unicode parameter55_name: Parameter name
        :param unicode parameter55_value: Parameter value
        :param unicode parameter56_name: Parameter name
        :param unicode parameter56_value: Parameter value
        :param unicode parameter57_name: Parameter name
        :param unicode parameter57_value: Parameter value
        :param unicode parameter58_name: Parameter name
        :param unicode parameter58_value: Parameter value
        :param unicode parameter59_name: Parameter name
        :param unicode parameter59_value: Parameter value
        :param unicode parameter60_name: Parameter name
        :param unicode parameter60_value: Parameter value
        :param unicode parameter61_name: Parameter name
        :param unicode parameter61_value: Parameter value
        :param unicode parameter62_name: Parameter name
        :param unicode parameter62_value: Parameter value
        :param unicode parameter63_name: Parameter name
        :param unicode parameter63_value: Parameter value
        :param unicode parameter64_name: Parameter name
        :param unicode parameter64_value: Parameter value
        :param unicode parameter65_name: Parameter name
        :param unicode parameter65_value: Parameter value
        :param unicode parameter66_name: Parameter name
        :param unicode parameter66_value: Parameter value
        :param unicode parameter67_name: Parameter name
        :param unicode parameter67_value: Parameter value
        :param unicode parameter68_name: Parameter name
        :param unicode parameter68_value: Parameter value
        :param unicode parameter69_name: Parameter name
        :param unicode parameter69_value: Parameter value
        :param unicode parameter70_name: Parameter name
        :param unicode parameter70_value: Parameter value
        :param unicode parameter71_name: Parameter name
        :param unicode parameter71_value: Parameter value
        :param unicode parameter72_name: Parameter name
        :param unicode parameter72_value: Parameter value
        :param unicode parameter73_name: Parameter name
        :param unicode parameter73_value: Parameter value
        :param unicode parameter74_name: Parameter name
        :param unicode parameter74_value: Parameter value
        :param unicode parameter75_name: Parameter name
        :param unicode parameter75_value: Parameter value
        :param unicode parameter76_name: Parameter name
        :param unicode parameter76_value: Parameter value
        :param unicode parameter77_name: Parameter name
        :param unicode parameter77_value: Parameter value
        :param unicode parameter78_name: Parameter name
        :param unicode parameter78_value: Parameter value
        :param unicode parameter79_name: Parameter name
        :param unicode parameter79_value: Parameter value
        :param unicode parameter80_name: Parameter name
        :param unicode parameter80_value: Parameter value
        :param unicode parameter81_name: Parameter name
        :param unicode parameter81_value: Parameter value
        :param unicode parameter82_name: Parameter name
        :param unicode parameter82_value: Parameter value
        :param unicode parameter83_name: Parameter name
        :param unicode parameter83_value: Parameter value
        :param unicode parameter84_name: Parameter name
        :param unicode parameter84_value: Parameter value
        :param unicode parameter85_name: Parameter name
        :param unicode parameter85_value: Parameter value
        :param unicode parameter86_name: Parameter name
        :param unicode parameter86_value: Parameter value
        :param unicode parameter87_name: Parameter name
        :param unicode parameter87_value: Parameter value
        :param unicode parameter88_name: Parameter name
        :param unicode parameter88_value: Parameter value
        :param unicode parameter89_name: Parameter name
        :param unicode parameter89_value: Parameter value
        :param unicode parameter90_name: Parameter name
        :param unicode parameter90_value: Parameter value
        :param unicode parameter91_name: Parameter name
        :param unicode parameter91_value: Parameter value
        :param unicode parameter92_name: Parameter name
        :param unicode parameter92_value: Parameter value
        :param unicode parameter93_name: Parameter name
        :param unicode parameter93_value: Parameter value
        :param unicode parameter94_name: Parameter name
        :param unicode parameter94_value: Parameter value
        :param unicode parameter95_name: Parameter name
        :param unicode parameter95_value: Parameter value
        :param unicode parameter96_name: Parameter name
        :param unicode parameter96_value: Parameter value
        :param unicode parameter97_name: Parameter name
        :param unicode parameter97_value: Parameter value
        :param unicode parameter98_name: Parameter name
        :param unicode parameter98_value: Parameter value
        :param unicode parameter99_name: Parameter name
        :param unicode parameter99_value: Parameter value

        :returns: The created StreamInstance
        :rtype: twilio.rest.api.v2010.account.call.stream.StreamInstance
        """
        data = values.of({
            'Name': name,
            'Url': url,
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

        payload = self._version.create(method='POST', uri=self._uri, data=data, )

        return StreamInstance(
            self._version,
            payload,
            account_sid=self._solution['account_sid'],
            call_sid=self._solution['call_sid'],
        )

    def get(self, sid):
        """
        Constructs a StreamContext

        :param sid: The SID of the Stream resource, or the `name`

        :returns: twilio.rest.api.v2010.account.call.stream.StreamContext
        :rtype: twilio.rest.api.v2010.account.call.stream.StreamContext
        """
        return StreamContext(
            self._version,
            account_sid=self._solution['account_sid'],
            call_sid=self._solution['call_sid'],
            sid=sid,
        )

    def __call__(self, sid):
        """
        Constructs a StreamContext

        :param sid: The SID of the Stream resource, or the `name`

        :returns: twilio.rest.api.v2010.account.call.stream.StreamContext
        :rtype: twilio.rest.api.v2010.account.call.stream.StreamContext
        """
        return StreamContext(
            self._version,
            account_sid=self._solution['account_sid'],
            call_sid=self._solution['call_sid'],
            sid=sid,
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.StreamList>'


class StreamPage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the StreamPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API
        :param account_sid: The SID of the Account that created this resource
        :param call_sid: The SID of the Call the resource is associated with

        :returns: twilio.rest.api.v2010.account.call.stream.StreamPage
        :rtype: twilio.rest.api.v2010.account.call.stream.StreamPage
        """
        super(StreamPage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of StreamInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.api.v2010.account.call.stream.StreamInstance
        :rtype: twilio.rest.api.v2010.account.call.stream.StreamInstance
        """
        return StreamInstance(
            self._version,
            payload,
            account_sid=self._solution['account_sid'],
            call_sid=self._solution['call_sid'],
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.StreamPage>'


class StreamContext(InstanceContext):

    def __init__(self, version, account_sid, call_sid, sid):
        """
        Initialize the StreamContext

        :param Version version: Version that contains the resource
        :param account_sid: The SID of the Account that created this resource
        :param call_sid: The SID of the Call the resource is associated with
        :param sid: The SID of the Stream resource, or the `name`

        :returns: twilio.rest.api.v2010.account.call.stream.StreamContext
        :rtype: twilio.rest.api.v2010.account.call.stream.StreamContext
        """
        super(StreamContext, self).__init__(version)

        # Path Solution
        self._solution = {'account_sid': account_sid, 'call_sid': call_sid, 'sid': sid, }
        self._uri = '/Accounts/{account_sid}/Calls/{call_sid}/Streams/{sid}.json'.format(**self._solution)

    def update(self, status):
        """
        Update the StreamInstance

        :param StreamInstance.UpdateStatus status: The status. Must have the value `stopped`

        :returns: The updated StreamInstance
        :rtype: twilio.rest.api.v2010.account.call.stream.StreamInstance
        """
        data = values.of({'Status': status, })

        payload = self._version.update(method='POST', uri=self._uri, data=data, )

        return StreamInstance(
            self._version,
            payload,
            account_sid=self._solution['account_sid'],
            call_sid=self._solution['call_sid'],
            sid=self._solution['sid'],
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Api.V2010.StreamContext {}>'.format(context)


class StreamInstance(InstanceResource):

    class Track(object):
        INBOUND_TRACK = "inbound_track"
        OUTBOUND_TRACK = "outbound_track"
        BOTH_TRACKS = "both_tracks"

    class Status(object):
        IN_PROGRESS = "in-progress"
        STOPPED = "stopped"

    class UpdateStatus(object):
        STOPPED = "stopped"

    def __init__(self, version, payload, account_sid, call_sid, sid=None):
        """
        Initialize the StreamInstance

        :returns: twilio.rest.api.v2010.account.call.stream.StreamInstance
        :rtype: twilio.rest.api.v2010.account.call.stream.StreamInstance
        """
        super(StreamInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'sid': payload.get('sid'),
            'account_sid': payload.get('account_sid'),
            'call_sid': payload.get('call_sid'),
            'name': payload.get('name'),
            'status': payload.get('status'),
            'date_updated': deserialize.rfc2822_datetime(payload.get('date_updated')),
        }

        # Context
        self._context = None
        self._solution = {
            'account_sid': account_sid,
            'call_sid': call_sid,
            'sid': sid or self._properties['sid'],
        }

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context

        :returns: StreamContext for this StreamInstance
        :rtype: twilio.rest.api.v2010.account.call.stream.StreamContext
        """
        if self._context is None:
            self._context = StreamContext(
                self._version,
                account_sid=self._solution['account_sid'],
                call_sid=self._solution['call_sid'],
                sid=self._solution['sid'],
            )
        return self._context

    @property
    def sid(self):
        """
        :returns: The SID of the Stream resource.
        :rtype: unicode
        """
        return self._properties['sid']

    @property
    def account_sid(self):
        """
        :returns: The SID of the Account that created this resource
        :rtype: unicode
        """
        return self._properties['account_sid']

    @property
    def call_sid(self):
        """
        :returns: The SID of the Call the resource is associated with
        :rtype: unicode
        """
        return self._properties['call_sid']

    @property
    def name(self):
        """
        :returns: The name of this resource
        :rtype: unicode
        """
        return self._properties['name']

    @property
    def status(self):
        """
        :returns: The status - one of `stopped`, `in-progress`
        :rtype: StreamInstance.Status
        """
        return self._properties['status']

    @property
    def date_updated(self):
        """
        :returns: The RFC 2822 date and time in GMT that this resource was last updated
        :rtype: datetime
        """
        return self._properties['date_updated']

    def update(self, status):
        """
        Update the StreamInstance

        :param StreamInstance.UpdateStatus status: The status. Must have the value `stopped`

        :returns: The updated StreamInstance
        :rtype: twilio.rest.api.v2010.account.call.stream.StreamInstance
        """
        return self._proxy.update(status, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Api.V2010.StreamInstance {}>'.format(context)
