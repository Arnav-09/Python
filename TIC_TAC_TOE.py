#TIC TAC TOE

from IPython.display import clear_output

def display_board(board):
    clear_output()
    print(board[7]+'|'+board[8]+'|'+board[9])
    print(board[4]+'|'+board[5]+'|'+board[6])
    print(board[1]+'|'+board[2]+'|'+board[3])

def player_input():
    pinput='WRONG'
    while pinput=='WRONG':
        pinput=input("Choose one from 'X' or 'O': ")
        if pinput not in ('X','O'):
            pinput='WRONG'
    if pinput=='X':
        return ('X','O')
    else:
        return ('O','X')

def place_marker(board, marker, position):
    board[position]=marker

def win_check(board, mark):
    
    #for horizontal
    i=1
    for i in range(1,8):
        if board[i]==board[i+1]==board[i+2]==mark:
            return True
        else:
            i+=3
    
    #for vertical
    j=1
    for j in range(1,4):
        if board[j]==board[j+3]==board[j+6]==mark:
            return True
        else:
            i+=1
            
    #for diagonal
    if board[1]==board[5]==board[9]==mark or board[3]==board[5]==board[7]==mark:
            return True

import random

def choose_first():
    flip=random.randint(0,1)
    
    if flip==0:
        return 'Player1'
    else:
        return 'Player2'

def space_check(board, position):
    if board[position]==' ':
        return True

def full_board_check(board):
    if ' ' not in board:
        return True
    else:
        False

def player_choice(board):
    
    #position
    position='WRONG'
    while position=='WRONG':
        position=int(input('Enter a position from 1-9: '))
        if position not in [1,2,3,4,5,6,7,8,9]:
            position='WRONG'
            
    if space_check(board,position)==True:
        return position

def replay():
    
    play='WRONG'
    while play=='WRONG':
        play=input('Do you wish to play again (Y/N)? ')
        if play not in ('Y','N'):
            play='WRONG'
    
    if play=='Y':
        return True
    else:
        return False

print('Welcome to Tic Tac Toe!')

def game():
    while True:
        # Reset the board
        theBoard = [' '] * 10
        player1_marker, player2_marker = player_input()
        turn = choose_first()
        print(turn + ' will go first.')
        
        play_game = input('Are you ready to play? Enter Yes or No.')
        
        if play_game.lower()[0] == 'y':
            game_on = True
        else:
            game_on = False

        while game_on:
            if turn == 'Player 1':
                # Player1's turn.
                
                display_board(theBoard)
                position = player_choice(theBoard)
                place_marker(theBoard, player1_marker, position)

                if win_check(theBoard, player1_marker):
                    display_board(theBoard)
                    print('Player 1 has won!')
                    game_on = False
                else:
                    if full_board_check(theBoard):
                        display_board(theBoard)
                        print('The game is a draw!')
                        break
                    else:
                        turn = 'Player 2'

            else:
                # Player2's turn.
                
                display_board(theBoard)
                position = player_choice(theBoard)
                place_marker(theBoard, player2_marker, position)

                if win_check(theBoard, player2_marker):
                    display_board(theBoard)
                    print('Player 2 has won!')
                    game_on = False
                else:
                    if full_board_check(theBoard):
                        display_board(theBoard)
                        print('The game is a draw!')
                        break
                    else:
                        turn = 'Player 1'

        if not replay():
            break 

print(game())