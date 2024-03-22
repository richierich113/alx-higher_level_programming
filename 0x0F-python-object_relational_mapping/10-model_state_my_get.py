#!/usr/bin/python3

'''
Write a script that prints the `State` object with the `name`
passed as argument from the database `hbtn_0e_6_usa`

    -Your script should take 4 arguments:
    `mysql username`, `mysql password`, `database name` and
    `state name to search` (SQL injection free)
    -You must use the module `SQLAlchemy`
    -You must import `State` and `Base` from
    `model_state` - `from model_state import Base, State`
    -Your script should connect to a MySQL server running
    on `localhost` at port `3306`
    -You can assume you have one record with the state name to search
    -Results must display the `states.id`
    -If no state has the name you searched for, display `Not found`
    -Your code should not be executed when imported
'''


from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == '__main__':
    # Check if correct number of arguments are provided
    if len(argv) != 5:
        print("Usage: {} <username> <password> <database> \
        <state_name>".format(argv[0]))
        exit(1)

    # Extract arguments
    username, password, database, state_name = argv[1:]

    # Create engine to connect to MySQL server
    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost:3306/{database}')

    # Bind the engine to the metadata of the Base class
    Base.metadata.bind = engine

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query State object with the given state name
    state = session.query(State).filter(State.name == state_name).first()

    # Check if state is found
    if state:
        print(state.id)
    else:
        print("Not found")

    # Close the session
    session.close()
