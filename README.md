# Django REST Framework Project

This repository provides a comprehensive guide and implementation for building RESTful APIs using Django and Django REST Framework. It covers both basic and intermediate-level concepts, making it a valuable resource for developers looking to deepen their understanding of Django REST Framework.

## Features

- Detailed explanations and implementations of RESTful API endpoints
- User authentication and authorization
- CRUD operations for various models
- Serialization and deserialization of data
- Custom permissions, throttling, pagination
- Postman file for api testing
- Example code and tutorials for common use cases

## Requirements

- Python 3.x
- Django 3.x or later
- Django REST Framework 3.x or later

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/SUGOGOi/django_rest_basic
   cd django_rest_basic
   
2. Create a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
3. Install the dependencies:
    ```bash
    pip install -r requirements.txt

4.  Apply makemigrations and migrations, If needed:
    ```bash
    python3 manage.py makemigrations
    python3 manage.py migrate
5. Superuser details:
   - username : sumsum
   - password : qwe123
   
6. Run the development server:

   ```bash
   python3 manage.py runserver

## Usage
- Check http://127.0.0.1:8000 
- Interact with the API endpoints using tools like Postman
- Use the Django admin interface at http://127.0.0.1:8000/admin/ to manage data




