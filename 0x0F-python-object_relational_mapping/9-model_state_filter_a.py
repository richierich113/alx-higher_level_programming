#!/usr/bin/python3

'''
Write a script that lists all `State` objects that contain the letter `a`
database `hbtn_0e_6_usa`

    -Your script should take 3 arguments:
    `mysql username`, `mysql password` and `database name`
    -You must use the module `SQLAlchemy`
    -You must import `State` and `Base` from
    `model_state` - `from model_state import Base, State`
    -Your script should connect to a MySQL server running
    on `localhost` at port `3306`
    Results must be sorted in ascending order by `states.id`
    -The results must be displayed as they are in the example below
    -Your code should not be executed when imported
'''


from sys import argv
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == '__main__':
    # Check if correct number of arguments are provided
    if len(argv) != 4:
        print("Usage: {} <username> <password> <database>".format(argv[0]))
        exit(1)

    # Create engine to connect to MySQL server
    engine = create_engine(
        f'mysql+mysqldb://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}')

    # Bind the engine to the metadata of the Base class
    Base.metadata.bind = engine

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query State objects that contain the letter 'a'
    states_with_a = session.query(State).filter(State.name.like('%a%')).\
        order_by(State.id).all()

    # Display the results
    for state in states_with_a:
        print(f"{state.id}: {state.name}")

    # Close the session
    session.close()
