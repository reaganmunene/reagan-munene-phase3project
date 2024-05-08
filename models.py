from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Parent(Base):
    __tablename__ = 'parents'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    children = relationship('Child', back_populates='parent')

class Child(Base):
    __tablename__ = 'children'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    parent_id = Column(Integer, ForeignKey('parents.id'))

    parent = relationship('Parent', back_populates='children')

