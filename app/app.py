from flask import Flask, render_template, request, redirect, url_for, jsonify
import pandas as pd
import csv
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('base.html', data=data)

@app.route('/about')
def about():
    return render_template('pages/about.html', data=data)

@app.route('/reproductive')
def reproductive():
    return render_template('pages/reproductive.html', data=data)

@app.route('/mental')
def mental():
    return render_template('pages/mental.html', data=data)

@app.route('/fitness')
def fitness():
    return render_template('pages/fitness.html', data=data)

# Define your specific values
first_data = [
    {"Year": 2019, "Male": 14.9, "Female": 15.6},
    {"Year": 2020, "Male": 13.2, "Female": 14.4},
    {"Year": 2021, "Male": 13.2, "Female": 13.9},
    {"Year": 2022, "Male": 13.8, "Female": 15.2},
]

# Define your specific values
additional_data = [
    {"Year": 2019, "Male": 8.4, "Female": 13.7},
    {"Year": 2020, "Male": 8.1, "Female": 14.1},
    {"Year": 2021, "Male": 8.4, "Female": 14.1},
    {"Year": 2022, "Male": 9.7, "Female": 15.5},
]

# Load data from CSV file
df = pd.read_csv('https://raw.githubusercontent.com/Alyssasorensen/flask_e2e_project/main/data/raw_data%20_new1.csv')

@app.route('/data')
def data():
    # Sample data from the CSV file
    sampled_data = df.sample(15).to_dict(orient='records')
    print(sampled_data)  # Add this line to print the sampled_data
    return render_template('pages/data.html', first_data=first_data, additional_data=additional_data, sampled_data=sampled_data)

@app.route('/contact')
def contact():
    return render_template('pages/contact.html')

@app.route('/submit_contact', methods=['POST'])
def submit_contact():
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')

    # Process the form data (e.g., send an email, store in a database)

    # Redirect to a thank-you page or the contact page
    return redirect(url_for('thank_you'))

@app.route('/thank_you')
def thank_you():
    return render_template('pages/thank_you.html', data=data)

@app.route('/api/data', methods=['GET'])
def api_data():
    data = {"message": "Hello, welcome to the Women's Health App!"}
    return jsonify(data)

if __name__ == '__main__':
    app.run(port=5001, debug=True)
