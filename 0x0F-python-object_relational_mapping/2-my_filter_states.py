#!/usr/bin/python3

'''
Write a script that takes in an argument and displays all values in
the `states` table of `hbtn_0e_0_usa` where `name` matches the argument.

    -Your script should take 4 arguments: `mysql username`, `mysql password`,
    `database name` and `state name searched` (no argument validation needed)
    -You must use the module `MySQLdb (import MySQLdb)`
    -Your script should connect to a MySQL server running on `localhost`
    at port `3306`
    -You must use `format` to create the SQL query with the user input
    -Results must be sorted in ascending order by `states.id`
    -Your code should not be executed when imported
'''


from sys import argv
import MySQLdb


def states_matching_the_searched_name(username, passwd, database, searched_name):
    '''List all states ordered by id in
    ascending order that match the searched_name'''
    db = MySQLdb.connect(
        host="localhost",
        user=username,
        passwd=passwd,
        db=database,
        port=3306)
    cursor = db.cursor()
    cursor.execute('SELECT * FROM states ORDER BY states.id ASC;')
    for list_result in cursor.fetchall():
        if list_result[1].startswith(searched_name):
            print(list_result)


if __name__ == '__main__':
    states_matching_the_searched_name(argv[1], argv[2], argv[3], argv[4])
