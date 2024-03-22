#!/usr/bin/python3

'''
Write a script that adds the `State` object “Louisiana” to the
database `hbtn_0e_6_usa`

    -Your script should take 3 arguments:
    `mysql username`, `mysql password` and `database name`
    -You must use the module `SQLAlchemy`
    -You must import `State` and `Base` from
    `model_state` - `from model_state import Base, State`
    -Your script should connect to a MySQL server running
    on `localhost` at port `3306`
    -Print the new `states.id` after creation
    -Your code should not be executed when imported
'''


from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == '__main__':
    # Check if correct number of arguments are provided
    if len(argv) != 4:
        print("Usage: {} <username> <password> <database>".format(argv[0]))
        exit(1)

    # Extract arguments
    username, password, database = argv[1:]

    # Create engine to connect to MySQL server
    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost:3306/{database}')

    # Bind the engine to the metadata of the Base class
    Base.metadata.bind = engine

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Create a new State object
    new_state = State(name="Louisiana")

    # Add the new State object to the session
    session.add(new_state)

    # Commit the session to save changes to the database
    session.commit()

    # Print the new state's id
    print(new_state.id)

    # Close the session
    session.close()
