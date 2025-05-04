from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import pymysql

# Define the database connection URL
username = 'root'
password = '1'  # Replace with the actual password
host = '127.0.0.1'
port = 3306
database = 'mydatabase'  # Replace with the actual database name

engine_url = f'mysql+pymysql://{username}:{password}@{host}:{port}/{database}'

try:
    # Create the engine
    engine = create_engine(engine_url)

    # Define the base class for our models
    Base = declarative_base()

    # Define a simple model
    class User(Base):
        __tablename__ = 'users'
        id = Column(Integer, primary_key=True)
        name = Column(String(50))
        email = Column(String(100))

    # Create the table
    Base.metadata.create_all(engine)

    # Create a session maker
    Session = sessionmaker(bind=engine)

    # Create a session
    session = Session()

    # Add a new user
    new_user = User(name='John Doe', email='john.doe@example.com')
    session.add(new_user)
    session.commit()

    # Query the users
    users = session.query(User).all()
    for user in users:
        print(user.name, user.email)

except pymysql.err.OperationalError as e:
    print(f"Error: {e}")
    if e.args[0] == 1698:
        print("Access denied for user 'root'@'localhost'. Please check your MySQL password.")
    else:
        print("An error occurred while connecting to the database.")
except Exception as e:
    print(f"An error occurred: {e}")