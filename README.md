# Simple Flask RESTful API

This repository contains a basic RESTful API built using the Flask framework in Python. The API offers essential CRUD (Create, Read, Update, Delete) operations for managing users. It serves as a foundation for building more complex APIs with Flask and is ideal for developers looking to get started with web development in Python.

# Key Features

- GET /users: Fetches all user records.
- GET /users/{id}: Retrieves the details of a user by their unique ID.
- POST /users: Allows you to create a new user by sending data in JSON format.
- PUT /users/{id}: Updates an existing user record.
- DELETE /users/{id}: Removes a user by their ID.

 # Requirements
 
Before running this API, make sure you have Python installed on your machine.

1. Clone the Repository
Start by cloning the repository to your local machine:

```bash
git clone https://github.com/yourusername/simple-flask-api.git
cd simple-flask-api
```

2. Install Dependencies
Create a virtual environment and install the necessary Python libraries, particularly Flask:

```bash
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate     # On Windows

pip install Flask
```

3. Run the Application
Once everything is set up, run the Flask development server:

```bash
python app.py
```

Your API will be available at http://127.0.0.1:5000/.

# API Endpoints
1. GET /users
This endpoint retrieves a list of all users.

- Example Request:
```bash
GET http://127.0.0.1:5000/users
```
- Example Response:
```json
{
  "users": [
    {
      "id": 1,
      "name": "Alice",
      "email": "alice@example.com"
    },
    {
      "id": 2,
      "name": "Bob",
      "email": "bob@example.com"
    }
  ]
}
```

2. GET /users/{id}
Fetch a specific user by their unique ID.

- Example Request:
```bash
GET http://127.0.0.1:5000/users/1
```
-Example Response:
```json
{
  "user": {
    "id": 1,
    "name": "Alice",
    "email": "alice@example.com"
  }
}
```
3. POST /users
Create a new user by sending a JSON object containing the user’s name and email.

- Example Request:
```bash
POST http://127.0.0.1:5000/users
Content-Type: application/json
{
  "name": "Charlie",
  "email": "charlie@example.com"
}
```

- Example Response:
```json
{
  "message": "User created successfully",
  "user": {
    "id": 3,
    "name": "Charlie",
    "email": "charlie@example.com"
  }
}
```
4. PUT /users/{id}
Update an existing user's details by their ID.

- Example Request:
```bash
PUT http://127.0.0.1:5000/users/1
Content-Type: application/json
{
  "name": "Alice Cooper",
  "email": "alice.cooper@example.com"
}
```

- Example Response:
```json
{
  "message": "User updated successfully",
  "user": {
    "id": 1,
    "name": "Alice Cooper",
    "email": "alice.cooper@example.com"
  }
}
```
5. DELETE /users/{id}
Delete a user from the system by their ID.

- Example Request:
```bash
DELETE http://127.0.0.1:5000/users/1
```
- Example Response:
```json
{
  "message": "User deleted successfully"
}
```

# Testing the API
You can interact with the API using tools like Postman or curl.

# Examples with curl:
- Get all users:

```bash
curl http://127.0.0.1:5000/users
```
- Get a user by ID:
```bash
curl http://127.0.0.1:5000/users/1
```

- Create a new user:
```bash
curl -X POST -H "Content-Type: application/json" -d '{"name": "Charlie", "email": "charlie@example.com"}' http://127.0.0.1:5000/users
```

- Update an existing user:
```bash
curl -X PUT -H "Content-Type: application/json" -d '{"name": "Alice Cooper", "email": "alice.cooper@example.com"}' http://127.0.0.1:5000/users/1
```

- Delete a user:
```bash
curl -X DELETE http://127.0.0.1:5000/users/1
```
