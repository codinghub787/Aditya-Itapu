from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from datetime import datetime

app = Flask(__name__)

# Connect to the SQLite database
conn = sqlite3.connect('data.db', check_same_thread=False)
c = conn.cursor()

# Create a table if it doesn't exist
c.execute('''CREATE TABLE IF NOT EXISTS data
             (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, email TEXT, age INTEGER, dob TEXT, phone TEXT)''')

# Route for the index page
@app.route('/')
def index():
    return render_template('index.html')

# Route for adding data
@app.route('/add', methods=['POST'])
def add():
    name = request.form['name']
    email = request.form['email']
    age = request.form['age']
    dob = request.form['dob']
    phone = request.form['phone']

    # Validate the data
    if not name or not email or not age or not dob or not phone:
        return 'Please fill in all fields'

    # Insert the data into the database
    c.execute("INSERT INTO data (name, email, age, dob, phone) VALUES (?, ?, ?, ?, ?)", (name, email, age, dob, phone))
    conn.commit()

    return redirect(url_for('data'))

# Route for displaying data
@app.route('/data')
def data():
    c.execute("SELECT * FROM data")
    rows = c.fetchall()
    return render_template('data.html', rows=rows)

if __name__ == '__main__':
    app.run(debug=True)