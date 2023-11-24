#!/usr/bin/python3
"""
    Takes in argument and displays all values in states table
    where name matches argument.
"""

import sys
import MySQLdb

if __name__ == "__main__":
    con = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = con.cursor()
    cur.execute("SELECT * FROM states WHERE\
            name '{}' ORDER BY states.id ASC".format(sys.argv[4]))
    [print(state) for state in cur.fetchall()]
