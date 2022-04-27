player1 = input("Enter a name for player 1: ")
player2 = input('Enter a name for player 2: ')
move_num = range(0,10)
a = [1,2,3,4,5,6,7,8,9]
game_list = [
        [a[0],a[1],a[2]],
        [a[3],a[4],a[5]],
        [a[6],a[7],a[8]]
    ]
def print_grid():
    for row in range(0,3):
        for column in range(0,3):
            if (column+1) % 3 != 0:
                print(game_list[row][column], end =" | ")
            else:
                print(game_list[row][column], end= '\n')
                my_string = ''
                for i in range(0,9):
                    my_string += '-'
                print(my_string)
def is_square_available(num):
    if game_list[(num-1)//3][(num-1)%3] == num:
        return True
    else:
        return False
def make_move(num,player):
    global game_list
    if is_square_available(num) is True:
        if player == 1:
            game_list[(num-1)//3][(num-1)%3] = 'X'
        elif player == 2:
            game_list[(num-1)//3][(num%3)-1] = 'O'
    else:
        new_square = int(input("You can't go there, pick a new square "))
        while is_square_available(new_square) is False:
            next_square = int(input("You can't go there, pick a new square "))
            if is_square_available(next_square) is True:
                if player == 1:
                    game_list[(next_square-1)//3][(next_square-1)%3] = 'X'
                    break
                elif player == 2:
                    game_list[(next_square-1)//3][(next_square%3)-1] = 'O'
                    break
        if is_square_available(new_square) is True:
            if player == 1:
                game_list[(new_square-1)//3][(new_square-1)%3] = 'X'
            elif player == 2:
                game_list[(new_square-1)//3][(new_square%3)-1] = 'O'
def is_board_full():
    # Used Google to find how to count the number of times an element appears in a nested list
    if sum(x.count('X') for x in game_list) + sum(x.count('O') for x in game_list) == 9:
        return True
    else:
        return False
def is_win():
    if game_list[0][0]==game_list[0][1]==game_list[0][2] or game_list[1][0]==game_list[1][1]==game_list[1][2] or game_list[2][0]==game_list[2][1]==game_list[2][2] or game_list[0][0]==game_list[1][0]==game_list[2][0] or game_list[0][1]==game_list[1][1]==game_list[2][1] or game_list[0][2]==game_list[1][2]==game_list[2][2] or game_list[0][0]==game_list[1][1]==game_list[2][2] or game_list[0][2]==game_list[1][1]==game_list[2][0]:
        return True
    else:
        return False
def game_loop():
    global game_list
    while is_board_full() is False:
        if is_win() is False:
            print_grid()
            one_action = int(input(f"Choose a number for the square you wish to place your mark in {player1}: "))
            make_move(one_action,1)
            if is_win() is True:
                print_grid()
                print(f"{player1} wins")
                break
        if is_win() is False:
            print_grid()
            if is_board_full() is False:
                two_action = int(input(f"Choose a number for the square you wish to place your mark in {player2}: "))
                make_move(two_action,2)
                if is_win() is True:
                    print_grid()
                    print(f"{player2} wins")
                    break
            elif is_board_full() is True:
                print("It was a tie")
                break
game_loop()






