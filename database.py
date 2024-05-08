# database.py

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Parent(Base):
    __tablename__ = 'parents'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    children = relationship('Child', back_populates='parent')

    @property
    def child_count(self):
        return len(self.children)

class Child(Base):
    __tablename__ = 'children'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    parent_id = Column(Integer, ForeignKey('parents.id'))

    parent = relationship('Parent', back_populates='children')

# ORM methods
def create_parent(session, name):
    parent = Parent(name=name)
    session.add(parent)
    session.commit()
    return parent

def delete_parent(session, parent_id):
    parent = session.query(Parent).get(parent_id)
    if parent:
        session.delete(parent)
        session.commit()
        return True
    return False

def get_all_parents(session):
    return session.query(Parent).all()

def find_parent_by_id(session, parent_id):
    return session.query(Parent).get(parent_id)

# cli.py

import click
from database import create_engine, create_session, Parent, Child
from sqlalchemy.orm.exc import NoResultFound

@click.group()
def main():
    pass

@main.command(name='create-parent')
@click.option('--name', prompt='Enter parent name', help='Parent name')
def create_parent(name):
    session = create_session()
    create_parent(session, name)
    click.echo(f"Parent '{name}' created successfully.")

@main.command(name='delete-parent')
@click.option('--parent-id', prompt='Enter parent ID', help='Parent ID to delete')
def delete_parent(parent_id):
    session = create_session()
    if delete_parent(session, parent_id):
        click.echo(f"Parent with ID '{parent_id}' deleted successfully.")
    else:
        click.echo(f"Parent with ID '{parent_id}' not found.")

@main.command(name='list-parents')
def list_parents():
    session = create_session()
    parents = get_all_parents(session)
    for parent in parents:
        click.echo(f"ID: {parent.id}, Name: {parent.name}, Children: {parent.child_count}")

@main.command(name='find-parent')
@click.option('--parent-id', prompt='Enter parent ID', help='Parent ID to find')
def find_parent(parent_id):
    session = create_session()
    try:
        parent = find_parent_by_id(session, parent_id)
        click.echo(f"ID: {parent.id}, Name: {parent.name}, Children: {parent.child_count}")
    except NoResultFound:
        click.echo(f"Parent with ID '{parent_id}' not found.")

if __name__ == '__main__':
    main()
