# Task Management System API
This is a simple task management system API built with Django and Django REST Framework. It provides endpoints for managing tasks and labels.

## Features
Create, retrieve, update, and delete tasks
Create, retrieve, update, and delete labels
Assign labels to tasks
User authentication and authorization
Custom filters for tasks and labels
### Requirements
- Python 3.7+
- Django 4.2+
- Django REST Framework
## Setup Instructions
Follow these steps to set up and run the project locally:
1. Clone the repository:

` git clone https://github.com/your-username/task-management-system.git  `

2. Navigate to the project directory:

`cd task-management-system`

3. Create and activate a virtual environment:

```
python -m venv env
source env/bin/activate  # For Linux/Mac
env\Scripts\activate  # For Windows
```
4. Install the project dependencies:

`pip install -r requirements.txt`

5. Apply database migrations:

`python manage.py migrate`

6. Create a superuser account:

`python manage.py createsuperuser`

Follow the prompts to enter a username, email, and password for the superuser account.

7. Start the development server:

`python manage.py runserver`

The API will be accessible at `http://localhost:8000/`.

API Endpoints
The following API endpoints are available:

- `POST /api/auth/login/` - Obtain an authentication token by providing valid credentials.
- `POST /api/tasks/` - Create a new task.
- `GET /api/tasks/` - List all tasks.
- `GET /api/tasks/{id}/` - Retrieve a specific task by ID.
- `PUT /api/tasks/{id}/` - Update a specific task by ID.
- `DELETE /api/tasks/{id}/` - Delete a specific task by ID.
- `POST /api/labels/` - Create a new label.
- `GET /api/labels/` - List all labels.
- `GET /api/labels/{id}/` - Retrieve a specific label by ID.
- `PUT /api/labels/{id}/` - Update a specific label by ID.
- `DELETE /api/labels/{id}/` - Delete a specific label by ID.

## Testing the API
To test the API endpoints, you can use tools like cURL or Postman. Here are some example requests:
1. Obtain an authentication token:
`curl -X POST -H "Content-Type: application/json" -d '{"username": "your-username", "password": "your-password"}' http://localhost:8000/api/auth/login/`
Replace `your-username` and `your-password` with your actual credentials.
2. Create a new task:
`curl -X POST -H "Content-Type: application/json" -H "Authorization: Token <your-token>" -d '{"title": "New Task", "description": "Task description"}' http://localhost:8000/api/tasks/`
Replace `your-token` with the authentication token obtained in step 1.
3. List all tasks:
`curl -H "Authorization: Token <your-token>" http://localhost:8000/api/tasks/`
4. Update a task:
`curl -X PUT -H "Content-Type: application/json" -H "Authorization: Token <your-token>" -d '{"title": "Updated Task", "completed": true}' http://localhost:8000/api/tasks/{id}/`
Replace `{id}` with the actual ID of the task you want to update.
5. Delete a task:
`curl -X DELETE -H "Authorization: Token <your-token>" http://localhost:8000/api/tasks/{id}/`
Replace `{id}` with the actual ID of the task you want to delete.
You can follow similar patterns for testing the label endpoints.

## Running Tests
To run the tests for the API, use the following command:
`python manage.py test`
This will execute the test cases defined in the tests.py file and provide the test results.

## Additional Notes
- The API uses token-based authentication. Make sure to include the authentication token in the Authorization header when making requests to protected endpoints.
- You can customize the API behavior by modifying the views, serializers, and models in the respective files.



