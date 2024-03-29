#!/usr/bin/python3
'''
Write a Python script that takes in a letter and sends a `POST` request
to `http://0.0.0.0:5000/search_user` with the letter as a parameter.
    The letter must be sent in the variable `q`
    If no argument is given, set `q=""`
    If the response body is properly JSON formatted and not empty, display
    the id and name like this: [<id>] <name>
    Otherwise:
        Display `Not a valid JSON` if the JSON is invalid
        Display `No result` if the JSON is empty
    -You must use the packages `requests` and `sys`
    -You are not allowed to import packages other than `requests` and `sys`
    -You don’t need to error check arguments passed to the
    script (number or type)
Please test your script in the sandbox provided, using the web server running
on port 5000
'''

if __name__ == "__main__":
    import requests
    import sys
    url = "http://0.0.0.0:5000/search_user"
    if len(sys.argv) > 1:
        q = sys.argv[1]
    else:
        q = ""
    query = {'q': q}
    response = requests.post(url, data=query)
    if response.status_code != requests.codes.ok or len(response.text) <= 0:
        print('No result')
        sys.exit()
    else:
        try:
            my_obj = response.json()
            if len(my_obj) == 0:
                print('No result')
                sys.exit()
            my_id = my_obj.get('id')
            my_name = my_obj.get('name')
            print("[{}] {}".format(my_id, my_name))
        except ValueError as invalid_json:
            print('Not a valid JSON')
