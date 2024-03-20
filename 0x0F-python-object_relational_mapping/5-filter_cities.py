#!/usr/bin/python3

'''
Write a script that takes in the name of a state as an argument and
lists all cities of that state, using the database hbtn_0e_4_usa

    -Your script should take 4 arguments: `mysql username`, `mysql password`
    and `database name` and state name (SQL injection free!)
    -You must use the module `MySQLdb (import MySQLdb)`
    -Your script should connect to a MySQL server running on `localhost`
    at port `3306`
    -Results must be sorted in ascending order by `cities.id`
    -You can use only `execute()` once
    -Your code should not be executed when imported

'''


from sys import argv
import MySQLdb


def cities_in_searched_state(username, passwd, database, state_name):
    '''List all cities in the searched state'''
    db = MySQLdb.connect(
        host="localhost",
        user=username,
        passwd=passwd,
        db=database,
        port=3306)
    cursor = db.cursor()
    cursor.execute('''SELECT cities.name, states.name FROM cities\
    INNER JOIN states ON cities.state_id=states.id ORDER BY cities.id ASC;''')
    state_cities = []
    for search_result in cursor.fetchall():
        if search_result[1] == state_name:
            state_cities.append(search_result[0])
    print(', '.join(state_cities))


if __name__ == '__main__':
    cities_in_searched_state(argv[1], argv[2], argv[3], argv[4])
