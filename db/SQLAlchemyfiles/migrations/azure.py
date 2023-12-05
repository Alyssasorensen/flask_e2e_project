"""

pip install sqlalchemy alembic mysql-connector-python pymysql

"""

## Part 1 - Define SQLAlchemy models for patients and their medical records:
### this file below could always be called db_schema.py or something similar

from sqlalchemy import create_engine, inspect, Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
import os
from dotenv import load_dotenv

# load_dotenv()

DB_HOST = os.getenv("DB_HOST")

Base = declarative_base()

# Define models

class health_statistics(Base):
    __tablename__ = 'health_statistics'

    id = Column(Integer, primary_key=True)
    year = Column(String(4), nullable=False)
    male = Column(String(4), nullable=False)
    female = Column(String(4), nullable=False)

records = relationship('additional_health_statistics', back_populates='health_statistics')

class additional_health_statistics(Base):
    __tablename__ = 'additional_health_statistics'

    id = Column(Integer, primary_key=True)
    year = Column(String(4), nullable=False)
    male = Column(String(4), nullable=False)
    female = Column(String(4), nullable=False)

records = relationship('location_health_statistics', back_populates='additional_health_statistics')

class location_health_statistics(Base):
    __tablename__ = 'location_health_statistics'
    id = Column(Integer, primary_key=True)
    year = Column(Integer(10), nullable=False)
    male = Column(Integer(10), nullable=False)
    female = Column(Integer(10), nullable=False)

records = relationship('health_statistics', back_populates='location_health_statistics')


### Part 2 - initial sqlalchemy-engine to connect to db:

engine = create_engine("mysql+pymysql://alyssaflask3:Admin-2023-1@alyssa-final-app.mysql.database.azure.com/webapp",
                         connect_args={'ssl': {'ssl-mode': 'preferred'}},
                         )


DATABASE_URL = "mysql+mysqlconnector://alyssaflask3:Admin-2023-1@alyssa-final-app.mysql.database.azure.com/webapp"
engine = create_engine(DB_HOST)

## Test connection

inspector = inspect(engine)
inspector.get_table_names()


### Part 3 - create the tables using sqlalchemy models, with no raw SQL required:

Base.metadata.create_all(engine)

### Running migrations 
""" these steps are then performed in the termainl, outside of your python code

1. alembic init migrations
` alembic init migrations `

2. edit alembic.ini to point to your database
` sqlalchemy.url = mysql+mysqlconnector://username:password@host/database_name `

3. edit env.py to point to your models
`from db_schema import Base`
`target_metadata = Base.metadata `

4. create a migration
` alembic revision --autogenerate -m "create tables" `

5. run the migration
` alembic upgrade head `

in addition, you can run ` alembic history ` to see the history of migrations
or you can run with the --sql flag to see the raw SQL that will be executed

so it could be like:
` alembic upgrade head --sql `

or if you then want to save it:
` alembic upgrade head --sql > migration.sql `

6. check the database

7. roll back: To roll back a migration in Alembic, you can use the downgrade command. 
The downgrade command allows you to revert the database schema to a previous 
migration version. Here's how you can use it:

`alembic downgrade <target_revision>` 

or if you want to roll back to the previous version, you can use the -1 flag:
`alembic downgrade -1`
 

"""