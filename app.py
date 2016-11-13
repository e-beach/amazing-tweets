import os
from pprint import pprint
from flask import Flask, send_file, request, redirect, url_for
from query import update_list
app = Flask(__name__)

@app.route("/")
def hello():
	print "GET"
	return send_file("index.html")

@app.route("/search", methods=['POST'] )
def update_content():
	print "POST /search"
	pprint(request)
	topic = request.form['topic']
	update_list(topic)
	return redirect(url_for(hello))


if __name__ == "__main__":
	# Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(port=port)
