#!/usr/bin/python3
def safe_Print_integer(value):
    try:
        print("{:d}".format(value))
        return True
    except:
        return False
