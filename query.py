import twitter
from credentials import consumer_key, consumer_secret, access_token_key, access_token_secret

api = twitter.Api(consumer_key=consumer_key,
                  consumer_secret=consumer_secret,
                  access_token_key=access_token_key,
                  access_token_secret=access_token_secret)

# results = api.GetSearch(
#     raw_query="q=webdev&src=typd")

results = api.PostUpdate('test')

print results
