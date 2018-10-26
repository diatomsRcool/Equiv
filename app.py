#!flask/bin/python
from flask import Flask, jsonify
from flask import abort
from flask import make_response
from flask import request
from flask import url_for
import service
from flask_httpauth import HTTPBasicAuth
auth = HTTPBasicAuth()

app = Flask(__name__)

@auth.get_password
def get_password(username):
	if username == 'anke':
		return 'python'
	return None

@auth.error_handler
def unauthorized():
	return make_response(jsonify({'error':'Unauthorized access'}), 403)

DATS = {}

#curl -u anke:python -i -H "Content-Type: application/json" -X POST -d '{DATS for search results}' http://localhost:5000/Equiv/api/v1.0/tasks
@app.route('/Equiv/api/v1.0/dset', methods=['POST'])
@auth.login_required
def input_DATS():
	if not request.json or not 'title' in request.json:
		abort(400)
	r,z = service.transform(DATS)
	x = get_equiv(r,z)
	return x, 201

if __name__ == '__main__':
	app.run(debug=True)