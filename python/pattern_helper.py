#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Output a 2d json list to file to make it easier for creating patterns
"""
import json

def create_matrix(nr_rows, nr_cols):
    """
    Create a 2d list of size
    """
    matrix = [[0 for i in range(nr_cols)] for j in range(nr_rows)]
    return matrix

def write_to_file(matrix, name):
    """
    Use json to dump matrix to file
    """
    file_path = "patterns/{}.json".format(name)
    with open(file_path, "w") as fh:
        json.dump(matrix, fh, indent=4)

def start():
    """
    Entry point of program and asks for info about matrix
    """
    rows = int(input("How many rows should there be? "))
    cols = int(input("How many columns should there be? "))
    filename = input("What is the name of the pattern? ")
    
    matrix = create_matrix(rows, cols)
    write_to_file(matrix, filename)
    print("File {} is now created in patterns/ for you to fill in a pattern!".format(filename))

if __name__ == "__main__":
    start()