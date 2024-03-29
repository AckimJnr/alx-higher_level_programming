#!/usr/bin/python3
"""
Select all the states from the database
    Args:
        argv[1](string): Db username
        argv[2](string): Db password
"""
import MySQLdb
import sys


if __name__ == '__main__':
    """
    This block makes it execute only as the main module
    """
    dbhost = "localhost"
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]

    conn = MySQLdb.connect(
            host=dbhost,
            port=3306,
            user=username,
            passwd=password,
            db=dbname,
            charset="utf8")

    cur = conn.cursor()
    cur.execute("""SELECT cities.id, cities.name, states.name
                FROM cities JOIN states
                ON states.id=cities.state_id ORDER BY cities.id ASC""")

    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
