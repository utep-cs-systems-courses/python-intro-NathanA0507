import re
import sys

# print("Hello world!")

read_file = open(sys.argv[1], 'r')
write_file = open(sys.argv[2], 'w')

word_count = {}

for line in read_file:
    for word in line.split():
        treated_word = re.sub(r'\W+', '', word).lower()
        if treated_word in word_count:
            word_count[treated_word] += 1
        else:
            word_count[treated_word] = 1

# print(word_count)

items = word_count.items()

sorted_items = sorted(items)

# print(sorted_items)

for line in sorted_items:
    write_file.write(line[0] + " " + str(line[1]) + '\n')
