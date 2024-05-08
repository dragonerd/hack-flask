from flask import Flask, jsonify, request
from flask_cors import CORS
 
app = Flask(__name__)
CORS(app)

#################################### H-1 ########################################  OK
@app.route('/users', methods=['GET'])
def methodget():
    response = {'payload': 'success'}
    return jsonify(response)

#################################### H-2 ########################################  OK
@app.route('/user', methods=['POST'])
def methodpost():
    response = {'payload': 'success'}
    return jsonify(response)

#################################### H-3 ########################################  OK
@app.route("/user", methods=['DELETE'])
def methoddelete():
    response = {'payload': 'success'}
    return jsonify(response)

#################################### H-4 ########################################  ok
@app.route("/user", methods=['PUT'])
def methodput():
  if request.method == "PUT":
      return jsonify({'payload': 'success', 'error': False}), 200
  else:
      return jsonify({'error': 'It valid this'}), 400
  
#################################### H-5 ########################################  OK
@app.route('/api/v1/users', methods=['GET'])
def methodgetv1():
    response = {'payload': []}
    return jsonify(response)

#################################### H-6 ######################################## ok
url = "http://localhost:5000/api/v1/user?email=foo@foo.foo&name=fooziman"

@app.route('/api/v1/user', methods=['POST'])
def create_user():
    email = request.args.get('email')
    name = request.args.get('name')
    user_data = {'payload': {'email': email, 'name': name}}
    
    return jsonify(user_data)


#################################### H-7 ########################################
@app.route('/api/v1/user/add', methods=['POST'])
def add():
    email = request.form.get('email')
    name = request.form.get('name')
    id = request.form.get('id')
    user_data = {'payload': {'email': email, 'name': name, 'id': id}}
    
    return jsonify(user_data)
 
 #################################### H-8 ########################################
 
@app.route('/api/v1/user/create', methods=['POST'])
def create():
    try:
        data = request.get_json(force=True)
        user_data = {'payload': data}
        return jsonify(user_data)
    except Exception as e:
        return f"Error", 400
 