# To-Do API

## Description

This is a To-Do API project developed using Django and PostgreSQL. The project includes features for user authentication, task management, and logging of requests.

## Features

- User registration and management
- Task creation, retrieval, update, and deletion
- Logging of API requests

## Future Improvements

### Enhancements
- **Testing**: Implement unit and integration tests to ensure the reliability of the application. The goal is to achieve at least **80% test coverage** for all critical components of the project. This will help catch bugs early and improve the overall quality of the code.

### Features to Consider
- **User Profiles**: Expand user functionality by allowing users to manage their profiles.
- **Task Reminders**: Implement a reminder feature for tasks based on due dates.
- **Search Functionality**: Add search capabilities to filter tasks by various criteria.
- **Front-End Integration**: Consider integrating a front-end framework for a more interactive user experience.

## Technologies Used

- Django
- PostgreSQL
- Docker
- Docker Compose

## Setup Instructions

1. **Clone the repository**:
```shell
  git clone https://github.com/Dogober/to-do-API.git
  cd to-do-API
```

2. **Create a virtual environment**:
```shell
  python -m venv venv
  source venv/bin/activate  # On Windows use venv\Scripts\activate
```

3. **Install requirements**:
```shell
  pip install -r requirements.txt
```

### Prerequisites

- Python 3.12 or later
- Docker
- Docker Compose

### Environment Variables

Create a `.env` file in the root directory with the following content:

```plaintext
# DB
POSTGRES_DB=<db_name>
POSTGRES_DB_PORT=<db_port>
POSTGRES_USER=<db_user>
POSTGRES_PASSWORD=<db_password>
POSTGRES_HOST=<db_host>

# Django
SECRET_KEY=<secret_key>
```

### Running the Application

1. **Start Docker containers**

   Run the following command to start your application and PostgreSQL:

```shell
    docker-compose up --build
```

2. **Apply Migrations**

   Once the containers are running, apply migrations with:

```shell
    python manage.py migrate
```

3. **Access the API**

   The API will be available at `http://127.0.0.1:8000/api/`.
    ## API Endpoints

### User Endpoints
- **Registration**
  - **POST** `/api/user/register/`
  - Registers a new user.

- **Token Management**
  - **POST** `/api/user/token/`
  - Obtains a JWT token for authentication.
  
  - **POST** `/api/user/token/refresh/`
  - Refreshes the JWT token.

  - **POST** `/api/user/token/verify/`
  - Verifies the JWT token.

- **Manage User**
  - **GET** `/api/user/me/`
  - Retrieves the current user's details.
  
  - **PUT** `/api/user/me/`
  - Updates the current user's details.

### To-Do Endpoints
- **To-Dos**
  - **GET** `/api/todos/`
  - Retrieves a list of to-do tasks for the authenticated user. Supports filtering by query parameters, such as `status` and `due_date`.

  - **POST** `/api/todos/`
  - Creates a new to-do task for the authenticated user.

  - **GET** `/api/todos/<id>/`
  - Retrieves details of a specific to-do task by ID.

  - **PUT** `/api/todos/<id>/`
  - Updates a specific to-do task by ID.

  - **DELETE** `/api/todos/<id>/`
  - Deletes a specific to-do task by ID.
