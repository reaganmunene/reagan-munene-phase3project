import click

@click.group()
def main():
    pass

@main.command(name='create-parent')
@click.option('--name', prompt='Enter parent name', help='Parent name')
def create_parent(name):
    from database import create_session, Parent, Child
    session = create_session()
    parent = Parent(name=name)
    session.add(parent)
    session.commit()
    click.echo(f"Parent '{name}' created successfully.")

@main.command(name='delete-parent')
@click.option('--parent-id', prompt='Enter parent ID', help='Parent ID to delete')
def delete_parent(parent_id):
    from database import create_session, Parent, Child
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
    from database import create_session, Parent, Child
    session = create_session()
    parents = session.query(Parent).all()
    for parent in parents:
        click.echo(f"ID: {parent.id}, Name: {parent.name}")

@main.command(name='find-parent')
@click.option('--parent-id', prompt='Enter parent ID', help='Parent ID to find')
def find_parent(parent_id):
    from database import create_session, Parent, Child
    from sqlalchemy.orm.exc import NoResultFound
    session = create_session()
    try:
        parent = session.query(Parent).filter_by(id=parent_id).one()
        click.echo(f"ID: {parent.id}, Name: {parent.name}")
    except NoResultFound:
        click.echo(f"Parent with ID '{parent_id}' not found.")

if __name__ == '__main__':
    main()
