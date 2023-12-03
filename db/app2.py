from flask import Flask, render_template
from sqlalchemy import create_engine
from pandas import read_sql
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, inspect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configure SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'  # Update with your database URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define models
class health_statistics(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.Integer)
    male = db.Column(db.Float)
    female = db.Column(db.Float)

class additional_health_statistics(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.Integer)
    male = db.Column(db.Float)
    female = db.Column(db.Float)

class location_health_statistics(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.Integer)
    male = db.Column(db.Float)
    female = db.Column(db.Float)

load_dotenv()  # Load environment variables from .env file

# Database connection settings from environment variables
DB_HOST = os.getenv("DB_HOST")
DB_DATABASE = os.getenv("DB_DATABASE")
DB_USERNAME = os.getenv("DB_USERNAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_PORT = int(os.getenv("DB_PORT", "3306"))
DB_CHARSET = os.getenv("DB_CHARSET", "utf8mb4")

# Connection string
conn_string = (
    f"mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_DATABASE}"
    "?charset=utf8mb4"
)

# Database connection settings
db_engine = create_engine(conn_string, echo=False)

@app.route('/')
def data():
    # Fetch data from health_statistics table
    sql_query_health_statistics = "SELECT * FROM health_statistics"
    df_health_statistics = read_sql(sql_query_health_statistics, db_engine)
    data_health_statistics = df_health_statistics.to_dict(orient='records')

    # Fetch data from additional_health_statistics table
    sql_query_additional_health_statistics = "SELECT * FROM additional_health_statistics"
    df_additional_health_statistics = read_sql(sql_query_additional_health_statistics, db_engine)
    data_additional_health_statistics = df_additional_health_statistics.to_dict(orient='records')

    # Fetch data from location_health_statistics table
    sql_query_location_health_statistics = "SELECT * FROM location_health_statistics"
    df_location_health_statistics = read_sql(sql_query_location_health_statistics, db_engine)
    data_location_health_statistics = df_location_health_statistics.to_dict(orient='records')

    return render_template('data.html', data_health_statistics=data_health_statistics, data_additional_health_statistics=data_additional_health_statistics, data_location_health_statistics=data_location_health_statistics)

if __name__ == '__main__':
    app.run(port=5001, debug=True)
