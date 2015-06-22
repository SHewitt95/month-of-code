from flask import Flask
from flask import render_template
from flask.ext.bower import Bower

app = Flask(__name__)
Bower(app)

@app.route("/")
def index():
	return render_template('index.html')

@app.route("/oreo_popcorn")
def oreo_popcorn():
	return render_template('oreo_popcorn.html')

@app.route("/wall_of_color")
def wall_of_color():
	return render_template('wall_of_color.html')

if __name__ == "__main__":
    app.run(
        host = "0.0.0.0",
		port=8000,
		use_reloader=True,
		debug=True,
    )
