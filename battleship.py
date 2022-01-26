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

#boats_details:

def boats_deatils():
    boats = {1:3, 2:3}
    boats_size = list(boats.keys())
    return boats, boats_size

#boats_deatils

#cordinate input + validation:

def is_valid_coordinates(size):
    letters = [string.ascii_letters[i] for i in range(26, 26+grid)]
    imp = []
    valid = False
    while not valid:
        imp = input(f'Please give {size} coordinates (A-{string.ascii_letters[25+grid]})(1-{grid}) separated by a space: ').split(' ')
        valids = []
        if len(imp) == size:
            for i in range(len(imp)):
                if len(imp[i]) == 2:
                    if imp[i][0].upper() in letters:
                        try:
                            0 < int(imp[i][1]) <= grid
                            valids.append(True)
                        except ValueError:
                            print("This didn't seem to be a valid coordinate.")
                            valids.append(False)
                    else:
                        print("This didn't seem to be a valid coordinate.")
                        valids.append(False)
                        pass
                else:
                    print('Coordinate must be 2 characters long: letter of row and number of col.')
                    valids.append(False)
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

#comment input + validation

#change 0-X:

def boats_init(boats, boats_size, board):
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
                ship[f'{coordinate[0]},{coordinate[1]}'] = 'X'
                board[coordinate[0]][coordinate[1]] = 'X'
                print_one_board(grid, board)
            coordinates_list.append(ship)
    return coordinates_list

#change O-X
# waiting screen 'Next player's placement phase' is displayed til pressing any button


#input shoot:

def is_valid_shoot():
    letters = [string.ascii_letters[i] for i in range(26, 26+grid)]
    imp = []
    valid = False
    while not valid:
        imp = input(f'Try to shoot a boat, give me a coordinate (A-{string.ascii_letters[25+grid]})(1-{grid}))')
        
        if len(imp) == 2:
            if imp[0].upper() in letters:
                try:
                    0 < int(imp[1]) <= grid
                    valid = True
                except ValueError:
                    print("This didn't seem to be a valid coordinate.")
            else:
                print("This didn't seem to be a valid coordinate.")
                pass
        else:
            print('Coordinate must be 2 characters long: letter of row and number of col.')
    return imp

def input_shoot(size):
    imp = is_valid_shoot()
    coordinate = (ord(imp[0].lower())-97, int(imp[1])-1)
    return coordinate

#input shoot

#test shoot:

# def test_shoot(board_a, imp):
#     if 


#test shoot

#change after shoot:

#change after shoot
        

[]
boats, boats_size = (boats_deatils())
board_a = init_board(grid)
# boats_init(boats, boat_size, board_a)
# cordinates_list = (boats_init(boats,boats_size, board_a))
# print(is_it_too_close(cordinates_list,board_a))
print(boats_init(boats, boats_size, board_a))
print(input_shoot(boats_size))
