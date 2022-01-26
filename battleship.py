import string
import os 
import time
# implementing the Battleship game


grid = 5
class bcolors:
    MISS = '\u001b[30m'
    WARNING = '\033[93m'
    OKGREEN = '\033[92m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'


def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')


def init_board(grid):
    board_a = [['0' for _ in range(grid)] for _ in range(grid)]
    return board_a


def init_turns():
    valid = False
    turns = ''
    while not valid:
        turns = input("How many turns do you want to play (5-50)? ")
        try:
            int(turns)
            if 5 <= int(turns) <= 50:
                valid = True
            else:
                print("Invalid input! (must be between 5-50)")
        except ValueError:
            print("Invalid input! (must be between 5-50)**")
            pass
    return turns


def init_boats(boats, boats_size, board):
    coordinates_list = []
    for m in range(len(boats)):
        for n in range(boats[m+1]):
            imp = []
            theres_contact = True
            while theres_contact:
                imp = is_valid_coordinates(boats_size[m])
                theres_contact = is_there_contact(imp, board, grid)
                if theres_contact:
                    print("Boats can't contact by edge.")
            ship = {}
            for p in range(len(imp)):
                coordinate = (ord(imp[p][0].lower())-97, int(imp[p][1])-1)
                ship[(coordinate[0],coordinate[1])] = 'X'
                board[coordinate[0]][coordinate[1]] = 'X'
            clear_terminal()
            print_one_board(grid, board)
            coordinates_list.append(ship)
    return coordinates_list, board


def boats_deatils():
    boats = {1:1}
    boats_size = list(boats.keys())
    return boats, boats_size


def print_one_board(grid, board):
    letter = ord('A')
    for i in range(grid+1):
        if i == 0:
            txt = ' '
            for j in range(grid):
                txt += ' ' + str(j+1)
            print(txt)
        else:
            txt = chr(letter+i-1) + ' '
            for j in range(grid):
                if board[i-1][j] == 'X':
                    txt += f'{bcolors.OKGREEN}{board[i-1][j]} {bcolors.ENDC}'
                else:
                    txt += board[i-1][j] + ' '
            print(txt)


def print_tiles(i, grid, board, txt):
    letter = ord('A')
    txt += chr(letter+i) + ' '
    for j in range(grid):
        if board[i][j] == 'X' or board[i][j] =='0':
            txt += '0' + ' '
        else:
            if board[i][j] == 'H':
                txt += f'{bcolors.WARNING}{board[i][j]} {bcolors.ENDC}'
            elif board[i][j] == 'M':
                txt += f'{bcolors.MISS}{board[i][j]} {bcolors.ENDC}'
            else:
                txt += f'{bcolors.FAIL}{board[i][j]} {bcolors.ENDC}'
    return txt


def print_two_board(grid, board_a, board_b):
    for i in range(grid+2):
        if i == 0:
            txt = ''
            txt += 'Player 1'
            txt += '  '*(grid-4)
            txt += '     '
            txt += 'Player 2'
            print(txt)
        elif i == 1:
            txt = ' '
            for k in range(2):
                for j in range(grid):
                    txt += ' ' + str(j+1)
                txt += '     '
            print(txt)
        else:
            txt = ''
            txt += print_tiles(i-2, grid, board_a, txt)
            txt += '   '
            txt = print_tiles(i-2, grid, board_b, txt)
            print(txt)


#cordinate input + validation:
def is_valid_input_coordinates(imp):
    letters = [string.ascii_letters[i] for i in range(26, 26+grid)]
    valid = False
    if len(imp) == 2:
        if imp[0].upper() in letters:
            try:
                int(imp[1])
                if 0 < int(imp[1]) <= grid:
                    valid = True
            except ValueError:
                print("This didn't seem to be a valid coordinate.")
        else:
            print("This didn't seem to be a valid coordinate.")
    else:
        print('Coordinate must be 2 characters long: letter of row and number of col.')
    return valid


def is_valid_coordinates(size):
    imp = []
    valid = False
    while not valid:
        imp = input(f'Please give {size} coordinate(s) (A-{string.ascii_letters[25+grid]})(1-{grid}) separated by a space: ').split(' ')
        valids = []
        if len(imp) == size:
            for i in range(len(imp)):
                valids.append(is_valid_input_coordinates(imp[i]))
        else:
            print(f"You must give {size} coordinates.")
            valids.append(False)
        if False in valids:
            valid = False
        else:
            valid = True
    return imp


