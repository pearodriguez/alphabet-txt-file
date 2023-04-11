alphabet = 'abcdefghijklmnopqrstuvwxyz'
count = 1

open_file = open('alphabet.txt', 'w')

for letter in alphabet:
    open_file.write(letter + '\n')
    
open_file.close()

open_file = open('alphabet.txt', 'r')
contents = open_file.readline()

while contents != '':
    line = contents
    line = line.rstrip()
    print(str(count) + ': ' + line)
    count += 1
    contents = open_file.readline()

open_file.close()
