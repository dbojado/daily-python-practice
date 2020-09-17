#Create a simple rock,paper,scissors game 

print('''Let play a game! Please pick one: \n
Rock
Paper
Scissors \n''')

while True:
    game_dict = {'rock': 1, 'scissors': 2, 'paper': 3}
    player_a = str(input("Player A: "))
    player_b = str(input("Player B: "))
    a = game_dict.get(player_a)
    b = game_dict.get(player_b)
    dif = a - b

    if dif in [-1, 2]:
        print('\nPlayer A Wins!')
        if str(input('\nDo you want to play another game, yes or no? ')) == 'yes':
            continue
        else:
            print('\nGame Over')
            break
    elif dif in [-2, 1]:
        print('\nPlayer B Wins!')
        if str(input('\nDo you want to play another game, yes or no? ')) == 'yes':
            continue
        else:
            print('\nGame Over')
            break
    else:
        print('\n Draw...Please continue')
        print('')