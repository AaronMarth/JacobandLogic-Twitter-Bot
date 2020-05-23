import tweepy
import LogicLyrics
import JakePictures



consumer_key = 'dcBWTGQzvMugMiSA48afqlgOs'
consumer_secret = 'BXmRtdAxOgoqj7C8gm3qKzdybrD0d2HJAJymLg2YHsljnwXmBV'
access_token = '1263513331236835330-y3nmxJESTLtoffyjt39DPg4JsH6qNB'
access_token_secret= 't6MsBSPZLAXZMzNg3kkDLtuO9cil6NWH4irU36eF7j3vu'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

path = JakePictures.randomNumber()
api = tweepy.API(auth)

public_tweets = api.home_timeline()

media = api.media_upload(path)
tweet = LogicLyrics.randomNumber()
api.update_status(status=tweet, media_ids=[media.media_id])