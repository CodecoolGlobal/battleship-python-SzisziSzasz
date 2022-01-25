import string
# implementing the Battleship game


#print board:
grid = 5
class bcolors:
    WARNING = '\033[93m'
    OKGREEN = '\033[92m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

def init_board(grid):
    board_a = [['0' for _ in range(grid)] for _ in range(grid)]
    return board_a

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
    txt += chr(letter+i-1) + ' '
    for j in range(grid):
        if board[i-1][j] == 'X' or board[i-1][j] =='0':
            txt += '0' + ' '
        else:
            if board[i-1][j] == 'H':
                txt += f'{bcolors.WARNING}{board[i-1][j]} {bcolors.ENDC}'
            else:
                txt += f'{bcolors.FAIL}{board[i-1][j]} {bcolors.ENDC}'
    return txt

def print_two_board(grid, board_a, board_b):
    for i in range(grid+1):
        if i == 0:
            txt = ' '
            for k in range(2):
                for j in range(grid):
                    txt += ' ' + str(j+1)
                txt += '     '
            print(txt)
        else:
            txt = ''
            txt += print_tiles(i, grid, board_a, txt)
            txt += '   '
            txt = print_tiles(i, grid, board_b, txt)
            print(txt)

#print board

#input:

def boats_deatils():
    boats = {1:3, 2:3}
    boat_size = list(boats.keys())
    return boats, boat_size
    

def is_valid_coordinates(letters):
    imp = []
    valid = False
    while not valid:
        imp = list(input(f'Please give a coordinate (A-{string.ascii_letters[25+grid]})(1-{grid})'))
        if len(imp) == 2:
            if imp[0].upper() in letters and 0 < int(imp[1]) <= grid:
                valid = True
            else:
                print("This didn't seem to be a valid coordinate.")
                pass
        else:
            print('Coordinate must be 2 characters long: letter of row and number of col.')
    return imp


def boats_init(boats, boat_size, board):
    coordinates_list = []
    print = f'This is a {boats}, you have to give {boat_size} coordinates'
    letters = [string.ascii_letters[i] for i in range(26, 26+grid)]
    for m in range(len(boats)):
        for n in range(boats[m+1]):
            ship = []
            for p in range(boat_size[m]):
                imp = is_valid_coordinates(letters)
                coordinate = (ord(imp[0].lower())-97, int(imp[1])-1)
                ship.append(coordinate)
                board[coordinate[0]][coordinate[1]] = 'X'
                print_one_board(grid, board)
            coordinates_list.extend(ship)
    return coordinates_list

# def is_it_too_close(coordinates_list,board):
#     for n in range(len(coordinates_list)):
        

[]
boats, boat_size = (boats_deatils())
board_a = init_board(grid)
# boats_init(boats, boat_size, board_a)
cordinates_list = (boats_init(boats,boat_size,board_a))
print(is_it_too_close(cordinates_list,board_a))

    