#!/usr/bin/python3

'''
Write a script that takes in an argument and displays all values in the
`states` table of `hbtn_0e_0_usa` where `name` matches the argument.
But this time, write one that is safe from MySQL injections!

    -Your script should take 4 arguments: `mysql username`, `mysql password`,
    `database name` and `state name searched` (safe from MySQL injection)
    -You must use the module `MySQLdb (import MySQLdb)`
    -Your script should connect to a MySQL server running on `localhost`
    at port `3306`
    -You must use `format` to create the SQL query with the user input
    -Results must be sorted in ascending order by `states.id`
    -Your code should not be executed when imported

    Did you test "Arizona'; TRUNCATE TABLE states ;
    SELECT * FROM states WHERE name = '" as an input?
'''


from sys import argv
import MySQLdb


def injection_safe_search_matching(username, passwd, database, searched_name):
    '''List all states matching "state_name"'''
    db = MySQLdb.connect(
        host="localhost",
        user=username,
        passwd=passwd,
        db=database,
        port=3306)
    cursor = db.cursor()
    query = 'SELECT * FROM states WHERE name = %s ORDER BY states.id ASC;'
    cursor.execute(query, (searched_name,))
    for search_results in cursor.fetchall():
        print(search_results)

if __name__ == '__main__':
    injection_safe_search_matching(argv[1], argv[2], argv[3], argv[4])
