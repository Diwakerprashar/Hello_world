from flask import *

app = Flask(__name__)

@app.route('/')
def default():
	return render_template('login.html')

@app.route('/login',methods=['POST','GET'])
def login():
	username = request.form['username']
	password = request.form['password']

	if uname == 'radha' and password == 'krishna':
		return render_template('page2.html')

	if uname == 'radha' and password != 'krishna':
		message = 'Incorrect password'
		return render_template('login.html',msg = message)

	if uname != 'radha' and password == 'krishna':
		message = 'Incorrect Username'
		return render_template('login.html',msg = message)
	else:
		message = 'Invalid Credentials'
		return render_template('login.html',msg = message)

if __name__ == "__main__":
	app.run(debug=True)
