# exercise-01 Vowel or Consonant

# Write the code that:
# 1. Prompts the user to enter a letter in the alphabet:
#      Please enter a letter from the alphabet (a-z or A-Z): 
# 2. Write the code that determines whether the letter entered is a vowel
# 3. Print one of following messages (substituting the letter for x):
#      - The letter x is a vowel
#      - The letter x is a consonant

# Hints:  Use the in operator to check if a character is in another string
#         For example, if some_char in 'abc':

alphabet = input('Please enter a letter from the alphabet (a-z or A-Z): ')
print(f'The user entered {alphabet}')
alphabetL = alphabet.lower()

if alphabetL in 'a e i o u':
    print(f'The letter {alphabet} is a vowel')
else:
    print(f'The letter {alphabet} is a consonant')