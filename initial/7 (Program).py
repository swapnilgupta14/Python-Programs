import string
import random

print("\nGenerate a random alphabetical string:")
max_length=5
s=""
for i in range(random.randint(1,max_length)):
    s=s+random.choice(string.ascii_letters)
print(s)