#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Output a 2d json list to file to make it easier for creating patterns
"""
from game import config

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
    file_path = config.PATTERN_PATH + "/{}.json".format(name)
    with open(file_path, "w") as fh:
        fh.write(matrix)

def insert_newline(matrix):
    """
    Format matrix with newlines adter each sub list
    """
    s_matrix = str(matrix)
    matrix = s_matrix.replace("], ", "],\n")
    return matrix

def start():
    """
    Entry point of program and asks for info about matrix
    """
    rows = int(input("How many rows should there be? "))
    cols = int(input("How many columns should there be? "))
    filename = input("What is the name of the pattern? ")

    matrix = create_matrix(rows, cols)
    matrix = insert_newline(matrix)
    write_to_file(matrix, filename)
    print("File {}.json is now created in ".format(filename) + config.PATTERN_PATH + "/ for you to fill in a pattern!")

if __name__ == "__main__":
    start()
