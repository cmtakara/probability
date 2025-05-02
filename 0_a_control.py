import random

# run multiple times to show different outcomes
for i in range(10):
# find an integer, 0 or 1, randomly (to illustrate probability)
    prob = random.randint(0, 1)
    if prob == 1:
        print('heads')
    else:
        print('tails')