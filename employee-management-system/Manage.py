from flask import Flask, request, jsonify
import mysql.connector


app = Flask(__name__)
db = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="root",
    database="assistants"
)
cursor = db.cursor()

# create_table_query = """
# CREATE TABLE IF NOT EXISTS assistant (
#     id INT AUTO_INCREMENT PRIMARY KEY,
#     name VARCHAR(255),
#     mobile VARCHAR(20),
#     email VARCHAR(255),
#     salary DECIMAL(10, 2),
#     city VARCHAR(100),
#     country VARCHAR(100),
#     department VARCHAR(100),
#     role VARCHAR(100)
# )
# """
# cursor.execute(create_table_query)

#create an assistant
@app.route('/assistant', methods=['POST'])
def create_assistant():
    data = request.json
    name = data['name']
    mobile = data['mobile']
    email = data['email']
    salary = data['salary']
    city = data['city']
    country = data['country']
    department = data['department']
    role = data['role']
    insert_query = """
    INSERT INTO assistant (name, mobile, email, salary, city, country, department, role)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """
    cursor.execute(insert_query, (name, mobile, email, salary, city, country, department, role))
    db.commit()

    return jsonify({'id': cursor.lastrowid}), 201

#find by ID
@app.route('/assistant/<int:assistant_id>', methods=['GET'])
def get_assistant(assistant_id):
    query = "SELECT * FROM assistant WHERE id = %s"
    cursor.execute(query, (assistant_id,))
    assistant = cursor.fetchone()

    if assistant:
        assistant_details = {
            'id': assistant[0],
            'name': assistant[1],
            'mobile': assistant[2],
            'email': assistant[3],
            'salary': float(assistant[4]),
            'city': assistant[5],
            'country': assistant[6],
            'department': assistant[7],
            'role': assistant[8]
        }
        return jsonify(assistant_details)
    else:
        return jsonify({'message': 'Assistant not found'}), 404
    
#find by name
@app.route('/assistant/<string:assistant_name>', methods=['GET'])
def get_assistant_by_name(assistant_name):
    query = "SELECT * FROM assistant WHERE name = %s"
    cursor.execute(query, (assistant_name,))
    assistant = cursor.fetchone()

    if assistant:
        assistant_details = {
            'id': assistant[0],
            'name': assistant[1],
            'mobile': assistant[2],
            'email': assistant[3],
            'salary': float(assistant[4]),
            'city': assistant[5],
            'country': assistant[6],
            'department': assistant[7],
            'role': assistant[8]
        }
        return jsonify(assistant_details)
    else:
        return jsonify({'message': 'Assistant not found'}), 404

#update the assistants data
@app.route('/assistant/<int:assistant_id>', methods=['PUT'])
def update_assistant(assistant_id):
    data = request.json
    name = data['name']
    mobile = data['mobile']
    email = data['email']
    salary = data['salary']
    city = data['city']
    country = data['country']
    department = data['department']
    role = data['role']

    update_query = """
    UPDATE assistant
    SET name=%s, mobile=%s, email=%s, salary=%s, city=%s, country=%s, department=%s, role=%s
    WHERE id=%s
    """
    cursor.execute(update_query, (name, mobile, email, salary, city, country, department, role, assistant_id))
    db.commit()

    return jsonify({'message': 'Assistant updated successfully'})

#delete assistants data
@app.route('/assistant/<int:assistant_id>', methods=['DELETE'])
def delete_assistant(assistant_id):
    delete_query = "DELETE FROM assistant WHERE id = %s"
    cursor.execute(delete_query, (assistant_id,))
    db.commit()

    return jsonify({'message': 'Assistant deleted successfully'})


if __name__ == '__main__':
    app.run(debug=True)
