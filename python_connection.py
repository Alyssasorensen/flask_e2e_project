import os
from dotenv import load_dotenv
from pandas import read_sql
from sqlalchemy import create_engine, inspect

load_dotenv()  # Load environment variables from .env file

# Database connection settings from environment variables
DB_HOST = os.getenv("DB_HOST")
DB_DATABASE = os.getenv("DB_DATABASE")
DB_USERNAME = os.getenv("DB_USERNAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_PORT = int(os.getenv("DB_PORT", 3306))
DB_CHARSET = os.getenv("DB_CHARSET", "utf8mb4")

# SSL Configuration (No need to redefine SSL_CA, SSL_CERT, SSL_KEY here)
# The SSL_CA, SSL_CERT, and SSL_KEY variables should be set in your .env file.

# Ensure that SSL_CA, SSL_CERT, and SSL_KEY are set in the environment
if not (os.getenv('SSL_CA') and os.getenv('SSL_CERT') and os.getenv('SSL_KEY')):
    raise ValueError("SSL_CA, SSL_CERT, and SSL_KEY environment variables are not set.")

# Connection string with SSL (note the use of a dictionary for SSL configuration)
conn_string = (
    f"mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_DATABASE}"
    f"?charset={DB_CHARSET}&"
    f"ssl={{'ca': '{os.getenv('SSL_CA')}', 'cert': '{os.getenv('SSL_CERT')}', 'key': '{os.getenv('SSL_KEY')}'}}"
)

# Create a database engine
db_engine = create_engine(conn_string, echo=False)

def get_tables(engine):
    """Get list of tables."""
    inspector = inspect(engine)
    return inspector.get_table_names()

def execute_query_to_dataframe(query: str, engine):
    """Execute SQL query and return result as a DataFrame."""
    return read_sql(query, engine)

# Example usage
tables = get_tables(db_engine)
print("Tables in the database:", tables)

sql_query = "SELECT * FROM percentage of fair or poor health status for adults aged 18 and over, United States, 2019—2022"
df = execute_query_to_dataframe(sql_query, db_engine)
print(df)