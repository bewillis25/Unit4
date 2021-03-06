'''
##########
Lab 4.02
##########

Part 1
----------
Write a function pluralize_words that takes in a list of words and updates the values of the list 
to make each one plural. It returns nothing.

Making plurals in English has a number of special cases, but for this lab we'll use a simple rule: 
if the word ends in a y remove the y and add ies; otherwise add an 's'.

We'll exercise the function on a list of words.

Create the function contract for pluralize_words.

Provide a few examples that confirm pluralize_words works as expected:

    Include examples with 'berry'

    What if the list is empty?

Example 1
----------
    # contract goes here
    def pluralize_words(word_list):
        # your code goes here
​
    word_list = ['apple', 'berry', 'melon']
    print(f"Singular words: {word_list}")
    pluralize_words(word_list)
    print(f"No longer singular words: {word_list}")
    # more examples go here

#######################################################
Here is what it should look like when you run your code:
#######################################################
Singular words: ['apple', 'berry', 'melon']
No longer singular words: ['apples', 'berries', 'melons']

Hint
-----
Remember that you can index into the string and get the length of a string. Use that to get the last letter of each word.

Part 2
------
Create a function my_reverse, which will return a reversed string.

Create the function contract for my_reverse.

Provide a few examples to confirm that my_reverse works:

    An empty string

    A string of even length

    A string of odd length greater than 1

    A string of length 1

Example 2
---------
    # contract goes here
    def my_reverse(string_to_reverse):
        # your code goes here
​
    reversed = my_reverse("apples")
    print(reversed)
    # examples go here

##############################################################
Here is what example 2 should look like when you run your code:
##############################################################
    selppa

Hint 2
------
To get the last element:(len(my_list) -1) - 0 
To get the second to last element: (len(my_list)-1 ) - 1 
To get the third to last element: (len(my_list)-1) - 2

Extension
---------
Create a function reverse_strings_in_list. This function will input a list of strings you want to reverse. 
The function will reverse the strings in the list by calling the my_reverse function in a loop.
'''

# Takes in a word list and pluralizes each word
def pluralize_words(word_list):
    new_list = []
    for item in word_list:
        if item[-1] != 'y':
            new_list.append(item + 's')
        else:
            new_item = item.replace("y","ies")
            new_list.append(new_item)
    print(new_list)
fruit_list = ['apple', 'berry','melon']
pluralize_words(fruit_list)


# Takes in a string moves the nth letter to the len(string)-n position (a negative means go backward, as in list indexing)
def my_reverse(word):
    # First argument in slice is the starting point, which is the last item of the string
    # Then, the slice goes backward one position and repeats until it gets to the stopping point, the second argument, which it will stop BEFORE
    # So, it will stop before [-6], i.e. end with [0] which is the first item of the string
    return word[len(word)-1:-len(word)-1:-1]

# Takes in a list with strings that will be reversed
def reverse_strings_in_list(string_list):
    new_list = []
    for item in string_list:
        new_list.append((my_reverse(item)))
    print(new_list)
fruit_list = ['milk', 'berry','melon']
reverse_strings_in_list(fruit_list)













