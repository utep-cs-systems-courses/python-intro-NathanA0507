import re
import sys

# Open two files, one for reading (where words will be counted from) one for writing output
read_file = open(sys.argv[1], 'r')
write_file = open(sys.argv[2], 'w')

# Create a dictionary to hold all words
word_count = {}

for line in read_file:
    # Split by all non-alphanumeric characters
    for word in re.split('[^a-zA-Z]', line):
        word = word.lower()  # convert the word to lowercase for consistency
        if word in word_count:  # If the word is in the dictionary, just increment the amount
            word_count[word] += 1
        elif len(word) > 0:  # If the word isn't in the dictionary and is not the blank character '', add to dict
            word_count[word] = 1


# Get the items from the dict and sort them
items = word_count.items()
sorted_items = sorted(items)

# Put the sorted items into the output text file
for line in sorted_items:
    write_file.write(line[0] + " " + str(line[1]) + '\n')
