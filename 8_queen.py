import random

def create_board():
    board = [0] * 8

    for i in range(8):
        board[i] = [0] * 8

    for i in range(8):
        random_index = random.randint(0, 7)
        board[random_index][i] = 1 

    return board

def print_board(board):
    for i in range(8):
        print(board[i], end = '\n')
    print('\n')

def calculate_attack(board):
    total_attacks = 0
    
    for col in range(8):
        for row in range(8):
            if board[row][col] == 1:   # we dont have to check the cells without a queen which makes it faster
                attack = 0

                c = col

                for c in range(col + 1, 8):
                    if board[row][c] == 1:
                        attack += 1

                r = row 
                c = col 

                # bottom right diagonal
                while r < 7 and c < 7:
                    if board[r + 1][c + 1] == 1:
                        attack += 1
                    r += 1
                    c += 1

                r = row
                c = col

                # top right diagonal
                while r >= 0 and c < 7:
                    if board[r - 1][c + 1] == 1:
                        attack += 1
                    r -= 1
                    c += 1

                total_attacks += attack

    return total_attacks

def basic_hill_climb(board):
    curr = [row[:] for row in board] 
    a = calculate_attack(curr)

    while True:    # to make sure it does not stop running
        best_board = [row[:] for row in curr]   # storing the current board as the best one
        attack = a
        lowest = False    # a boolean variable to exit out of the loop

        for col in range(8):     # finding the queen
            q_row = 1000000
            for row in range(8):
                if curr[row][col] == 1:
                    q_row = row
                    break

            for row in range(8):  
                if row == q_row:    # skip this iteration if on the same row as queen
                    continue

                curr[q_row][col] = 0    # change
                curr[row][col] = 1

                b = calculate_attack(curr)

                if b < attack:    # compare
                    attack = b
                    best_board = [r[:] for r in curr]
                    lowest = True

                curr[row][col] = 0    # undo the changes to get back to the original board
                curr[q_row][col] = 1

        if lowest:
            curr = [r[:] for r in best_board]
            a = attack
        else:
            print(f"Local Minimum Reached. {a} attacks still remain")
            return curr
    
    
    
    
    # curr = board

    # a = calculate_attack(board)
    # if a == 0:
    #     return board

    # for col in range(8):
    #     for row in range(8):
    #         best_board = [row[:] for row in curr]
    #         if curr[row][col] == 1:
    #             q_row = row
    #             break

    #     lowest = 1000000000

    #     for row in range(8):
    #         if row == q_row:
    #             continue

    #         curr[q_row][col] = 0
    #         curr[row][col] = 1
    #         a = calculate_attack(curr)
            
    #         if a < lowest:
    #             lowest = a
    #             new_board = curr

    #     curr = new_board

    # if lowest == 0:
    #     return curr
    # else:
    #     return "Local minimum reached"


            # if curr[row][col] == 1:
            #     new_row = 0
            #     curr[row][col] = 0

            #     if new_row == row:
            #         new_row += 1
            #     curr[new_row][col] = 1
            #     boards.append(curr)

            #     b = calculate_attack(boards[i])
            #     if b == 0:
            #         return boards[i]
            #     if b < lowest:
            #         lowest = b
            #         new_board = boards[i]
            #     elif b == lowest:
            #         return "Local Minimum reached"

                
            # basic_hill_climb(new_board)


def random_restart(board):
    restarts = 0
    while True:
        board = create_board()
        result = basic_hill_climb(board)
        restarts += 1
        print("\n")
        if calculate_attack(result) == 0:
            print(f"Number of restarts: {restarts}")
            print_board(result)
            return result


board = create_board()

print_board(board)

a = basic_hill_climb(board)
for i in range(len(a)):
    print(a[i], end = '\n')

b = random_restart(board)
