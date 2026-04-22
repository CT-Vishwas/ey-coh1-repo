import random

length_of_word = random.randint(1,50)

l1 = []
for i in range(length_of_word):
    char = chr(random.randint(97,122))
    l1.append(char)

s1 = ''.join(l1)
print(s1)