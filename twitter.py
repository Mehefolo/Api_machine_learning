import tweepy
from tweepy import OAuthHandler
import pandas as pd

"""I like to have my python script print a message at the beginning. This helps me confirm whether everything is set up correctly. And it's nice to get an uplifting message ;)."""

print("You got this!")

consumer_key=""
consumer_secret=""
access_token=""
access_token_secret=""

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

tweets = []

count = 1

"""Twitter will automatically sample the last 7 days of data. Depending on how many total tweets there are with the specific hashtag, keyword, handle, or key phrase that you are looking for, you can set the date back further by adding since= as one of the parameters. You can also manually add in the number of tweets you want to get back in the items() section."""

for tweet in tweepy.Cursor(api.search, q="@SG_CotedIvoire", count=450, since='2020-02-28').items(50000):
	
	print(count)
	count += 1

	try: 
		data = [tweet.created_at, tweet.id, tweet.text, tweet.user._json['screen_name'], tweet.user._json['name'], tweet.user._json['created_at'], tweet.entities['urls']]
		data = tuple(data)
		tweets.append(data)

	except tweepy.TweepError as e:
		print(e.reason)
		continue

	except StopIteration:
		break

df = pd.DataFrame(tweets, columns = ['created_at','tweet_id', 'tweet_text', 'screen_name', 'name', 'account_creation_date', 'urls'])

"""Add the path to the folder you want to save the CSV file in as well as what you want the CSV file to be named inside the single quotations"""
df.to_csv(path_or_buf = 'FileName.csv', index=False) 

print ("API NAME IS: ", api.me().name)
api.update_status("Using Tweepy from the command line")

timeline = api.user_timeline(screen_name=user, include_rts=True, count=100)
for tweet in timeline:
    print ("ID:", tweet.id)
    print ("User ID:", tweet.user.id)
    print ("Text:", tweet.text)
    print ("Created:", tweet.created_at)
    print ("Geo:", tweet.geo)
    print ("Contributors:", tweet.contributors)
    print ("Coordinates:", tweet.coordinates) 
    print ("Favorited:", tweet.favorited)
    print ("In reply to screen name:", tweet.in_reply_to_screen_name)
    print ("In reply to status ID:", tweet.in_reply_to_status_id)
    print ("In reply to status ID str:", tweet.in_reply_to_status_id_str)
    print ("In reply to user ID:", tweet.in_reply_to_user_id)
    print ("In reply to user ID str:", tweet.in_reply_to_user_id_str)
    print ("Place:", tweet.place)
    print ("Retweeted:", tweet.retweeted)
    print ("Retweet count:", tweet.retweet_count)
    print ("Source:", tweet.source)
    print ("Truncated:", tweet.truncated)