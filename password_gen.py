#import random functions
import random

#define shuffle function
def shuffle(string):
    templist = list(string)
    random.shuffle(templist)
    return ''.join(templist)

#randomise characters
upper_case_1 = chr(random.randint(65, 90))
upper_case_2 = chr(random.randint(65, 90))
lower_case_1 = chr(random.randint(97, 122))
lower_case_2 = chr(random.randint(97, 122))
number_1 = chr(random.randint(48, 57))
number_2 = chr(random.randint(48, 57))
special_1 = chr(random.randint(32, 64))
special_2 = chr(random.randint(32, 64))

#arrange and randomise character order
password = upper_case_1 + upper_case_2 + lower_case_1 + lower_case_2 + number_1 + number_2 + special_1 + special_2
password = shuffle(password)

#print password
print(password)
