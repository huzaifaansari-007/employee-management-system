# employee-management-system
Employee Management System using Flask and MySQL
This project is a simple employee management system built with Flask, a Python web framework, and MySQL as the database. It allows users to perform basic CRUD (Create, Read, Update, Delete) operations on employee records.

Prerequisites
Before running this application, ensure that you have the following installed on your system:

Python (preferably version 3.x)
Flask
MySQL
MySQL Connector for Python
Installation
Follow these steps to set up and run the project:

Clone the repository:

bash
Copy code
git clone https://github.com/your_username/employee-management-system.git
Navigate to the project directory:

bash
Copy code
cd employee-management-system
Install the necessary dependencies:

bash
Copy code
pip install -r requirements.txt
Setting up MySQL:
Install MySQL on your system if it is not already installed.
Create a database named employees.
Make sure the MySQL server is running.
Update MySQL connection details:
Open the app.py file.
Update the host, user, password, and database fields in the database connection section.
Usage
To run the Flask application:

bash
Copy code
python app.py
Open your web browser and go to http://localhost:5000.

Available Operations:
Create a new employee record: Send a POST request to /employee.
Retrieve an employee by ID: Send a GET request to /employee/<id>.
Retrieve an employee by name: Send a GET request to /employee/name/<name>.
Update an existing employee: Send a PUT request to /employee/<id>.
Delete an employee: Send a DELETE request to /employee/<id>.
API Endpoints
POST /employee: Add a new employee.
GET /employee/<id>: Retrieve an employee by their ID.
GET /employee/name/<name>: Retrieve an employee by their name.
PUT /employee/<id>: Update an existing employee's details.
DELETE /employee/<id>: Remove an employee from the system.
Database Schema
The following schema is used for the employees table:

sql
CREATE TABLE IF NOT EXISTS employee (
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
Contributing
Contributions are highly encouraged! If you encounter any issues or have suggestions for new features, feel free to open an issue or submit a pull request.

