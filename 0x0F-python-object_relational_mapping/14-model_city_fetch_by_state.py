#!/usr/bin/python3
"""
Prints all city objects from the database
"""
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Lets this execute only when not imported
    """
    dbUsername = sys.argv[1]
    dbPassword = sys.argv[2]
    dbName = sys.argv[3]
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'.format(
                dbUsername,
                dbPassword,
                dbName),
            pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    query = session.query(State, City).filter(
            State.id == City.state_id
            ).order_by(City.id).all()

    for state, city in query:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.close()
