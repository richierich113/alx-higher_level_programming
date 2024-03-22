#!/usr/bin/python3
'''
Write a script that lists all `State` objects from the
database `hbtn_0e_6_usa`

    -Your script should take 3 arguments:
    `mysql username`, `mysql password` and `database name`
    -You must use the module `SQLAlchemy`
    -You must import `State` and `Base` from
    `model_state` - `from model_state import Base, State`
    -Your script should connect to a MySQL server running
    on `localhost` at port `3306`
    -Results must be sorted in ascending order by `states.id`
    -The results must be displayed as they are in the example below
    -Your code should not be executed when imported
'''


from sys import argv
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    # Check if correct number of arguments are provided
    if len(argv) != 4:
        print("Usage: {} <username> <password> <database>".format(argv[0]))
        exit(1)

    # Create engine to connect to MySQL server
    try:
        engine = create_engine(
            f'mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}')
        # Create all tables in the database
        Base.metadata.create_all(engine)
    except Exception as e:
        print("An error occurred:", e)
        exit(1)

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        # Query all State objects and print them sorted by id
        for instance in session.query(State).order_by(State.id):
            print(f"{instance.id}: {instance.name}")
    except Exception as e:
        print("An error occurred:", e)
    finally:
        # Close the session
        session.close()

