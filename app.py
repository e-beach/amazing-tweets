import os
from flask import Flask, send_file
from query import update_list
app = Flask(__name__)

@app.route("/")
def hello():
    return send_file("index.html")

@app.route("/<path:path>")
def update_content(path):
	update_list(path)
	return path


if __name__ == "__main__":
	# Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(port=port)
