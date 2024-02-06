import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Create an engine to connect to the database
engine = sa.create_engine('sqlite:///books.db', echo=True)

# Create a base class for declarative class definitions
Base = declarative_base()

# Define the Books class
class Books(Base):
    __tablename__ = 'books'

    title = sa.Column(sa.String, primary_key=True)
    author = sa.Column(sa.String)
    year = sa.Column(sa.Integer)

# Create a session maker
Session = sessionmaker(bind=engine)
session = Session()

# Query and print titles in alphabetical order
titles = session.query(Books.title).order_by(Books.title).all()
for title in titles:
    print(title[0])

# Close the session
session.close()
