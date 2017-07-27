import random

print("choice")
print(range(50))

print(random.choice(range(50)))

print(random.choice([5,6,1,2]))

k = random.choice('Hello World')
print(k)

print("randrange")
print(random.randrange(1, 5, 2))
print(random.randrange(1, 6, 2))

print("random")
print(random.random())

print(int(random.random()*100))