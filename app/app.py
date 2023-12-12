from flask import Flask, render_template, request, redirect, url_for, jsonify, session
import pandas as pd
import csv
from sqlalchemy import create_engine, inspect, text
from pandas import read_sql
import os
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from authlib.integrations.flask_client import OAuth
from authlib.common.security import generate_token
from oauth.db_functions import update_or_create_user
from flask_session import Session
import sentry_sdk

app = Flask(__name__)

DB_HOST = os.getenv("DB_HOST")
DB_DATABASE = os.getenv("DB_DATABASE")
DB_USERNAME = os.getenv("DB_USERNAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")
DB_PORT = int(os.getenv("DB_PORT", "3306"))
DB_CHARSET = os.getenv("DB_CHARSET", "utf8mb4")

sentry_sdk.init(
    dsn="https://29d775fba6696385edf06b5eb70c6bee@o4506300835692547.ingest.sentry.io/4506380652183552",
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    traces_sample_rate=1.0,
    # Set profiles_sample_rate to 1.0 to profile 100%
    # of sampled transactions.
    # We recommend adjusting this value in production.
    profiles_sample_rate=1.0,
)

load_dotenv()

GOOGLE_CLIENT_ID = os.getenv('GOOGLE_CLIENT_ID')
GOOGLE_CLIENT_SECRET = os.getenv('GOOGLE_CLIENT_SECRET')

print(GOOGLE_CLIENT_ID)
print(GOOGLE_CLIENT_SECRET)

app = Flask(__name__)

app.secret_key = 's547efrhkls'
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)
oauth = OAuth(app)

@app.route('/')
def index():
    return render_template('pages/index.html')

@app.route('/google/')
def google():
    CONF_URL = 'https://accounts.google.com/.well-known/openid-configuration'
    oauth.register(
        name='google',
        client_id=GOOGLE_CLIENT_ID,
        client_secret=GOOGLE_CLIENT_SECRET,
        server_metadata_url=CONF_URL,
        client_kwargs={
            'scope': 'openid email profile'
        }
    )

    # Redirect to google_auth function
    ## note, if running locally on a non-google shell, do not need to override redirect_uri
    ## use url_for 
    redirect_uri = url_for('google_auth', _external=True)
    print('REDIRECT URL: ', redirect_uri)
    session['nonce'] = generate_token()
    ## note: if running in google shell, need to override redirect_uri 
    ## to the external web address of the shell, e.g.,
    redirect_uri = 'https://5000-cs-750560197970-default.cs-us-east1-vpcf.cloudshell.dev/google/auth/'
    return oauth.google.authorize_redirect(redirect_uri, nonce=session['nonce'])

# redirect_uri = 'https://e2ealyssa.azurewebsites.net/google/auth/'

@app.route('/google/auth/')
def google_auth():
    token = oauth.google.authorize_access_token()
    user = oauth.google.parse_id_token(token, nonce=session['nonce'])
    session['user'] = user
    update_or_create_user(user)
    print(" Google User ", user)
    return redirect('/dashboard')

@app.route('/dashboard/')
def dashboard():
    user = session.get('user')
    if user:
        return render_template('pages/dashboard.html', user=user)
    else:
        return redirect('/')

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect('/')

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

## create a route that throws an error
@app.route('/error')
def error():
    raise Exception('This is a test error for Sentry Testing')

## create a db connection error 
@app.route('/db-error')
def db_error():
    conn = create_engine(f'mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}')
    try:
        conn.connect()
    except Exception as e:
        raise Exception(f'Error connecting to the database: {e}')

@app.route('/api/data', methods=['GET'])
def api_data():
    additional_data = [
        {"Year": 2019, "Male": 8.4, "Female": 13.7},
        {"Year": 2020, "Male": 8.1, "Female": 14.1},
        {"Year": 2021, "Male": 8.4, "Female": 14.1},
        {"Year": 2022, "Male": 9.7, "Female": 15.5},
    ]

    data = {"message": "Hello, welcome to the Women's Health App! Here is some example data from the web app. The data represents the percentage of regularly having feelings of worry, nervousness, or anxiety for adults aged 18 and over, United States, 2019-2022", "data": additional_data}

    return jsonify(data)

# if __name__ == '__main__':
#     app.run(port=5001, debug=True)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

# if __name__ == '__main__':
#     app.run(
#         debug=True, 
#         port=5000
#     )

