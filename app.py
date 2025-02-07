from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data to simulate a user database
users = [
    {'id': 1, 'name': 'Alice', 'email': 'alice@example.com'},
    {'id': 2, 'name': 'Bob', 'email': 'bob@example.com'}
]

# GET endpoint: Fetch all users
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify({'users': users})

# GET endpoint: Fetch a specific user by ID
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = next((user for user in users if user['id'] == user_id), None)
    if user:
        return jsonify({'user': user})
    else:
        return jsonify({'message': 'User not found'}), 404

# POST endpoint: Create a new user
@app.route('/users', methods=['POST'])
def create_user():
    new_user = request.get_json()
    if 'name' in new_user and 'email' in new_user:
        user_id = len(users) + 1
        new_user['id'] = user_id
        users.append(new_user)
        return jsonify({'message': 'User created successfully', 'user': new_user}), 201
    else:
        return jsonify({'message': 'Invalid data'}), 400

# PUT endpoint: Update an existing user by ID
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = next((user for user in users if user['id'] == user_id), None)
    if user:
        data = request.get_json()
        user['name'] = data.get('name', user['name'])
        user['email'] = data.get('email', user['email'])
        return jsonify({'message': 'User updated successfully', 'user': user})
    else:
        return jsonify({'message': 'User not found'}), 404

# DELETE endpoint: Delete a user by ID
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = next((user for user in users if user['id'] == user_id), None)
    if user:
        users.remove(user)
        return jsonify({'message': 'User deleted successfully'})
    else:
        return jsonify({'message': 'User not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
