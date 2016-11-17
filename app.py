import os
from pprint import pprint
from flask import Flask, render_template, request, redirect, url_for
from forms import RegistrationForm
from query import update_list
app = Flask(__name__)

@app.route("/", methods=['POST', 'GET'])
def hello():
	form = RegistrationForm(request.form)
	if request.method == 'POST' and form.validate():
		topic = form.topic.data
 		update_list(topic)
	return render_template("index.html", form=form)

if __name__ == "__main__":
	# Bind to PORT if defined, otherwise default to 5000.
	port = int(os.environ.get('PORT', 5000))
	app.run(port=port)
