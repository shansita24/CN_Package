from flask import Flask, render_template, request, jsonify
import mysql.connector

app = Flask(__name__)

# Set up MySQL connection
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="cn"
)

@app.route('/', methods=['GET'])
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    try:
        username = request.form.get('username')
        password = request.form.get('password')

        cursor = connection.cursor()

        query = 'SELECT COUNT(*) FROM accounts WHERE username = %s AND password = %s'
        cursor.execute(query, (username, password))
        count = cursor.fetchone()[0]

        if count == 1:
            return jsonify({'message': 'Login successful'}), 200
        else:
            return jsonify({'message': 'Invalid username or password'}), 401
    except Exception as e:
        return jsonify({'message': 'An error occurred'}), 500
    finally:
        cursor.close()

if __name__ == '__main__':
    app.run(debug=True)
