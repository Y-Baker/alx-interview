#!/usr/bin/python3
"""determines if a given data set represents a valid UTF-8 encoding"""


def validUTF8(data):
    """function to determines if  a valid UTF-8 encoding"""
    for i in data:
        if i > 255:
            return False
    return True
