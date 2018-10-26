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

def make_public_task(task):
	new_task = {}
	for field in task:
		if field == 'id':
			new_task['uri'] = url_for('get_task', task_id=task['id'], _external=True)
		else:
			new_task[field] = task[field]
	return new_task

@app.route('/Equiv/api/v1.0/tasks', methods=['GET'])
@auth.login_required
def get_tasks():
	return jsonify({'tasks': [make_public_task(task) for task in tasks]})
	
@app.errorhandler(404)
def not_found(error):
	return make_response(jsonify({'error':'Not found'}), 404)

#curl -i -H "Content-Type: application/json" -X POST -d '{DATS for search results}' http://localhost:5000/Equiv/api/v1.0/tasks
@app.route('/Equiv/api/v1.0/tasks', methods=['POST'])
def input_DATS():
	if not request.json or not 'title' in request.json:
		abort(400)
	x = <send to service.py>
	return x, 201

@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
	task = [task for task in tasks if task['id'] == task_id]
	if len(task) == 0:
		abort(404)
	tasks.remove(task[0])
	return jsonify({'result': True})

if __name__ == '__main__':
	app.run(debug=True)