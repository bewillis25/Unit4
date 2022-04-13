'''
############
Lab 4.04
############

Part 1
-----------
The goal of this lab is to practice using and accessing items from lists of lists.

You have a few errands to run and have created a few shopping lists to help you remember what to buy. 
You stored your notes in a nested list, shopping_cart. This program will allow the user to ask for a 
specific item by its index or update what items are in the cart. The user can request to view list to 
see the items in a specific shopping list.

Shopping Lists
    shopping_lists = [
        ['toothpaste', 'q-tips', 'milk'],
        ['milk', 'candy', 'apples'],
        ['planner', 'pencils', 'q-tips']
    ]
User Inputs
1 - Update

The program asks which shopping list the user wants to update, which position it should update, and the new value to update.

2 - View Item

The program asks which shopping list the item is on and which position it occupies, then prints the item's name.

3 - View List

The program asks which shopping list the user wants and prints all of the items associated with that shopping list.

Functions
update_list

Takes in an integer representing the index of the shopping list, an integer representing the index of the item to update, and a string representing the new value for that item. Does not alter the length of the list.

print_item

Takes an int representing the index of the shopping list followed by an int representing the index of the item to print.

print_list

Takes an int representing the index of the shopping list to print.

Feel free to add more functions as you see fit.

Example
    >>> Choose 1 = update item, 2 = view item, or 3 = view list: 1
    Which shopping list would you like to update? 1
    Which item would you like to change? 2
    New value for item #2? cheese
    toothpaste, cheese, milk
    >>> Choose 1 = update item, 2 = view item, or 3 = view list: 2
    Which shopping list do you want to choose? 2
    Which item on list #2 do you want to see? 3
    apples
    >>> Choose 1 = update item, 2 = view item, or 3 = view list: 3
    Which shopping list would you like to see? 3
    planner, pencils, q-tips

Part 2
------------
In this part of the lab you will go through your shopping list program and perform a few different calculations.

Create a function, all_in_one, that will put all the shopping lists into a single combined list using a for loop.

Create a function, count_q_tips, which will go through all items of the list and keep a count of how many times 
'q-tips' occurs.

In order to make the shopping lists more calcium rich, write a function, drink_more_milk, that adds 'milk' to each 
of the lists (unless it's already there).

You can't have milk without cookies. Write a function if_you_give_a_moose_a_cookie, that will go through every 
element of shopping_cart and update 'milk' to be 'milk and cookies'.

Extension
-------------
Write a function to reverse the order of the lists, and also reverse the order of the items in each list, in the shopping_cart nested list.

The new reversed list should look like the following when printed (newlines and spacing added for clarity):

    shopping_cart = [
        ['q-tips', 'pencils', 'planner'],
        ['apples', 'candy', 'milk'],
        ['milk', 'q-tips', 'tooth paste']
    ]
Tip
Last item can be gotten by my_list[-1]

Second to last element: my_list[-2]

Third to last element: my_list[-3]
'''



shopping_lists = [
        ['toothpaste', 'q-tips', 'milk'],
        ['milk', 'candy', 'apples'],
        ['planner', 'pencils', 'q-tips']
    ]
new_list = []
# Takes in the list and the item and replaces it with what the user wants
def update_list():
        list_num = input("Which shopping list would you like to update? ")
        item_num = input("Which item would you like to change? ")
        string = input(f"New value for item #{item_num}? ")
        shopping_lists[int(list_num)-1][int(item_num)-1] = string
        print(shopping_lists[int(list_num)-1])
# Prints any item the user chooses out of the three lists
def print_item():
        list_num = input("Which list would you like to see? ")
        item_num = input(f"Which item of list {int(list_num)-1} do you want to see? ")
        print(shopping_lists[int(list_num)-1][int(item_num)-1])
# Prints out any of the three lists the user wants
def print_list():
        list_num = input("Which list would you like to see? ")
        print(shopping_lists[int(list_num)-1])
# Gets users input for what they want to do with the shopping list
def select_action():
    action_num = input("Choose 1 = update item, 2 = view item, or 3 = view list: ")
    if int(action_num) == 1: 
        update_list()
    elif int(action_num) == 2:
        print_item()   
    elif int(action_num) == 3:
        print_list()
# Takes in the 3 lists and makes a new list combining them
def all_in_one():
    global new_list
    for i in range(0,3):
        new_list += shopping_lists[i]
# Goes throught the all_in_one list to see how may times q-tips shows up
def count_q_tips():
    counter = 0
    global new_list
    all_in_one()
    for item in new_list:
        if item == 'q-tips':
            counter += 1
    print(f"There are {counter} q-tips in your shopping list")
# Adds milk to any shopping list that doesn't already have it
def drink_more_milk():
    for i in range(0,3):
        if 'milk' in shopping_lists[i]:
            pass
        else:
            shopping_lists[i].append('milk')
    print(shopping_lists)
# Replaces 'milk' with 'milk and cookies' 
def if_you_give_a_moose_a_cookie():
    global shopping_lists
    for i in range(0,3):
        for j in range(0,3):       
            if shopping_lists[i][j] == 'milk':
                shopping_lists[i][j] = 'milk and cookies'
    print(shopping_lists)
# Reversed the nested list and its values
def reverse_list():
    new_list = []
    for i in range(0,3):
        reversed_nested_list = shopping_lists[::-1]
        new_list += reversed_nested_list[i][::-1]
    print(new_list)