def is_there_contact(imp, board, grid):
    neighbors = set()
    for i in range(len(imp)):
        for j in range(len(imp)):
            coordinate = (ord(imp[j][0].lower())-97, int(imp[j][1])-1)
            if coordinate[0] != 0:
                upper = (coordinate[0]-1, coordinate[1])
                neighbors.add(board[upper[0]][upper[1]])
            if coordinate[0] != grid-1:
                lower = (coordinate[0]+1, coordinate[1])
                neighbors.add(board[lower[0]][lower[1]])
            if coordinate[1] != 0:
                left = (coordinate[0], coordinate[1]-1)
                neighbors.add(board[left[0]][left[1]])
            if coordinate[1] != grid-1:
                right = (coordinate[0], coordinate[1]+1)
                neighbors.add(board[right[0]][right[1]])
    if 'X' in neighbors:
        return True
    else:
        return False


def is_valid_shoot():
    imp = ''
    valid = False
    while not valid:
        imp = input(f'Try to shoot a boat, give me a coordinate (A-{string.ascii_letters[25+grid]})(1-{grid}))')
        valid = is_valid_input_coordinates(imp)
    return imp


def input_shoot():
    imp = is_valid_shoot()
    hit = (ord(imp[0].lower())-97, int(imp[1])-1)
    return hit


def check_ship(coordinates_list, hit):
    for ship in coordinates_list:
        if hit in ship:
            ship[hit[0],hit[1]] = 'H'
            return ship


def is_sunk(ship):
    ship_set = list(ship.values())
    return not 'X' in ship_set


def sunk_parts(ship):
    sunk = list(ship.keys())
    return sunk


def mark_shoot_on_board(board, hit, coordinates_list):
    if board[hit[0]][hit[1]] == 'X':
        board[hit[0]][hit[1]] = 'H'
        ship = check_ship(coordinates_list, hit)
        if is_sunk(ship):
            sunk = sunk_parts(ship)
            coordinates_list.remove(ship)
            for tile in sunk:
                board[tile[0]][tile[1]] = 'S'
    elif board[hit[0]][hit[1]] == '0':
        board[hit[0]][hit[1]] = 'M'


def is_win(coordinates_list, player):
    win = len(coordinates_list) == 0
    return win, player

if __name__ == '__main__':
    try:
        clear_terminal()
        boats, boats_size = (boats_deatils())
        print(f"{bcolors.FAIL}Player 2's turn.{bcolors.ENDC}")
        board_a = init_board(grid)
        print_one_board(grid, board_a)
        coordinates_list_a, board_a = init_boats(boats, boats_size, board_a)
        # waiting screen 'Next player's placement phase' is displayed til pressing any button
        time.sleep(3)
        clear_terminal()
        print(f"{bcolors.FAIL}Player 2's turn.{bcolors.ENDC}")
        board_b = init_board(grid)
        print_one_board(grid, board_b)
        coordinates_list_b, board_b = init_boats(boats, boats_size, board_b)
        time.sleep(3)
        clear_terminal()
        turns = int(init_turns())
        clear_terminal()
        won = False
        winner = ''
        while turns > 0 or not won:
            print(f"{bcolors.FAIL}Turns left: {turns}{bcolors.ENDC}")
            print(f"Player 1's turn.")
            print_two_board(grid, board_a, board_b)
            hit = input_shoot()
            mark_shoot_on_board(board_b, hit, coordinates_list_b)
            print_two_board(grid, board_a, board_b)
            won, winner = is_win(coordinates_list_b, '1')
            if won:
                break
            clear_terminal()

            print(f"{bcolors.FAIL}Turns left: {turns}{bcolors.ENDC}")
            print(f"Player 2's turn.")
            print_two_board(grid, board_a, board_b)
            hit = input_shoot()
            mark_shoot_on_board(board_a, hit, coordinates_list_a)
            print_two_board(grid, board_a, board_b)
            won, winner = is_win(coordinates_list_a, '2')
            if won:
                break
            clear_terminal()
            turns += -1
        if won:
            print(f'Player {winner} wins!')
        if turns == 0:
            print("No more turns, it's a draw! ")
    except KeyboardInterrupt:
        print('Goodbye...')
