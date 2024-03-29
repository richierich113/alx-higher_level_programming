#!/usr/bin/python3

'''
-Write a Python script that takes your GitHub credentials
(username and password) and uses the `GitHub API` to display your `id`
    -You must use `[Basic Authentication]
(https://docs.github.com/en/rest/overview/other-authentication-methods)`
with a `[personal access token](https://docs.github.com/en/authentication\
/keeping-your-account-and-data-secure/creating-a-personal-access-token)`
as password to access to your information
(only `read:user` permission is needed)
    -The first argument will be your `username`
    -The second argument will be
    your `password` (in your case, a `personal access token as password`)
    -You must use the package `requests` and `sys`
    -You are not allowed to import packages other than `requests` and `sys`
    -You don’t need to check arguments passed to the script (number or type)
'''

if __name__ == "__main__":
    import requests
    from requests.auth import HTTPBasicAuth
    import sys
    url = "https://api.github.com/"
    user_url = url + "user"
    username = sys.argv[1]
    password = sys.argv[2]
    response = requests.get(user_url,
                            auth=HTTPBasicAuth(username,
                                               password))
    if response.status_code == requests.codes.ok and len(response.text) > 0:
        try:
            my_obj = response.json()
            print(my_obj.get('id'))
        except ValueError as invalid_json:
            print('Not a valid JSON')
    else:
        print(None)
