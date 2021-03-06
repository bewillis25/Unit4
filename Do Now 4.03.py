'''
#############
Do Now 4.03
#############

Type in your console:
----------------------
    def print_6_stars():
        my_string = ''
        for i in range(0, 6):
            my_string += ' *'
        print(my_string)

In your notebook
-----------------
Write down what the output of the function print_6_stars is.

Write a function  print_star_square that calls print_6_stars in a loop to produce the following output.

    >>>python print_stars.py
    * * * * * *
    * * * * * *
    * * * * * *
    * * * * * *
    * * * * * *
    * * * * * *

    # write you code for this function below:
    def print_star_square():
        #your code goes here

Rewrite the function print_star_square without using print_6_stars.
    # write you code for this function below:
        def print_star_square():
            #your code goes here

Note that there are two ways (at least) to get the above output, so just try doing both!
'''
# Makes a horizontal line of 6 stars
def print_6_stars():
        my_string = ''
        for i in range(0, 6):
            my_string += ' *'
        print(my_string)

# Makes a 6x6 square out of stars
def print_star_square():
    string = ''
    for i in range(0,6):
        string += f'{print_6_stars()} \n'

def print_star_square2():
    string = ' *'*6
    new_string = ''
    new_string += f'{string}\n'*6
    print(new_string)
print_star_square2()
















