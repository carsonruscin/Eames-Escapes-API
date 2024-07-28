#!/bin/bash

rm db.sqlite3
rm -rf ./Eamesapi/migrations
python3 manage.py migrate
python3 manage.py makemigrations Eamesapi
python3 manage.py migrate Eamesapi
python3 manage.py loaddata users
python3 manage.py loaddata tokens
python3 manage.py loaddata propertytype
python3 manage.py loaddata amenity
python3 manage.py loaddata property
python3 manage.py loaddata booking
python3 manage.py loaddata propertyamenity
python3 manage.py loaddata propertyimage

