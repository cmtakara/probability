import math

# the probability of getting k heads (or tails) out of n flips
print('To figure out the probability of a given number of heads - or tails - you get ')
print('if the order does not matter, use collections')
print('the formula is: number of favorable outcomes over total number of outcomes')
print('number of favorable outcomes is n choose k, where n is total flips and k is the number of heads results')
print('total number of outcomes is 2^n')

n = int(input('What is the total number of coin flips?  '))
k = int(input('How many times to get heads as a result? '))

fav_outcome = math.factorial(n)/(math.factorial(k)*math.factorial(n-k))
tot_outcome = 2**n
prob = fav_outcome/tot_outcome

print('the probability is ' + str(prob))

print('that example was for one value')
print('if you want a range, find the probability for each number of heads and add them')
print('this time, have a range - such as 4-6 heads')
start = int(input('what is the beginning number in the range? '))
stop = int(input('what is the ending number in the range? '))
n = int(input('What is the total number of coin flips?  '))

total = 0

for i in range(start, stop+1):
    fav_outcome = math.factorial(n)/(math.factorial(i)*math.factorial(n-i))
    print('there are ' + str(fav_outcome) + ' ways to get ' + str(i) + ' results')
    total += fav_outcome
prob = total/2**n

print('the probability is ' + str(prob))