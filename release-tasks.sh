#!/usr/bin/env bash
set -e

echo "Initializing database "

python migrate.py db init
python migrate.py db migrate
python migrate.py db upgrade
python bulkInsert.py

echo "Initializing database completed"