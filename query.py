from pprint import pprint
import twitter
from credentials import consumer_key, consumer_secret, access_key, access_secret

auth = twitter.OAuth(access_key, access_secret, consumer_key, consumer_secret)
api= twitter.Twitter(auth = auth)


LIST_NAME = 'abc'
SCREEN_NAME = 'newsstreamapp'

def get_users(topic):
	results = api.users.search(q = topic)
	IDs = [ user["id_str"] for user in results ]
	return IDs

def content_stream(topic):
	stream = twitter.TwitterStream(auth = auth, secure = True)
	ids = ','.join(get_users(topic))
	tweet_iter = stream.statuses.filter(follow = ids)
	for tweet in tweet_iter:
		pprint(tweet)

def create_list():
	name= LIST_NAME # WIP
	result = api.lists.create(name=name)
	pprint(result)

def add_users(users):
	api.lists.members.create_all(
		slug=LIST_NAME,
		owner_screen_name=SCREEN_NAME,
		user_id=users
	)

def post_something():
	new_status = "testing testing"
	results = api.statuses.update(status = new_status)
	print "updated status: %s" % new_status




# https://dev.twitter.com/rest/reference/post/lists/create 	

add_users(','.join(get_users('webdev')))

	


