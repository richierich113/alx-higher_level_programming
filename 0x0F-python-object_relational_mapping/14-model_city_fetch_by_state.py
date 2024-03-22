#!/usr/bin/python3
'''
write a script `14-model_city_fetch_by_state.py` that prints
all `City` objects from the database `hbtn_0e_14_usa`:

    -Your script should take 3 arguments:
    `mysql username`, `mysql password` and `database name`
    -You must use the module `SQLAlchemy`
    -You must import `State` and `Base` from
    `model_state` - `from model_state import Base, State`
    -Your script should connect to a MySQL server running
    on `localhost` at port `3306`
    -Results must be sorted in ascending order by `cities.id`
    -Results must be display as they are in the example
    below (`<state name>: (<city id>) <city name>`)
    -Your code should not be executed when imported
'''


from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State, City


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

    # Query all City objects and join with State to get state name
    cities = session.query(City, State).join(State).order_by(City.id).all()

    # Display the results
    for city, state in cities:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    # Close the session
    session.close()
