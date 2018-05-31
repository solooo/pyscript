# -*- coding: utf-8 -*-

from flask import Flask, jsonify
from flask import request


app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    t = {
        'a': 1,
        'b': 2,
        'c': [3, 4, 5]
    }
    return jsonify(t)


@app.route('/signin', methods=['GET'])
def signin_form():
    return '''
        <form action="/signin" method="post">
          <p><input name="username"></p>
          <p><input name="password" type="password"></p>
          <p><button type="submit">Sign In</button></p>
        </form>
    '''


@app.route('/signin', methods=['POST'])
def signin():
    if request.form['username'] == 'admin' and request.form['password']=='admin':
        return '<h3>Hello, admin</h3>'
    return '<h3>Bad username or password</h3>'

if __name__ == '__main__':
    app.run(port=8000)
