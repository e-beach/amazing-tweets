from pprint import pprint
import twitter
from credentials import consumer_key, consumer_secret, access_key, access_secret

api= twitter.Twitter(
		        auth = twitter.OAuth(access_key, access_secret, consumer_key, consumer_secret))

def get_users(topic_str):
	results = api.users.search(q = topic_str)
	IDs = [ user["id"] for user in results ]
	return IDs
