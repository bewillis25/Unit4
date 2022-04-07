'''
###########
Lab 4.03
###########

Instructions
In this lab we will be drawing images using nested for loops.

For each of the following problems, you will write a function that will draw the desired output. You may use an extra function if you find it helpful.

1.  Write a function, draw_7, to draw the 7x7 square (shown below)

    * * * * * * *
    * * * * * * *
    * * * * * * *
    * * * * * * *
    * * * * * * *
    * * * * * * *
    * * * * * * *
2.  Write a function stars_and_stripes, that will draw a 3 sets of rows. 1st a row of 7 stars followed by a row of 7 dashes (shown below)

    * * * * * * *
    - - - - - - -
    * * * * * * *
    - - - - - - -
    * * * * * * *
    - - - - - - -
3.  Write a function, increasing_triangle that will print out the following:

    1
    1 2
    1 2 3
    1 2 3 4
    1 2 3 4 5
    1 2 3 4 5 6
    1 2 3 4 5 6 7

4. Write a function, vertical_stars_and_stripes that will print out the following:

    - * - * - * -
    - * - * - * -
    - * - * - * -
    - * - * - * -
    - * - * - * -
    - * - * - * -
    - * - * - * -

5.  Use a function to create your own pattern or drawing. Some possible pattern ideas:

    Write a function that will print a border around a 7x7 square (shown below)

        * * * * * * * *
        * - - - - - - *
        * - - - - - - *
        * - - - - - - *
        * - - - - - - *
        * - - - - - - *
        * - - - - - - *
        * - - - - - - *
        * * * * * * * *
    Write a function that will print the following balanced_triangle.

        1
        1 2
        1 2 3
        1 2 3 4
        1 2 3 4 5
        1 2 3 4 5 6
        1 2 3 4 5 6 7
        1 2 3 4 5 6
        1 2 3 4 5
        1 2 3 4
        1 2 3
        1 2
        1
    Write a function that will print the following triangle.

        *
        ***
        *****
    
'''

# Makes a line of 7 stars
def draw_7_line():
        my_string = ''
        for i in range(0, 7):
            my_string += ' *'
        print(my_string)
# Makes a 7x7 square
def draw_7():
    string = ''
    for i in range(0,7):
        string += f'{draw_7_line()} \n'

# Draws a line of stars then below it a line of stripes
def stars_and_stripes():
    my_string2 = ''
    my_string = ''
    for i in range(0,6):
        my_string2 += ' *'
    for i in range(0,6):
        my_string += ' -'
    print(my_string2)
    print(my_string)
# Repeats the above loop three times
def three_rows_stars_and_stripes():
    string = ''
    for i in range(0,3):
        string += f'{stars_and_stripes()} \n'

# Makes a triangle with increasing numbers per row
def increasing_number_triangle(num):
    for i in range(0,num + 1):
        for j in range(0,i+1):
            # Used google to find the end='' function in order to print 1234, etc. without going down a line each iteration
            print(j+1, end='')
        print()

# Same as stars_and_stripes() but vertical
def row_one_vertical_stars_and_stripes():
    string1 = ''
    string2 = ''
    for i in range(0,6):
        if i%2 == 0:
            string1 = ' -'
        else:
            string2 = ' *'
    print(3*(string1+string2))
def n_rows_vertical_stars_and_stripes(num):
    string = ''
    for i in range(0,num):
        string += f'{row_one_vertical_stars_and_stripes()} \n'

# Increasing triangle of asterisks with odd number per row
def increasing_star_triangle(num):
    for i in range(0,num):
            print('*'*(2*i+1))


        















