import math

print('how many sequences of k objects can be made from a collection of n objects?')
print('for example, how many possible 3 letter words in english (all combos)')
print('the formula is n^k')
print('THIS IS WITH REPLACEMENT')

collect = int(input('how many items in your collection?'))
items = int(input('How items in the sequence?'))
possible = collect ** items
print('the total possible is ' + str(possible))

print('how many sequences of k objects can be made from a collection of n objects - with no repeat choices?')
print('for example, in a class of 15 students, the people in a 5 person group, and the order determines their role')
print('the formula is n!/(k!(n-k)!)')
print('THIS IS WITHOUT REPLACEMENT')

collect2 = int(input('how many items in your collection?'))
items2 = int(input('How items in the sequence?'))
possible2 = math.factorial(collect2)/math.factorial(collect2-items2)
print('the total possible is ' + str(possible2))

