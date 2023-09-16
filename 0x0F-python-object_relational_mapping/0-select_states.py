#!/usr/bin/python3

import MySQLdb
import sys
""" Select all the states from the database
    Args:
        argv[1](string): Db username
        argv[2](string): Db password
"""


if __name__ == '__main__':
    dbhost = "localhost"
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = "hbtn_0e_0_usa"

    conn = MySQLdb.connect(
            host=dbhost,
            port=3306,
            user=username,
            passwd=password,
            db=dbname,
            charset="utf8")

    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")

    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()