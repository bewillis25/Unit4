'''
Lab 4.01

Remove the Vowels
Create a function, de_vowel, which will take a string as input and return a copy of that string with all the vowels removed. Otherwise, the string should be the same. 'Y' does not count as a vowel for the purposes of this function.

Create the function contract for de_vowel.

Write de_vowel using a for loop

Provide a few examples that confirm de_vowel works as expected:

What if the string is all vowels?

What if there are no vowels?

What if there is a mix of vowels and non-vowels and spaces?

What if some vowels are capitalized, e.g., the first letter in a sentence?

Example
Example of the file:

    # contract goes here
    def de_vowel(a_string):
        # your code goes here
​
    no_vowels = de_vowel("This sentence has no vowels")
    print(no_vowels)
    # examples go here
Example output:

    >>> python3 de_vowel_lab.py
    Ths sntnc hs n vwls
Bonus
Use a counter (variable you define outside of a loop to keep track of a value inside a loop) to create a function count_vowels.

count_vowels takes in a string and returns an int representing the number of vowels in the string.

Can you think of an alternate way to do complete this task without any loop or counter, by making use of your new de_vowel() function instead?
'''
# Removes all lower case vowels from a string and returns a copy of the de-voweld string
def de_vowel(word):
    vowels = ['a','e','i','o','u','A','E','I','O','U']
    for letter in vowels:
        word = word.replace(letter,"")
    print(word)

# Counts the number of vowels in a word
def count_vowels(word):
    vowels = ['a','e','i','o','u','A','E','I','O','U']
    counter = 0
    for i in range(9):
        if vowels[i] in word:
            counter += 1
    print(counter)

# For an alternate method, use the length of the word - the de_voweled word

        








