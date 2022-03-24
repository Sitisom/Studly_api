#!/bin/bash

APPS="core auth course lessons students teachers"

for i in $APPS; do
  python manage.py makemigrations $(echo $i)
done