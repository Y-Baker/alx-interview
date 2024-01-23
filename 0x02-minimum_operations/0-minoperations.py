#!/usr/bin/python3
"""there is a single character H.
Your text editor can execute only two operations in this file: Copy All, Paste
Given a number n, write a method that calc the fewest number of operations
needed to result in exactly n H characters in the file."""


def minOperations(n):
    """Problem Solving"""
    if n <= 1:
        return 0

    current = 1
    operations = 0
    copied = 0
    while (current < n):
        if (n % current == 0):
            operations += 1   # Copy All
            copied = current

        operations += 1   # Paste
        current += copied

    return operations
