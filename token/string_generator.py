from string import ascii_letters, punctuation, digits
from random import choice, randint

min = 4
max = 6
string_format = ascii_letters.upper()+digits#+punctuation
string_digits=digits
#generated_string = "".join(choice(string_format) for x in range(randint(min, max))).join(choice(string_digits) for y in range(randint(min, max)))
generated_string= "".join(choice(string_format) for x in range(randint(min, max)))
print("Your String is: {0}".format(generated_string))
print(len(generated_string))

"JGD-)-P$d8bW.}g#/2Vq;UK4HDfOAN-dZ^wf9qmTA%luUeJOzpu:7`'uv|a9K-"
