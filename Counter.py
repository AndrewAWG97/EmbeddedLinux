#!/bin/python3

ls = [1, 2, 4, 3, 44, 6, 7, 4, 4, 2, 6, 5, 4]
counter = 0

for i in range(len(ls)):
    if ls[i] == 4:
        counter = counter + 1

print(f"Counter = {counter}")
