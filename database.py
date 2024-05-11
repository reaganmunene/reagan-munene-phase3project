# database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Base

def create_session():
    engine = create_engine('sqlite:///data.db')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    return Session()

