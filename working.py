# rules of the game
# objective: capture more stones than the opponent
# 1. four pieces are places in each of the 12 holes initially
# 2. each player has a mancala (the larger holes)
# 3. the game begins with one player picking up all the pieces in any of the holes on their side
# 4. moving counter-clockwise, the player deposits one of the stones in each hole until the stones run out
# 5. if you run into your own store, deposit one piece in it. if you run into your opponent's store, skip it
# 6. if the last piece you drop is in your own store, you get a free turn
# 7. if the last piece you drop is in an empty hole on your side, you capture that piece and any pieces in the hole directly opposite
# 8. always place all captured pieces in your store
# 9. the game ends when all six spaces on one side of the Mancala board are empty
# 10. the player who still has pieces on his side of the board when the game ends capture all of those pieces

# configurable settings --------------------------
num_holes_pp = 6
start_num_pieces = 4
# ------------------------------------------------
num_holes = num_holes_pp * 2


def print_board(board):
    print("- - - - - - - - - - - -")
    print("|         ", board[get_player_hole(2)], "          |")
    print("| - - - - - - - - - - -|")
    for i in range(int((len(board) - 2) / 2)):
        print("|(", i + 1, ")", board[i + 1], "    ", board[len(board) - i - 1], "(", len(board) - i - 2, ")|")
    print("| - - - - - - - - - -|")
    print("|         ", board[get_player_hole(1)], "        |")
    print("- - - - - - - - - - -")


def init_board():
    board = [start_num_pieces for i in range(num_holes + 2)]
    board[get_player_hole(1)] = 0
    board[get_player_hole(2)] = 0
    return board


def get_player_hole(num):
    return int((num % 2) * (num_holes / 2 + 1))


def check_valid_move(player, hole_num, board):
    if (player == 1 and hole_num > num_holes / 2) or (player == 2 and hole_num <= num_holes / 2):
        print("invalid move, choose a hole on your side")
        return False
    if board[convert_to_index(hole_num)] <= 0:
        print("invalid move, choose a non-empty hole")
        return False
    return True


def convert_to_index(num):
    # numbers 1,2,3,4,5,6 / 7,8,9,10,11,12 to 1,2,3,4,5,6 / 8,9,10,11,12,13
    return (num + 1 if num > num_holes_pp else num) % (num_holes + 2)


def prompt_new_move(player, board):
    hole_choice = int(input("Player " + str(player) + ", make your move: "))

    if hole_choice < 1 or hole_choice > num_holes:
        print("invalid input, please choose another number!")
        prompt_new_move(player, board)
        return
    else:
        make_move(player, hole_choice, board)
        return


def make_move(player, hole_num, board):
    if check_valid_move(player, hole_num, board):
        curr_hole = convert_to_index(hole_num)
        mov_index = curr_hole
        for i in range(board[mov_index]):
            mov_index += 1
            mov_index %= num_holes + 2
            if mov_index == get_player_hole(player + 1):
                mov_index += 1
                mov_index %= num_holes + 2
            board[mov_index] += 1
        board[curr_hole] = 0
        if not is_game_over(board):
            check_special_moves(player, mov_index, board)
        return
    else:
        prompt_new_move(player, board)
        return


def check_special_moves(player, curr_index, board):
    if curr_index == get_player_hole(player):
        print("yay! you get another turn!")
        print_board(board)
        prompt_new_move(player, board)
        return
    elif board[curr_index] == 1:
        print("yay! you get all the stones in the opposite hole!")
        board[get_player_hole(player)] += board[len(board) - curr_index]
        board[len(board) - curr_index] = 0
        return


def is_game_over(board):
    status_1 = True
    status_2 = True

    # check if one side of holes is empty
    for i in range(int(num_holes / 2)):
        j = i + int(num_holes / 2) + 2
        if board[i + 1] != 0:
            status_1 = False
        if board[j] != 0:
            status_2 = False

    # shift the rest of the stones if needed
    if status_1:
        for x in range(int(num_holes / 2)):
            j = x + int(num_holes / 2) + 2
            board[get_player_hole(2)] += board[j]
            board[j] = 0
    if status_2:
        for y in range(int(num_holes / 2)):
            board[get_player_hole(1)] += board[y + 1]
            board[y + 1] = 0

    return status_1 or status_2


def get_winner(board):
    return 1 if board[get_player_hole(1)] > board[get_player_hole(2)] else 2


def main():
    this_board = init_board()
    print_board(this_board)
    print("New Mancala Game! Player 1 please make your move!")
    curr_player = 1

    while not is_game_over(this_board):
        prompt_new_move(curr_player, this_board)
        print_board(this_board)
        curr_player = 2 if curr_player == 1 else 1

    if this_board[get_player_hole(1)] == this_board[get_player_hole(2)]:
        print("Game over! It is a draw!")
    else:
        print("Game over! Player " + str(get_winner(this_board)) + " won!")
    print_board(this_board)


main()
