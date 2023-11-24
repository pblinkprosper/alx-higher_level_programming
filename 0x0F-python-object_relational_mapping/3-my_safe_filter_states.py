#!/usr/bin/python3
"""Takes argument but is safe from MySQL injections"""

import sys
import MySQLdb

if __name__ == "__main__":
    con = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = con.cursor()
    cur.execute("SELECT * FROM states")
    [print(state) for state in cur.fetchall() if state[1] == sys.argv[4]]
