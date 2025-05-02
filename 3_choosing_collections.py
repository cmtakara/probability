import math 

print('how many collections of k objects can be made from a collection of n objects - with no repeat choices?')
print('for example, in a class of 15 students, the people in a 5 person group')
print('the formula is n!/(k!(n-k)!)')
print('THIS IS WITHOUT REPLACEMENT')

collect2 = int(input('how many items in your collection?'))
items2 = int(input('How items in the new collection?'))
possible2 = math.factorial(collect2)/(math.factorial(items2)*math.factorial(collect2-items2))
print('the total possible is ' + str(possible2))

print('using the binomial theorem to define the coefficients of the expanded form of (a+b)^n')
print('in general the formula is that the coefficient for the i term, with the first term being 0th')
print('is: (n choose i), where the rest of the term is a^(n-1)b^i')

terms = int(input('what is the exponent that your binomial is raised to?'))
for i in range(terms):
    # the coefficient is 1 choose terms
    coeff = math.factorial(terms)/(math.factorial(i)*math.factorial(terms-i))
    print('the ' + str(i) + ' coefficient is ' + str(coeff))
print('the ' + str(terms) + ' coefficient is 1')