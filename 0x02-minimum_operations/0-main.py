#!/usr/bin/python3
"""
Main file for testing the minOperations function.
"""

minOperations = __import__('0-minoperations').minOperations

def main():
    # Test cases
    n = 4
    print(f"Min # of operations to reach {n} char: {minOperations(n)}")

    n = 12
    print(f"Min # of operations to reach {n} char: {minOperations(n)}")

if __name__ == "__main__":
    main()
