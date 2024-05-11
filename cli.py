import click

from models import Parent, Child
from database import create_session

@click.group()
def main():
    pass

@main.command(name='create-parent')
@click.option('--name', prompt='Enter parent name', help='Parent name')
def create_parent(name):
    session = create_session()
    parent = Parent(name=name)
    session.add(parent)
    session.commit()
    click.echo(f"Parent '{name}' created successfully.")

@main.command(name='delete-parent')
@click.option('--parent-id', prompt='Enter parent ID', help='Parent ID to delete')
def delete_parent(parent_id):
    session = create_session()
    parent = session.query(Parent).get(parent_id)
    if parent:
        session.delete(parent)
        session.commit()
        click.echo(f"Parent with ID '{parent_id}' deleted successfully.")
    else:
        click.echo(f"Parent with ID '{parent_id}' not found.")

@main.command(name='list-parents')
def list_parents():
    session = create_session()
    parents = session.query(Parent).all()
    for parent in parents:
        click.echo(f"ID: {parent.id}, Name: {parent.name}")

@main.command(name='find-parent')
@click.option('--parent-id', prompt='Enter parent ID', help='Parent ID to find')
def find_parent(parent_id):
    session = create_session()
    parent = session.query(Parent).get(parent_id)
    if parent:
        click.echo(f"ID: {parent.id}, Name: {parent.name}")
    else:
        click.echo(f"Parent with ID '{parent_id}' not found.")

if __name__ == '__main__':
    main()
