# Importing Required Libraries:
# Comment: Import necessary components from SQLAlchemy and MySQL connector.
# Syntax: from sqlalchemy import create_engine, Column, Integer, String, Sequence
# from sqlalchemy.orm import sessionmaker, declarative_base

from sqlalchemy import create_engine, Column, Integer, String, Sequence, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base, relationship
from sqlalchemy.ext.automap import automap_base
import pandas as pd

# Create an Engine:
# Comment: Create a new SQLAlchemy engine instance to connect to a MySQL database.
# Syntax: create_engine('mysql+pymysql://user:password@host/dbname')

# Ensure pymysql is installed: pip install pymysql

engine = create_engine('mysql+pymysql://username:password@localhost/mydatabase')
# Replace 'username', 'password', 'localhost', and 'mydatabase' with your MySQL credentials and database name.

# Define a Base Class:
# Comment: Define the base class for declarative class definitions.
# Syntax: Base = declarative_base()

Base = declarative_base()

# Define a Model (ORM Mapping):
# Comment: Define a model class that maps to a table in the MySQL database.
# Syntax:
# class ModelName(Base):
#     __tablename__ = 'table_name'
#     id = Column(Integer, primary_key=True)
#     name = Column(String)

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    name = Column(String(50))
    age = Column(Integer)

# Create the Table:
# Comment: Create tables in the MySQL database based on the model definitions.
# Syntax: Base.metadata.create_all(engine)

Base.metadata.create_all(engine)  # Creates the tables in the MySQL database

# Create a Session:
# Comment: Create a new session to interact with the MySQL database.
# Syntax: sessionmaker(bind=engine)()

Session = sessionmaker(bind=engine)
session = Session()

# Adding Records:
# Comment: Add new records to the MySQL database.
# Syntax:
# new_record = ModelName(column1=value1, column2=value2)
# session.add(new_record)
# session.commit()

new_user = User(name='Alice', age=30)
session.add(new_user)
session.commit()

# Querying Records:
# Comment: Query records from the MySQL database using the session.
# Syntax:
# results = session.query(ModelName).filter_by(condition).all()
# result = session.query(ModelName).filter_by(condition).first()

users = session.query(User).all()  # Get all users
alice = session.query(User).filter_by(name='Alice').first()

print(users)
print(alice)

# Updating Records:
# Comment: Update existing records in the MySQL database.
# Syntax:
# record = session.query(ModelName).filter_by(condition).first()
# record.column1 = new_value
# session.commit()

alice.age = 31
session.commit()

# Deleting Records:
# Comment: Delete records from the MySQL database.
# Syntax:
# record = session.query(ModelName).filter_by(condition).first()
# session.delete(record)
# session.commit()

session.delete(alice)
session.commit()

# Using Relationships:
# Comment: Define relationships between models for more complex queries.
# Syntax:
# class Parent(Base):
#     __tablename__ = 'parents'
#     id = Column(Integer, primary_key=True)
#     children = relationship('Child', back_populates='parent')

# class Child(Base):
#     __tablename__ = 'children'
#     id = Column(Integer, primary_key=True)
#     parent_id = Column(Integer, ForeignKey('parents.id'))
#     parent = relationship('Parent', back_populates='children')

class Parent(Base):
    __tablename__ = 'parents'
    id = Column(Integer, primary_key=True)
    children = relationship('Child', back_populates='parent')

class Child(Base):
    __tablename__ = 'children'
    id = Column(Integer, primary_key=True)
    parent_id = Column(Integer, ForeignKey('parents.id'))
    parent = relationship('Parent', back_populates='children')

Base.metadata.create_all(engine)  # Create the new tables

# Adding Records with Relationships:
# Comment: Add records with relationships between tables.
# Syntax:
# parent = Parent()
# child = Child(parent=parent)
# session.add(parent)
# session.add(child)
# session.commit()

parent = Parent()
child = Child(parent=parent)
session.add(parent)
session.add(child)
session.commit()

# Querying with Relationships:
# Comment: Query records and access related objects.
# Syntax:
# parent = session.query(Parent).first()
# children = parent.children

parent = session.query(Parent).first()
children = parent.children
print(children)

# Using SQL Expressions:
# Comment: Execute raw SQL expressions for complex queries.
# Syntax:
# from sqlalchemy import text
# result = engine.execute(text("SELECT * FROM table_name"))

from sqlalchemy import text

result = engine.execute(text("SELECT * FROM users"))
for row in result:
    print(row)

# Creating a View:
# Comment: Create a SQL view in the MySQL database.
# Syntax:
# from sqlalchemy import text
# engine.execute(text("CREATE VIEW view_name AS SELECT * FROM table_name"))

engine.execute(text("CREATE VIEW user_view AS SELECT name FROM users"))

# Reflecting Existing Tables:
# Comment: Reflect existing tables into SQLAlchemy models.
# Syntax:
# Base = automap_base()
# Base.prepare(engine, reflect=True)
# ExistingModel = Base.classes.table_name

Base = automap_base()
Base.prepare(engine, reflect=True)
User = Base.classes.users

# Handling Transactions:
# Comment: Handle transactions manually using the session.
# Syntax:
# session.begin()
# try:
#     # operations
#     session.commit()
# except:
#     session.rollback()

session.begin()
try:
    new_user = User(name='Bob', age=25)
    session.add(new_user)
    session.commit()
except:
    session.rollback()

# Creating Indexes:
# Comment: Create an index on a column for better query performance.
# Syntax:
# from sqlalchemy import Index
# Index('index_name', ModelName.column_name)

from sqlalchemy import Index

Index('ix_users_name', User.name)
Base.metadata.create_all(engine)  # Ensure the index is created

# Working with Data Types:
# Comment: Use various SQLAlchemy column types for MySQL.
# Syntax: Column(type, ...)

from sqlalchemy import Date, Float

class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    price = Column(Float)
    manufacture_date = Column(Date)

Base.metadata.create_all(engine)

# Using SQLAlchemy with Pandas:
# Comment: Load SQL query results directly into a Pandas DataFrame.
# Syntax:
# df = pd.read_sql_query(sql, engine)

df = pd.read_sql_query('SELECT * FROM users', engine)
print(df)

# Defining Custom Data Types:
# Comment: Define custom column types if needed.
# Syntax:
# class CustomType(TypeDecorator):
#     ...

from sqlalchemy.types import TypeDecorator, String

class UpperCaseString(TypeDecorator):
    impl = String

    def process_bind_param(self, value, dialect):
        if value is not None:
            value = value.upper()
        return value

    def process_result_value(self, value, dialect):
        if value is not None:
            value = value.upper()
        return value

class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(UpperCaseString(50))

Base.metadata.create_all(engine)
