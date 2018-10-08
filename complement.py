#!/usr/bin/python

''' This is a simple way to take any file that's inputted after the script (e.g. ./complement.py input.txt) and will output the complemented string into output.txt'''

from sys import argv

file = open(argv[1], 'r')

complemented_array = []


def complement(file, complemented_array):
    # The next part of this opens the file that was inputted
    reversed_sequence = file.read().replace('\n', '')
    # This takes in the array that we fed the file into and reverses it
    reversed_sequence = reversed_sequence[::-1]
    # As you can imagine, this takes the initially empty array complemented_array and appends complementary nucleic bases to it
    for i in reversed_sequence:
        if i == 'A':
            complemented_array.append('T')
        elif i == 'G':
            complemented_array.append('C')
        elif i == 'C':
            complemented_array.append('G')
        else:
            complemented_array.append('A')
    return complemented_array


# Runs the function
complement(file, complemented_array)

# Makes our appended array into a string
output_string = ''.join(complemented_array)
# Writes the string to a file called out.txt
writer = open('out.txt', 'w')
writer.write(output_string)
writer.close()
print("Done")
