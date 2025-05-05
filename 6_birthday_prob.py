# the probability of n people having unique birthdays is 
# 365 x 364 x 363 x ... x (365-n-1)
# all over 365 ^ n
# so the probability of any shared birthdays 1 minus that number

num_people = int(input('how many people in the room? '))

ans = 1
for i in range(num_people):
    quot = (365 - i)/365
    ans *= quot
print('the probability of no one sharing a birthday is ' + str(ans))