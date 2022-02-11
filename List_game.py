#a small game where a user can choose a "position" in an existing list and replace it with a value of their choice

#defining the game list
game_list=[0,1,2]

#displaying the game list
def display(game_list):
    return('Here is the current list: {}'.format(game_list))

#creating a function for input
def game_input(game_list):

    user_input='WRONG'

    while user_input=='WRONG':
        user_input=input('Enter an index poisiton from (0,1,2): ')

        if user_input not in ('0','1','2'):
            print('Sorry, thats not a valid input')
            user_input='WRONG'
    
    return int(user_input)

#replacing the item in list
def replacement_choice(game_list,user_input):
    replacement=input('Enter the string to be placed in position: ')
    game_list[user_input]=replacement
    return('The new list is: {}'.format(game_list))

#asking the user whether to continue playing?
def gameon_choice():
    choice='WRONG'

    while choice=='WRONG':
        choice=input('Whether to continue playing, Y or N: ')

        if choice not in ('Y','N'):
            print('Sorry, the choice should be in Y or N')
            choice='WRONG'
    
    if choice=='Y':
        return game_on==True

    elif choice=='N':
        return game_on==False







#Launching game
game_on=True
game_list=[0,1,2]

while game_on:
    print(display(game_list))
    print(replacement_choice(game_list,game_input(game_list)))
    print(gameon_choice())