'''
    Complete end of Chapter 13 - Exercises 13.1-13.5
    **With all of the changes to Twitter, the API's are not working correctly so what I am looking for is for you to simulate what the code would be.  
    I realize you cannot test for these assignments but use the knowledge from the book to write the code as that is all we can do at this point.
'''
import tweepy
import keys
auth = tweepy.OAuthHandler(keys.consumer_key, keys.consumer_secret)
auth.set_access_token(keys.access_token, keys.access_token_secret)

# Creating an API object
api = tweepy.API(auth, wait_on_rate_limit = True, wait_on_rate_limit_notify = True)

# 13-1 (Percentage of English Tweets) Twitter is truly an international social network. Use the Twitter search API to look at 10,00 tweets.
# Look at each tweet's lang property. Count and display the number of tweets in each language.
tweets = api.search(q="*", count=10000)
lang_count = dict()

for tweet in tweets:
  if tweet.lang not in lang_count.keys():
    lang_count[tweet.lang] = 1
  else:
    lang_count[tweet.lang] += 1

total_tweets = len(tweets)
english_count = lang_count.get("en", 0)  # Handle potential absence of "en" key

# Calculate percentage of English tweets
english_percentage = (english_count / total_tweets) * 100

print("Number of tweets in each language:")
for lang in lang_count.keys():
  print(f"{lang}: {lang_count[lang]}")
print(f"\nPercentage of English tweets: {english_percentage:.2f}%")

# 13-2 ( Percentage of Retweet) Look at 10,000 tweets and determine the percentage of tweets that begin wit Twitter's reserved word RT
retweet_count = 0
for tweet in tweets:
  if tweet.text.lower().startswith("rt"):
    retweet_count += 1

# Calculate percentage of retweets
retweet_percentage = (retweet_count / total_tweets) * 100
print(f"Percentage of retweets: {retweet_percentage:.2f}%")

# 13-3 (Percentage of Extended Tweets) Look at 10,000 tweets and determine the percentage of them are extended tweets
extended_tweet_count = 0

for tweet in tweets:
  # Check if the tweet has a 'truncated' flag set to True (indicating truncation)
  if tweet.truncated:
    extended_tweet_count += 1
total_tweets = len(tweets)
extended_tweet_percentage = (extended_tweet_count / total_tweets) * 100
print(f"Percentage of extended tweets (possibly truncated): {extended_tweet_percentage:.2f}%")

# 13-4 (Basic Account Information) Get the ID, name, screen name, and description of a Twitter ccount of interest to you
lolla =  api.get_user("lollapalooza")

print(f"@lollaapalooza id: {lolla.id}")
print(f"@lollaapalooza name: {lolla.name}")
print(f"@lollaapalooza screen name: {lolla.screen_name}")
print(f"@lollaapalooza description: {lolla.description}")

# 13-5 (User timeline) Get the past 10 tweets from an account of interest to you.

lolla_tweets = api.user_timeline(screen_name = "lollapalooza", counts = 10)
for tweet in lolla_tweets:
    print(f"{tweet.user.screen_name}: {tweet.text}\n")