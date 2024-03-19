#!/usr/bin/python3

'''
Write a script that lists all `states` with a `name` starting
with `N` (upper N) from the database `hbtn_0e_0_usa`:

    -Your script should take 3 arguments: `mysql username`, `mysql password`
    and `database name` (no argument validation needed)
    -You must use the module `MySQLdb (import MySQLdb)`
    -Your script should connect to a MySQL server running
    on `localhost` at port `3306`
    -Results must be sorted in ascending order by `states.id`
    -Your code should not be executed when imported
'''


from sys import argv
import MySQLdb


def states_starting_with_N(username, passwd, database):
    '''List all states ordered by id in
    ascending order that start with "N"'''
    db = MySQLdb.connect(
        host="localhost",
        user=username,
        passwd=passwd,
        db=database,
        port=3306)
    cursor = db.cursor()
    cursor.execute('SELECT * FROM states ORDER BY states.id ASC;')
    for list_result in cursor.fetchall():
        if list_result[1].startswith('N'):
            print(list_result)


if __name__ == '__main__':
    states_starting_with_N(argv[1], argv[2], argv[3])





































