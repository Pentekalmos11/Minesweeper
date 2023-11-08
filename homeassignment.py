import random
import copy
import string

print('hello')

def main_game():
    valid_number = True

    while valid_number:
        try:
            size = int(input('How big the board should be? maximum value(10): '))
            maximum_number_of_bombs = round((size*size)/2)
        except ValueError:
             print("Make sure you entered a number")
        if size < 11 and size>0: 
                 valid_number = False
        else: print('Give a valid number please')



    valid_bombs = True
    while valid_bombs:
        try:
            print(f'How many bomb should be placed?\nIt can be more than: {maximum_number_of_bombs}' )        
            bombs = int(input('Number of bobms:'))
        except ValueError:
             print("Make sure you entered a number") 
        if bombs<=maximum_number_of_bombs:
             valid_bombs = False
        else: print("\nIt's not correct! Give a valid number please")

    row_labels = list(string.ascii_lowercase)
    header= ['  ', '1', '2', '3', '4','5','6','7','8','9','10']



    length = size
    mine_positions = set() # I can store the bombs's position because set only stores unique elements


    #create the table
    visible_board = []
    for i in range(length):
        row=[]
        for value in range(length):
            row.append('X')
        visible_board.append(row)


    def print_visible_board():
        #add header
        for label in range(size+1):
            print(header[label], end=' ')
        print()
        #add row labels and print visible_board
        for i, row in enumerate(visible_board):
            print(row_labels[i] + ': ' + ' '.join(row))

    # I create an other board to store the bombs's position
    invisible_board = copy.deepcopy(visible_board)



    # create the bombs until the len(mine_positions) reach the len(bombs)
    while len(mine_positions) < bombs:
        x, y = random.randint(0, size-1), random.randint(0, size-1) # Due to the zero index I must deduct 1 from size
        mine_positions.add((x, y))
        invisible_board[x][y] = 'B'   # for example: invisible board[0][4] --> that means I place a bomb in the first row, fifth column


    def print_invisible_board():
        # print the invisible board to make sure the bombs are placed
        for label in range(size+1):
            print(header[label], end=' ')
        print()  
        for i, row in enumerate(invisible_board):
            print(row_labels[i] + ': ' + ' '.join(row))


    

    print_visible_board()

    print('-'*10)

   # print_invisible_board()  # just for testing the code


    revealed_fields = 0
    safe_fields = size*size-bombs

    while True:
            number_of_bomb = 0
            user_input = input("What field to reveal? (e.g., B3): ").strip().lower()
            if len(user_input) !=2:
                print("Give a valid field")

            else: row, col = user_input[0], int(user_input[1]) - 1

            #  label index give me the index of the charachter 
            label_index = row_labels.index(row)

            if visible_board[label_index][col] != 'X':
                print("Field already revealed.")
                continue

            if invisible_board[label_index][col] == 'B':
                print('you lose')
                break
                
            # def count_bombs_around(row, col, invisible_board, size):
            #     bomb_count = 0
            #     for r in range(max(0, row-1), min(row+2, size)):
            #         for c in range(max(0, col-1), min(col+2, size)):
            #             if invisible_board[r][c] == 'B':
            #                 bomb_count += 1
            #     return bomb_count
                

            # I need to inspect if the given input's neighbor has a bomb
            try:
                if invisible_board[label_index-1][col] == 'B':  
                    number_of_bomb +=1
            except IndexError:
                    pass
            try:
                if invisible_board[label_index+1][col] == 'B':  
                    number_of_bomb +=1
            except IndexError:
                    pass
            try:
                if invisible_board[label_index][col-1] == 'B':  
                    number_of_bomb +=1
            except IndexError:
                    pass
            try:
                if invisible_board[label_index][col+1] == 'B':  
                    number_of_bomb +=1
            except IndexError:
                    pass
            
            
            # number_of_bomb = count_bombs_around(label_index, col, invisible_board, size)

            if number_of_bomb > 0:
                visible_board[label_index][col] = str(number_of_bomb)
                print_visible_board()
                revealed_fields += 1
            else:  
                visible_board[label_index][col] = 'O'
                print_visible_board()
                revealed_fields += 1

                
            if revealed_fields == safe_fields:
                print("Congratulations! You've cleared all the safe spots!")
                break

            number_of_bomb =0
            
    replay = input("Play again? (y/n): ").strip().lower()
    if replay == 'y':
        main_game()

    




main_game()


    








