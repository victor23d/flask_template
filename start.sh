#!/usr/bin/env bash

export FLASK_ENV=development
export FLASK_APP=web.py

python3 -m flask run --host=0.0.0.0 --port=80