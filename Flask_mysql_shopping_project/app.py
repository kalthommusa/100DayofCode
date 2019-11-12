from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/menwatches')
def menwatches():
	return render_template('menwatches.html')

@app.route('/womenwatches')
def womenwatches():
	return render_template('womenwatches.html')

@app.route('/contactus')
def contactus():
	return render_template('contactus.html')

if __name__ == '__main__':
	app.run(debug=True)