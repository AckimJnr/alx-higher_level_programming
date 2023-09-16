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
        cur.execute("SELECT * FROM states\
                    WHERE BINARY name LIKE %s\
                    ORDER BY id ASC", (searchItem,))

        query_rows = cur.fetchall()
        for row in query_rows:
            print(row)

    except MySQLdb.Error as err:
        print("Error: {}".format(err))

    finally:
        cur.close()
        conn.close()
