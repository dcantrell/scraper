#!/usr/bin/env python3
import os
import twitter
import json
import twython
#consumerKey = os.getenv('consumerkey')
#consumerSecret = os.getenv('consumersecret')
#oauthToken = os.getenv('accesstoken')
#oauthTokenSecret = os.getenv('accesstokensecret')


consumerKey = "mykey"
consumerSecret = "mysecret"
oauthToken = "mytoken"
oauthTokenSecret = "mysecretoken"
auth = twitter.OAuth(oauthToken, oauthTokenSecret, consumerKey, consumerSecret)
twtr = twitter.Twitter(auth=auth)

query = 'slpguru'
limit = 10
results = twtr.search.tweets(q=query, count=limit)
python_datastruct = json.loads(results)

#tweet_json = twtr.search.tweets
#python_datastruct = json.loads(tweet_json)

print (results)



#print(consumerkey,consumersecret,accesstoken,accesstokensecret)

