#!/bin/bash

rm db.sqlite3
rm -rf ./Eamesapi/migrations
python3 manage.py migrate
python3 manage.py makemigrations Eamesapi
python3 manage.py migrate Eamesapi
python3 manage.py loaddata users
python3 manage.py loaddata tokens

