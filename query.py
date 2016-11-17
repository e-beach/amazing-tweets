from pprint import pprint
import twitter
import urllib
from credentials import consumer_key, consumer_secret, access_key, access_secret

auth = twitter.OAuth(access_key, access_secret, consumer_key, consumer_secret)
api= twitter.Twitter(auth = auth)


LIST_NAME = 'content'
SCREEN_NAME = 'newsstreamapp'

def get_user_ids(topic):
	topic = urllib.quote_plus(topic)
	results = api.users.search(q = topic)
	IDs = [ user["id_str"] for user in results ]
	return ','.join(IDs)

def create_list():
	result = api.lists.create(name=LIST_NAME)

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

def update_list(topic):
	try:
		api.lists.destroy(slug=LIST_NAME, owner_screen_name=SCREEN_NAME)
	except twitter.TwitterHTTPError:
		# The list did not exist.
		pass
	create_list()
	def try_to_add():
		try:
			add_users(get_user_ids(topic))
		except twitter.TwitterHTTPError:
			# Why? We don't know.
			sleep(1)
			try_to_add()
	try_to_add()


if __name__ == "__main__":
	update_list("heavy-metal")


# https://dev.twitter.com/rest/reference/post/lists/create 	
#add_users(get_user_ids('webdev'))

	


