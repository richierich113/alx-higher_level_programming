#!/bin/bash
# script sends request to a URL passed as an argument, and displays only the status code of the response. You are not allowed to use any pipe, redirection, etc.
curl -L -s -X HEAD -w "%{http_code}" "$1"
