import os
from flask import Flask, send_file
app = Flask(__name__)

@app.route("/")
def hello():
    return send_file("index.html")

if __name__ == "__main__":
	# Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(port=port)
