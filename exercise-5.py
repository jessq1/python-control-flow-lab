# exercise-05 Fibonacci sequence for first 50 terms

# Write the code that:
# 1. Calculates and prints the first 50 terms of the fibonacci sequence.
# 2. Print each term and number as follows:
#      term: 0 / number: 0
#      term: 1 / number: 1
#      term: 2 / number: 1
#      term: 3 / number: 2
#      term: 4 / number: 3
#      term: 5 / number: 5
#      etc.

# Hint: The next number is found by adding the two numbers before it

term = 0
firstTerm = 1
secondTerm = 1
while term<=50:
    if term<2:
        print(f"term: {term} / number: {term}")
    elif term==2:
        print(f"term: {term} / number: {secondTerm}")
    else:
        num = firstTerm + secondTerm
        print(f"term: {term} / number: {num}")
        firstTerm = secondTerm
        secondTerm = num
    term += 1