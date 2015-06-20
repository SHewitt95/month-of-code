from flask import Flask
from flask import render_template
from flask.ext.bower import Bower

app = Flask(__name__)
Bower(app)

@app.route("/")
def index():
	return render_template('index.html')

if __name__ == "__main__":
    app.run(
        host = "0.0.0.0",
		port=8000,
		use_reloader=True,
		debug=True,
    )
