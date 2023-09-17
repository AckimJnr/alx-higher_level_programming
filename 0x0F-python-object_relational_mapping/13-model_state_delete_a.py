#!/usr/bin/python3
"""
Deletes states
"""
import sys
from model_state import Base, State
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

    states_to_delete = session.query(State).filter(
            State.name.like('%a%')).all()

    if states_to_delete:
        for state in states_to_delete:
            session.delete(state)
        session.commit()

    session.close()
