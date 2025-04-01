### Superheroes API

## Author

# Azriel Ngae

## Description

The Superheroes API is a Flask-based RESTful API designed to manage superheroes and their powers. It allows users to retrieve, create, and update heroes, powers, and hero-power relationships in a SQLite database.

## Features

# Retrieve a list of all heroes

# Retrieve a specific hero and their associated powers

# Retrieve all available powers

# Retrieve details of a specific power

# Update the description of a power

# Assign a power to a hero with a specified strength

## Technologies Used

# Python (Flask, SQLAlchemy)

# SQLite (Database)

# Flask-Migrate (Database migrations)

# Thunder Client/Postman (API testing)

## Installation

# Prerequisites

# Python 3.x installed

## Virtual environment setup (recommended)

## Steps

Clone this repository:

git clone <repo-url>
cd superheroes

Create and activate a virtual environment:

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

Install dependencies:

pip install -r requirements.txt

Initialize and migrate the database:

flask db init
flask db migrate -m "Initial migration"
flask db upgrade

Seed the database with sample data:

python seed.py

Run the application:

flask run

API Endpoints

Base URL:

http://127.0.0.1:5000/

Heroes

GET /heroes - Retrieve all heroes

GET /heroes/:id - Retrieve a specific hero with their powers

Powers

GET /powers - Retrieve all available powers

GET /powers/:id - Retrieve details of a specific power

PATCH /powers/:id - Update a power's description

Request Body:

{
  "description": "Updated Power Description"
}

Hero Powers

POST /hero_powers - Assign a power to a hero

Request Body:

{
  "hero_id": 1,
  "power_id": 2,
  "strength": "Strong"
}

Testing the API

Use Thunder Client or Postman to test the endpoints. Ensure Content-Type: application/json is set for requests requiring a body.

#License

This project is open-source and free to use.

