#!/bin/python3

import os

# List environment variables
env_vars = os.environ.items()
print("List of ENV VAR")

for key, value in env_vars:
    print(key)

while True:
    x = input('Enter desired VAR: ')
    x = x.replace(" ", "_") 
    try:
        print(f"Output: {os.environ[x.upper()]}")

    except KeyError:
        print(f"Environment variable '{x.upper()}' not found.")
