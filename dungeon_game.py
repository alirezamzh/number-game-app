import random

# draw grid
# pick random location for the player
# pick random location for the exit door
# pick random location for the monster
# draw a player in the grid
# take input or movement
# move player, unless invalid move (past edges of grid)
# check for win/lose
# clear screen and random grid


cells = [
    (0, 0), (1, 0), (2, 0), (3, 0), (4, 0),
    (0, 1), (1, 1), (2, 1), (3, 1), (4, 1),
    (0, 2), (1, 2), (2, 2), (3, 2), (4, 2),
    (0, 3), (1, 3), (2, 3), (3, 3), (4, 3),
    (0, 4), (1, 4), (2, 4), (3, 4), (4, 4),
    
]
def get_location():
    monster = None
    door = None
    player = None
    
    return monster, door, player

def move_player(player, move):
    # get the player's location
    # if move == LEFT, x-1
    # if move == RIGHT, x+1
    # if move == UP, y-1
    # if move == DOWN, y+1 
    return player

def get_move(player):
    moves = ["LEFT", "RIGHT", "UP", "DOWN"]
    # if player's y==0, they can't move up
    # if player's y==4, they can't move down
    # if player's x==0, they can't move left
    # if player's x==4, they can't move right
    return moves
while True:
    print('welcome to the dungeon!')
    print("you're currently in room {}")  # fill with player position
    printO("you can move {}")  # fill with available moves
    print("enter `QUIQ` to quit")

    move = input("> ")
    move = move.upper()
    
    if move == 'QUIT':
        break

    # good move? change player position
    # bad move? don't change anything
    # on the door? they win
    # on the monster? they lose
    # otherwise, loop back around