"""

pip install sqlalchemy alembic mysql-connector-python pymysql

"""

## Part 1 - Define SQLAlchemy models for patients and their medical records:
### this file below could always be called db_schema.py or something similar

from sqlalchemy import create_engine, inspect, Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy.ext.declarative import declarative_base
import os
from dotenv import load_dotenv
from sqlalchemy import Column, Integer, String, ForeignKey

# load_dotenv()

databaseURL = os.getenv("DATABASE_URL")

Base = declarative_base()

# Define models

class HealthStatistics(Base):
    __tablename__ = 'health_statistics'

    id = Column(Integer, primary_key=True)
    year = Column(String(4), nullable=False)
    male = Column(String(4), nullable=False)
    female = Column(String(4), nullable=False)

    records = relationship('AdditionalHealthStatistics', back_populates='health_statistics')

class AdditionalHealthStatistics(Base):
    __tablename__ = 'additional_health_statistics'

    id = Column(Integer, primary_key=True)
    year = Column(String(4), nullable=False)
    male = Column(String(4), nullable=False)
    female = Column(String(4), nullable=False)

    records = relationship('LocationHealthStatistics', back_populates='additional_health_statistics')

class LocationHealthStatistics(Base):
    __tablename__ = 'location_health_statistics'
    id = Column(Integer, primary_key=True)
    all_women = Column(Integer, ForeignKey('health_statistics.id'), nullable=False)
    non_hispanic_white = Column(Integer, nullable=False)
    non_hispanic_black = Column(Integer, nullable=False)
    hispanic = Column(Integer, nullable=False)
    asian_and_pacific_islander = Column(Integer, nullable=False)
    american_indian_alaska_native = Column(Integer, nullable=False)
    other = Column(Integer, nullable=False)

    records = relationship('HealthStatistics', back_populates='location_health_statistics')

### Part 2 - initial sqlalchemy-engine to connect to db:

engine = create_engine("mysql+pymysql://alyssaflask3:Admin-2023-1@alyssa-final-app.mysql.database.azure.com/webapp",
                         connect_args={'ssl': {'ssl-mode': 'preferred'}},
                         )


DATABASE_URL = "mysql+mysqlconnector://alyssaflask3:Admin-2023-1@alyssa-final-app.mysql.database.azure.com/webapp"
engine = create_engine(DATABASE_URL)

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