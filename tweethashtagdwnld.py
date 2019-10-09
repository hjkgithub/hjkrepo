import tweepy
from tweepy import StreamListener

consumer_key =''
consumer_secret = ''
access_token = ''
access_token_secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

#api = tweepy.API(auth)

#verifier = raw_input('Verifier:')



#api = tweepy.API(auth)
#api.update_status('tweepy + oauth!')

#auth = tweepy.OAuthHandler("consumer_key", "consumer_secret")

# Redirect user to Twitter to authorize
#redirect_user(auth.get_authorization_url())

# Get access token
#auth.get_access_token("verifier_value")

# Construct the API instance
#api = tweepy.API(auth)


import csv
import pandas as pd
####input your credentials here
#consumer_key = ''
#consumer_secret = ''
#access_token = ''
#access_token_secret = ''

#auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
#auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)
#####United Airlines
# Open/Create a file to append data
csvFile = open('ua.csv', 'a')
#Use csv Writer
csvWriter = csv.writer(csvFile)

#for tweet in tweepy.Cursor(api.search,q="#unitedAIRLINES",count=100,
for tweet in tweepy.Cursor(api.search,q="#kanchanjangha",count=1000,
                           lang="en",
                           since="2017-01-03").items():
    print (tweet.created_at, tweet.text)
    #csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])
