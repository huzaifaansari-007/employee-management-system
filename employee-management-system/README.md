# Assistant Management System using Flask and MySQL

This project is a simple assistant management system built with Flask, a Python web framework, and MySQL for the database. It allows you to perform basic CRUD (Create, Read, Update, Delete) operations on assistant records.

## Prerequisites

Before running this application, make sure you have the following installed:

- Python (3.x recommended)
- Flask
- MySQL
- MySQL Connector for Python

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your_username/assistant-management-system.git
Navigate to the project directory:
cd assistant-management-system
Install dependencies:
pip install -r requirements.txt

 ## Set up MySQL:
Install MySQL on your system if not already installed.
Create a database named assistants.
Make sure MySQL server is running.
Modify MySQL connection details:
Open app.py file.
Update the host, user, password, and database fields in the db connection.

 ## Usage
Run the Flask application:
>python app.py
Open your web browser and navigate to http://localhost:5000.

 ## You can perform the following operations:
Create a new assistant by sending a POST request to /assistant.
Retrieve an assistant by ID or name with GET requests to /assistant/<id> or /assistant/<name>.
Update an existing assistant by sending a PUT request to /assistant/<id>.
Delete an assistant by sending a DELETE request to /assistant/<id>.

 ## Endpoints
POST /assistant: Create a new assistant.
GET /assistant/<id>: Retrieve an assistant by ID.
GET /assistant/<name>: Retrieve an assistant by name.
PUT /assistant/<id>: Update an existing assistant.
DELETE /assistant/<id>: Delete an assistant.

 ## Database Schema
The application uses the following database schema:

 ## sql
CREATE TABLE IF NOT EXISTS assistant (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    mobile VARCHAR(20),
    email VARCHAR(255),
    salary DECIMAL(10, 2),
    city VARCHAR(100),
    country VARCHAR(100),
    department VARCHAR(100),
    role VARCHAR(100)
);
 ## Contributing
Contributions are welcome! If you find any issues or want to add new features, feel free to open an issue or submit a pull request.
