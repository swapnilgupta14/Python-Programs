import random

# random.randint generates random number
print("random.randint(1,20)=",random.randint(1,20))
print("random.randint(1,20)=",random.randint(1,20))
print("\n")

print(random.choice(['apple','pear','banana']))
#'apple'
print(random.sample(['1','2','3','4','5','6','7'],3))
#[5,2,1]
print(random.random())
#0.8334443073581229
print(random.randrange(1,6))
print(random.randint(1,6))