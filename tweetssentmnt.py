import tweepy
from textblob import TextBlob

consumer_key = 'ngIjCNjFYfP2c2u4QPPlnAIUS'
consumer_secret = '5miw3aqECo7JZPVnKpQh7sXojsIaBECRh66e9jARRAMDkyDHgX'
access_token = '752613576-XDwZGux7mjvBLDsSrTQ8ZRp8nEGjBHW0J2Y2Bmba'
access_token_secret = 'PFhDycZcCIbHGBgXXH5PAWCezWutTz6WkSS6SHhifULqt'

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
        
    

