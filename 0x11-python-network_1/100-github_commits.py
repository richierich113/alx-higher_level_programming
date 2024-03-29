#!/usr/bin/python3

'''
-Write a Python script that takes 2 arguments in order to solve this challenge.
    -The first argument will be the `repository name`
    -The second argument will be the `owner name`
    -You must use the packages `requests` and `sys`
    -You are not allowed to import packages other than `requests` and `sys`
    -You don’t need to check arguments passed to the script (number or type)
-Only 17% of applicants for a backend position at Holberton finished this task
in less than 15 minutes.
'''

if __name__ == "__main__":
    import requests
    import sys
    url = "https://api.github.com/"
    username = sys.argv[1]
    repo = sys.argv[2]
    commits_url = url + "repos/{}/{}/commits".format(username, repo)
    response = requests.get(commits_url)
    if response.status_code == requests.codes.ok and len(response.text) > 0:
        try:
            my_obj = response.json()
            for i, obj in enumerate(my_obj):
                if i == 10:
                    break
                if type(obj) is dict:
                    name = obj.get('commit').get('author').get('name')
                    print("{}: {}".format(obj.get('sha'), name))
        except ValueError as invalid_json:
            pass
