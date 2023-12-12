import logging
from flask import Flask, render_template
from dotenv import load_dotenv
from sqlalchemy import create_engine
import sentry_sdk
import os

load_dotenv('/home/alyssa_sorensen/flask_e2e_project/.env')

DB_HOST = os.getenv("DB_HOST")
DB_DATABASE = os.getenv("DB_DATABASE")
DB_USERNAME = os.getenv("DB_USERNAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")
DB_PORT = int(os.getenv("DB_PORT", "3306"))
DB_CHARSET = os.getenv("DB_CHARSET", "utf8mb4")

print(f'DB_HOST: {DB_HOST}, DB_DATABASE: {DB_DATABASE}, DB_USERNAME: {DB_USERNAME}, DB_PASSWORD: {DB_PASSWORD}, DB_NAME: {DB_NAME}, DB_PORT: {DB_PORT}, DB_CHARSET: {DB_CHARSET}')

sentry_sdk.init(
    dsn="https://f74c704ba3c87b4800946c82134d8feb@o4506300835692547.ingest.sentry.io/4506380509708288",
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    traces_sample_rate=1.0,
    # Set profiles_sample_rate to 1.0 to profile 100%
    # of sampled transactions.
    # We recommend adjusting this value in production.
    profiles_sample_rate=1.0,
)

app = Flask(__name__)

# Configure the logger
logging.basicConfig(filename='app.log', level=logging.INFO)  # Log to a file

@app.route('/')
def home():
    # Log a message when the home route is accessed
    logging.info('Home route accessed')
    return render_template('base.html')

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
        logging.error(f'Error connecting to the database: {e}')
        sentry_sdk.capture_exception(e)
        return render_template('db_error.html', error_message=str(e)), 500

if __name__ == '__main__':
    app.run(port=5002, debug=True)