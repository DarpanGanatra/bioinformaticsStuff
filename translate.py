#!/usr/bin/python
""" This takes in a file that you put in after the string (e.g. ./translate.py input.txt) and outputs the result into out.txt"""

from sys import argv

t_file = open(argv[1], 'r')


def translate(file):
    sequence = file.read().replace('\n', '')
    sequence = sequence.replace('T', 'U')
    return sequence


u_file = open('out.txt', 'w')
u_file.write(translate(t_file))
u_file.close()

print(translate(t_file))
