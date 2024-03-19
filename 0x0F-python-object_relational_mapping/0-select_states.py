#!/usr/bin/python3

'''
A script that lists all `states` from the database `hbtn_0e_0_usa`:

    -take 3 arguments: `mysql username`, `mysql password`
    and `database name` (no argument validation needed)
    -uses the module `MySQLdb (import MySQLdb)`
    -script  connect to a MySQL server running
    on `localhost` at port `3306`
    -Results sorted in ascending order by `states.id`
    -Code not executed when imported
'''


from sys import argv
import MySQLdb


def list_all_states(username, passwd, db):
    '''List all states ordered by id in
    ascending order'''
    db = MySQLdb.connect(
        host="localhost",
        user=username,
        passwd=passwd,
        db=db,
        port=3306)
    cursor = db.cursor()
    cursor.execute('SELECT * FROM states ORDER BY states.id ASC;')
    for states_result in cursor.fetchall():
        print(states_result)


if __name__ == '__main__':
    list_all_states(argv[1], argv[2], argv[3])
