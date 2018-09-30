This project is a simple GUI which will fetch data from Cricbuzz website and display it in GUI. 
You can select the match whose details you want to see. Just select the match from the List of Live Matches and then click GET SCORE AND UPDATE button.

As you click this button, Live Feed for the match will be displayed on the GUI Panel and details for any match delayed or abondoned due to rain is also displayed 
at bottom .

You can use thi GUI when you are not allowed to Log in to Cricbuzz App or Cricbuzz Website or any other source. Or if you want the Feed sent to your Mobile Phone after every n minutes.
 
Enclosed with this file...
1.Code for GUI.
2.Sample code for Sending Feed to your mobile phone via SMS.
3.Other relevant files and pictures. 

For Sending Feed via SMS , you need to Sign up at website : https://www.twilio.com/
After creating account, you will get account_sid , auth_token and registered mobile number (Used in code).
Then you can use the code to send any message to any valid number . (Make sure these online messaging services are available for those subscribers who have not subscribed for DND facility).

Software & their Version:
1. Python 3.6 (Anaconda Distribution - Spyder IDE)
2. PyQt5
3. pycricbuzz Library
4. twilio Library

Libraries can be easily installed by: pip install <package_name>

Updated:  Now Messaging is integrated with the GUI.
Before sending Message,
1. Verify the recipient number on twilio.com
2. Add proper prefix like +91 for INDIA