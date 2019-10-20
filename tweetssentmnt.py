import tweepy
from textblob import TextBlob

consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#type your keyword u want to check by erasing 'kanchanjangha'
public_tweets = api.search('kanchanjangha')

for tweet in public_tweets:
    print(tweet.text)
    u=tweet.text
    u=u.encode('unicode-escape').decode('utf-8')

    
    #Step 4 Perform Sentiment Analysis on Tweets
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
    if analysis.sentiment[0]>0:

        print ('Positive')
    elif analysis.sentiment[0]<0:

            print ('Negative')
    else:

            print ('Neutral')   
        
    

