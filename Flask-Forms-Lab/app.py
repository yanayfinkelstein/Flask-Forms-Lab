from flask import Flask, jsonify, request, render_template, redirect, url_for
import random


app = Flask(  # Create a flask app
	__name__,
	template_folder='templates',  # Name of html file folder
	static_folder='static'  # Name of directory for static files
)


username = "yanay"
password = "123"
facebook_friends=["Loai","Yonathan","Adan", "George", "Fouad", "Celina"]

@app.route('/', methods=['GET', 'POST'])
def home():
	if request.method == 'POST':
		name1 = request.form['username']
		password1 = request.form['password']
		if password == password1 and username == name1:
			return render_template('home.html', name = name1, password= password, new_friends=facebook_friends)
		else:
			return render_template('login.html')
	else:
		return render_template('login.html')

@app.route('/home')
def sdfb():
	return render_template('home.html', new_friends= facebook_friends)
@app.route('/friend_exists/<string:friend>', methods=['GET','POST'])
def friend(friend):
	if friend in facebook_friends:
		friend_is_friend = True
	else:
		friend_is_friend=False
	return render_template('friend_exists.html', friend=friend, friend_name=friend_is_friend)
		


if __name__ == "__main__":  # Makes sure this is the main process
	app.run( # Starts the site
		debug=True
	)