import numpy as np
door = np.array([1,0,1])

# probability if you don't switch 33%

n = 10000
count = 0
for value in range(n):
    x = np.random.choice(door)
    if x == 0:
        count = count +1
count/n

#probability if you do switch 66%
n = 10000
count = 0
for value in range(n):
    x = np.random.choice(door)
    if x == 1:
        count = count +1
count/n

