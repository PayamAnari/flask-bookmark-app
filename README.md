<h1 align="center">
  <img
    width="400"
    alt="flask"
    src="https://live.staticflickr.com/65535/53577307136_7b04645dc8_z.jpg">
</h1>

---

<h3 align="center">
  <strong>
      🗂️ Flask Bookmark REST API 🗂️

  </strong>
</h3>

---

<p align="center">
  <img 
    width="1000"
    alt="home"
    src="https://live.staticflickr.com/65535/53577313611_7b9d34fe01_z.jpg"/>
</p>

---

## Flask Bookmark REST API
### Description

This Flask application provides a RESTful API for managing bookmarks. It allows users to register, login, create, edit, and delete bookmarks, as well as retrieve statistics on their bookmarked URLs. Short URLs are automatically generated for each bookmark to provide easy access.

---

## Features

- **User Authentication:** Users can register and login securely using their email and password. Passwords are hashed for security.
- **Bookmark Management:** Users can create, edit, delete, and view their bookmarks. Each bookmark includes details such as URL, description, creation date, and number of visits.
- **Short URL Generation:** Short URLs are automatically generated for each bookmark to provide easy access.
- **Swagger Documentation:** API endpoints are documented using Swagger UI, making it easy to understand and use the API.
- **Pagination Support:** The API supports pagination for endpoints that return multiple items, allowing users to navigate through large sets of data with ease.

<p align="center">
  <img 
    width="600"
    alt="home"
    src="https://live.staticflickr.com/65535/53577777000_96737e39e6_z.jpg"/>
</p>


---

## Technologies Used

- **Flask:** A lightweight Python web framework used for building the REST API.
- **Flask JWT Extended:** Provides JSON Web Token (JWT) support for user authentication.
- **SQLAlchemy:** Object-relational mapping (ORM) library for interacting with the database.
- **Flasgger:** Integrates Swagger UI for API documentation.
- **Werkzeug:** Provides utilities for password hashing and verification.
- **Validators:** Library used for URL and email validation.


  <p align="left">
  <img src="https://img.shields.io/badge/flask-00008B?style=for-the-badge&logo=flask&logoColor=white"/>
  <img src="https://img.shields.io/badge/jwt-acace6?style=for-the-badge&logo=JWT&logoColor=white"/>
  <img src="https://img.shields.io/badge/sqlalchemy-0000FF?style=for-the-badge&logo=sqlalchemy&logoColor=white"/>
  <img src="https://img.shields.io/badge/Swagger-85EA2D?style=for-the-badge&logo=Swagger&logoColor=white"/>
  <img src="https://img.shields.io/badge/werkzeug-ffa500?style=for-the-badge&logo=werkzeug&logoColor=white"/>
  <img src="https://img.shields.io/badge/validators-FF0000?style=for-the-badge&logo=validators&logoColor=white"/>
 
</p>

---

## API Endpoints
### Authentication

| METHOD | ROUTE | FUNCTIONALITY |ACCESS| REQUIRMENTS |
| ------- | ----- | ------------- | ------------- | ------------ |
| *POST* | ```/api/v1/auth/register/``` | _Register New User_| _All users_| - |
| *POST* | ```/api/v1/auth/login/``` | _Login User_| _All users_| - |
| *GET* | ```/api/v1/auth/me/``` | _Get User Details_| _All users_| Authentication |
| *PUT* | ```/api/v1/auth/<user_id>/``` | _Update User Details_| _All users_|  Authentication |
| *DELETE* | ```/api/v1/auth/<user_id>/``` | _Delete User_| _All users_|  Authentication |
| *POST* | ```/api/v1/auth/token/refresh/``` | _Refresh User's Token_| _All users_|  Authentication |

### Bookmarks

| METHOD | ROUTE | FUNCTIONALITY |ACCESS| REQUIRMENTS |
| ------- | ----- | ------------- | ------------- | ------------ |
| *POST* | ```/api/v1/bookmarks/``` | _Create Bookmark_| _All users_| Authentication |
| *GET* | ```/api/v1/bookmarks/``` | _Get All Bookmarks_| _All users_| Authentication |
| *GET* | ```/api/v1/bookmarks/<bookmark_id>/``` | _Get Bookmark By Id_| _All users_| Authentication |
| *PUT* | ```/api/v1/bookmarks/<bookmark_id>``` | _Edit Bookmark_| _All users_| Authentication |
| *DELETE* | ```/api/v1/bookmarks/<bookmark_id>``` | _Delete Bookmark_| _All users_| Authentication |
| *GET* | ```/api/v1/bookmarks/stats/``` | _Get Bookmark Statistics_| _All users_| Authentication |
| *GET* | ```/api/v1/<short_url>/``` | _Redirect to a Short URL_| _All users_| - |


---

## Installation

1- **Clone the repository:**
```
git clone https://github.com/your-username/flask-bookmark-api.git

```
2- **Create your virtualenv and activate it:**
```
Pipenv or virtualenv

```
3- **Install dependencies:**
```
pip install -r requirements.txt

```
4- **Set environment variables for configuration** (e.g., SECRET_KEY, SQLALCHEMY_DB_URI, JWT_SECRET_KEY).

5- **Run the application:**
```
flask run
```

---

## Example Requests
### - User Login
### Request:

```
{
  "email": "john@example.com",
  "password": "password123"
}

```
### Response (Successful login):
```
{
  "message": "User logged in successfully",
  "user": {
    "refresh": "<refresh_token>",
    "access": "<access_token>",
    "username": "john_doe",
    "email": "john@example.com"
  }
}

```
### - Create Bookmark
### Request
```
{
  "url": "https://www.example.com",
  "body": "This is an example bookmark"
}

```
### Response (Successful creation):

```
{
  "data": {
    "id": 1,
    "url": "https://www.example.com",
    "short_url": "qW6",
    "visit": 0,
    "body": "This is an example bookmark",
    "created_at": "2024-03-09T12:00:00Z",
    "updated_at": "2024-03-09T12:00:00Z"
  },
  "message": "Bookmark created successfully"
}

```
### - Get all Bookmarks
### Parameters:
```
page (optional): Page number to retrieve (default is 1).
per_page (optional): Number of bookmarks per page (default is 5).
```

### Response:

```
{
  "data": [
    {
      "id": 1,
      "url": "https://www.example.com",
      "short_url": "qW6",
      "visit": 0,
      "body": "This is an example bookmark",
      "created_at": "2024-03-09T12:00:00Z",
      "updated_at": "2024-03-09T12:00:00Z"
    },
    {
      "id": 2,
      "url": "https://www.anotherexample.com",
      "short_url": "aB7",
      "visit": 0,
      "body": "This is another example bookmark",
      "created_at": "2024-03-10T12:00:00Z",
      "updated_at": "2024-03-10T12:00:00Z"
    }
  ],
  "meta": {
    "page": 1,
    "pages": 2,
    "total_count": 10,
    "prev_page": null,
    "next_page": 2,
    "has_next": true,
    "has_prev": false
  }
}

```
---

## License
This project is licensed under the [MIT License](LICENSE).

---
### Built with ❤️ by Payam Anari

Thank you for exploring the Gym Fitness app! If you have any questions, feedback, or just want to say hi, feel free to [reach out](mailto:anari.p62@gmail.com). Happy fitness journey!

---
