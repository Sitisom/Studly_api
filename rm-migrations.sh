#!/bin/bash

find . -type d \( -path ./venv -o -path ./.venv \) -prune -false -o -type d -name "migrations" -exec rm -rf {} +