# Find the expected value in the following conditions
# a person rolls two dice, and they get x amount of money if certain outcomes show
# they get none otherwise


# start with the probabilities for the outcomes of the sums of the values
#  need the number of times each outcome occurs
num_sum_out = {
    2: 1,
    3: 2,
    4: 3,
    5: 4,
    6: 5,
    7: 6,
    8: 5,
    9: 4,
    10: 3,
    11: 2,
    12: 1
}

# iterate through to find probabilities
# Iterate through keys and modify values to probs by dividing by total outcomes
#   6 is the number of outcomes from 1 die
#   there are two die
total = 6 ** 2
for key in num_sum_out:
    num_sum_out[key] = num_sum_out[key] / total

# check if we are looking for a sum, same value, 
print('you can find expected value for a values of sums of the dice by entering sum')
print('you can find the expected value for all matching by entering matching')
prob_type = input('enter sum or matching: ')

if (prob_type == 'sum') :
    print('finding the expected value of sums')
    # in this case, we need to know which sums we are looking for
    out = input('enter the values that result in a win, separated by commas: ').replace(" ", "").split(',')
    win = int(input('enter the amount to be won: '))
    # find the total probability by adding all of the probabilities of favorable outcomes
    sum = 0
    for val in out:
        prob = num_sum_out[int(val)]
        print(prob)
        sum += prob
    print(sum)
    exp_val = sum*win
    print('_____ the expected value is: ', exp_val)
elif (prob_type == 'matching'):
    # print('finding the expected value of all matching pairs')
    win = int(input('enter the amount to be won: '))
    # probability of two dice being the same is
    # 6/36 - the number of matching outcomes/the total number of outcomes
    prob = 6/36
    exp_val = prob*win
    print('_____ the expected value is: ', exp_val)
else:
    print('that was not a valid input')