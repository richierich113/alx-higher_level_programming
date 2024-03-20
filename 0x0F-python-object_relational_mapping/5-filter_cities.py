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
    query = '''
        SELECT cities.name 
        FROM cities
        INNER JOIN states ON cities.states_id=states.id 
        WHERE states.name = %s
        ORDER BY cities.id ASC;
    '''
    cursor.execute(query, (state_name,))
    for searched_results in cursor.fetchall():
        print(searched_results[0])

if __name__ == '__main__':
    cities_in_searched_state(argv[1], argv[2], argv[3], argv[4])
