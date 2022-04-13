'''
##########
Lab 4.05
##########

1. Read through the following code
    def print_numbers(list):
        for i in range(1, len(list)+1):
            print(list[i])
​
    num_list = [1, 2, 3, 4, 5, 6]
    print_numbers(num_list)
In your notebook
Write down any bugs that you see in the program. We need range(0,len(list)) to not be out of range

2. Read through the following code
    def swapping_stars():
    line_str = ""
        for line in range(0, 6):
            for char in range(0,6):
                if line % 2 == char % 2:
                    line_str += "*"
                else:
                    line_str += "-"
    print(line_str)
Continue in your notebook
Write down any bugs that you see in the program. Since it starts and ends with an odd number, every 5th character from the start will have two -- or ** since we check if the numbers are even or odd with %

3. In script mode
Fix the 2 programs above.
Create a program that asks the user which function they would like to run.
'''

def print_numbers(list):
    for i in range(0, len(list)):
        print(list[i])
num_list = [1, 2, 3, 4, 5, 6]
def swapping_stars():
    line_str = ""
    for line in range(0, 7):
        for char in range(0,7):
            if line % 2 == char % 2:
                    line_str += "*"
            else:
                    line_str += "-"
    print(line_str)
def action():
    action_num = int(input("Choose '1' for print_numbers and '2' for swapping stars: "))
    if action_num == 1:
        print_numbers(num_list)
    elif action_num == 2:
        swapping_stars()
    else:
        print("Invalid input, try again")
action()






