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
    try:
        dbhost = "localhost"
        username = sys.argv[1]
        password = sys.argv[2]
        dbname = sys.argv[3]
        searchItem = sys.argv[4]

        conn = MySQLdb.connect(
                host=dbhost,
                port=3306,
                user=username,
                passwd=password,
                db=dbname,
                charset="utf8")

        cur = conn.cursor()
        cur.execute("""SELECT cities.name FROM states
                    JOIN cities on states.id = cities.state_id
                    WHERE states.name LIKE %s
                    ORDER BY states.id ASC""", (searchItem,))
        cities = []
        query_rows = cur.fetchall()

        for row in query_rows:
            cities.append(row[0])

        print(', '.join(cities))
    except MySQLdb.Error as err:
        print("Error: {}".format(err))

    finally:
        cur.close()
        conn.close()
