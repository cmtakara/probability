import math

print('Calculate how many numbers there are from a starting number to an ending number')
print('The formula is n - k + 1, where n is the bigger number and k is the smaller number')
begin = int(input('What is the first number? '))
end = int(input('what is the last number? '))
numNum = end - begin + 1
print('There are ' + str(numNum) + ' numbers between ' + str(begin) + ' and ' + str(end))

print('how many numbers between k (the beginning) and n (the end) that are divisible by another number q')
begin2 = int(input('What is the first number? '))
end2 = int(input('what is the last number? '))
q = int(input('what is the number you are dividing by?'))
# need to divide begin2/q - but then take the ceiling 
# the logic is - if k is not evenly divisible by that number, you don't want to count it
# you want to move to the next integer
# floor would include the number prior
begin3 = math.ceil(begin2/q)
# need to divide end2/q - but then take the floor
# the logic is - if n is not evenly divisible by that number, you don't want to count it
# you want to move back to the prior integer
end3 = math.floor(end2/q)
numNum2 = end3 - begin3 + 1
print('There are ' + str(numNum2) + ' numbers between ' + str(begin2) + ' and ' + str(end2) + ' that are divisible by ' + str(q))
