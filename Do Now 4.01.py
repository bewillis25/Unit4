'''
Do Now 4.01

1. In your console
Type the following Code
    single_fruit = ['apple', 'banana', 'watermelon', 'grape']
    multi_fruit = []
    multi_fruit.append(single_fruit[0] + 's')
    multi_fruit.append(single_fruit[1] + 's')
    multi_fruit.append(single_fruit[2] + 's')
    multi_fruit.append(single_fruit[3] + 's')
    print(multi_fruit)

In your notebook
Respond to the following
Briefly write down what happened. What would happen if you added 100 items to the list single_fruit? We create an empty list multi_fruit to which we add the single_fruit elements, but with an 's' at the end of each. If we added 100 items, we would have to add 100 more lines for multi_fruit adding 's' to 100 new elements of single_fruit.
Write down how you would update multi_fruit.

2. In your console
Type the following
    list_of_numbers = [3, 5, 10, 23]
    for num in list_of_numbers:
        print(f"num is {num}")
        
Continue in your notebook
Respond to the following
Briefly write down what happened. How would this change if you added 100 items to list_of_numbers? It prints out "num is {num}" for each elements in list_of numbers. If we added 100 items to the list, it would automatically update and print out those 100 extra items as well.

3. In your console
Rewrite the code from part 1 using knowledge from part 2.
'''
# multi_fruit list 
single_fruit = ['apple','banana','watermelon','grape']
multi_fruit = []
for item in single_fruit:
    multi_fruit.append(item + 's')
print(multi_fruit)



