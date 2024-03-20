#!/usr/bin/python3

'''
a script that takes in an argument and displays all values in
the `states` table of `hbtn_0e_0_usa` where `name` matches the argument.

    - script  take 4 arguments: `mysql username`, `mysql password`,
    `database name` and `state name searched` (no argument validation needed)
    - use the module `MySQLdb (import MySQLdb)`
    - connect to a MySQL server running on `localhost`
    at port `3306`
    - use `format` to create the SQL query with the user input
    -Results sorted in ascending order by `states.id`
    - script not executed when imported
'''


from sys import argv
import MySQLdb


def states_matching_the_searched_name(user, passwd, db, searched_name):
    '''List all states ordered by id in
    ascending order that match "searched_name"'''
    db = MySQLdb.connect(
        host="localhost",
        user=user,
        passwd=passwd,
        db=db,
        port=3306)
    cursor = db.cursor()
    cursor.execute('SELECT * FROM states ORDER BY states.id ASC;')
    for list_result in cursor.fetchall():
        if list_result[1].startswith(searched_name):
            print(list_result)


if __name__ == '__main__':
    states_matching_the_searched_name(argv[1], argv[2], argv[3], argv[4])
