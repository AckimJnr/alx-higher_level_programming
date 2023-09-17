#!/usr/bin/python3
"""
creates the State “California” with the City “San Francisco”
"""
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship

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

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    california_state = session.query(State).filter_by(
            name='California').first()

    if california_state is None:
        california_state = State(name='California')
        session.add(california_state)

    san_francisco = City(name='San Francisco')

    san_francisco.state = california_state

    session.add(san_francisco)
    session.commit()
    session.close()
