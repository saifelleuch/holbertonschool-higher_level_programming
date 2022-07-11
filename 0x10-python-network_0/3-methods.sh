#!/bin/bash
#a Bash script that takes in a URL and displays all HTTP methods the server will accept.
churl -sI "$1"
