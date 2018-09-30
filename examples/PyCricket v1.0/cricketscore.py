# -*- coding: utf-8 -*-
"""
Created on Sun Jun  4 15:59:29 2017

@author: LALIT ARORA
"""

from pycricbuzz import Cricbuzz
from twilio.rest import Client
c = Cricbuzz() 
matches = c.matches()
message=""
livematches=[]

# printing live matches at that time
for match in matches:
    if(match['mchstate']=='inprogress'):
        livematches.append(match['mchdesc'])
print("Live Matches :")       
for i in range(len(livematches)):
    print(livematches[i])        
      
# Get your country match by this search 

for match in matches:
    if('IND ' in match['mchdesc']):
        print(match['id'])

#Get the feed for your team     
print()   
finalscorecard=""
for match in matches:
    if 'IND vs PAK' in match['mchdesc']:
        identity=match['id']
        finalscorecard=finalscorecard+str(match['srs'])
        finalscorecard=finalscorecard+"\n"+str(match['mchdesc'])
        finalscorecard=finalscorecard+"\n"+str(match['type'])+str(match['mnum'])
        finalscorecard=finalscorecard+"\n"+str(match['status'])
        finalscorecard=finalscorecard+"\n"+str(match['mchstate'])
        scorecard=c.scorecard(identity)
        seperator="-------------------------------------------------------------------------------"
        finalscorecard=finalscorecard+"\n"+seperator
        finalscorecard=finalscorecard+"\n"+"BATTING TEAM :"+str(scorecard['scorecard'][0]['batteam'])
        for i in range(len(scorecard['scorecard'][0]['batcard'])):
            temp=""
            temp=str(scorecard['scorecard'][0]['batcard'][i]['name'])+" "+str(scorecard['scorecard'][0]['batcard'][i]['runs'])+"of"+str(scorecard['scorecard'][0]['batcard'][i]['balls'])+",  Fours :"+str(scorecard['scorecard'][0]['batcard'][i]['fours'])+", Sixes :"+str(scorecard['scorecard'][0]['batcard'][i]['six'])+", Dismissal :"+str(scorecard['scorecard'][0]['batcard'][i]['dismissal'])
            finalscorecard=finalscorecard+"\n"+temp
            
        finalscorecard=finalscorecard+"\n"+"Score :"+str(scorecard['scorecard'][0]['runs'])+"/"+str(scorecard['scorecard'][0]['wickets'])
        finalscorecard=finalscorecard+"\n"+"Runrate :"+str(scorecard['scorecard'][0]['runrate'])
        finalscorecard=finalscorecard+"\n"+seperator
        finalscorecard=finalscorecard+"\n"+"BOWLING TEAM :"+str(scorecard['scorecard'][0]['bowlteam'])
        for i in range(len(scorecard['scorecard'][0]['bowlcard'])):
            temp=""
            temp=str(scorecard['scorecard'][0]['bowlcard'][i]['name'])+"Overs :"+str(scorecard['scorecard'][0]['bowlcard'][i]['overs'])+", Runs :"+str(scorecard['scorecard'][0]['bowlcard'][i]['runs'])+", Wickets :"+str(scorecard['scorecard'][0]['bowlcard'][i]['wickets'])
            finalscorecard=finalscorecard+"\n"+temp

print(finalscorecard)
print(seperator)
# Listing Matches affected by Rain
print("Matches affected by Rain: ")

for match in matches:
    if(match['mchstate']=='rain'):
        print(match['mchdesc'])

# Sending match details through SMS to a vernumber from regnumber
# Go through READ ME file first
# vernumber must start with a proper prefix like +91 for INDIA
 
message=finalscorecard
account_sid = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
auth_token = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
client = Client(account_sid, auth_token)
if message!="":
    msg = client.api.account.messages.create(to="vernumber",
                                             from_="regnumber",
                                             body=message)
else:
    msg=client.api.account.messages.create(to="vernumber",
                                             from_="regnumber",
                                             body="No live Match")
    
