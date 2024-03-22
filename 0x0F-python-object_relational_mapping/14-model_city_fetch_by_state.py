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

from sqlalchemy import (create_engine)
from model_state import Base, State
from model_city import City
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    engine = create_engine(
        f'mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for instance in session.query(City).order_by(City.id):
        state_data = session.query(State).filter_by(id=instance.state_id).one()
        state_name = state_data.name
        print(f"{state_name}: ({instance.id}) {instance.name}")
