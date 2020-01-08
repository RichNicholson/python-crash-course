filename = 'resources/chapter_10/pi_million_digits.txt'
birthday = '090775'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

if birthday in pi_string:
    print("Your birthday is in the first million digits of pi")
else:
    print("Your birthday is not in the first million digits of pi")