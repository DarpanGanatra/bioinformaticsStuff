#!/usr/bin/python
"""This will take an input and print out the amount of nucletides in A,C,G,T order"""
from collections import Counter
from sys import argv

file = open(argv[1], 'r')


def nuceloutide_count(file):
    sequence = file.read().replace('\n', '')
    output = Counter(sequence)
    freq = []
    freq.append(output['A'])
    freq.append(output['C'])
    freq.append(output['G'])
    freq.append(output['T'])
    return freq


for i in nuceloutide_count(file):
    print(i, sep=" ", end=" ")
