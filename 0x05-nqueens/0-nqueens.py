#!/usr/bin/python3
"""solve the nqueens problem"""
import sys

num: str = sys.argv[1]
if not num.isnumeric():
    print("N must be a number")
else:
    num = int(num)
    if num < 4:
        print("N must be at least 4")
    else:
        print(num)
