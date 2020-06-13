import mu

def mu_game():
    print('Welcome to MU, a puzzle game invented by Douglas Hofstadter in Godel Escher Bach')
    name = input('Please enter your name: ')

    # options to play a game, view the rules
    # game_option = menu_options()



    game = mu.MU()
    print(game)
    game_input()
    game.ruleI()
    print(game)


def menu_options():
    option = input('New game or quit?\n')
    if option == 'n':
        print('start new game')
    elif option == 'r':
        print('rules')
    elif option == 'q':
        quit()
    else:
        print('not chill try again')
        menu_options()

    return option

def game_input():
    player_input = input('Enter a rule, or press m for Menu: ')
    print(f'You selected{player_input}.')
    if player_input in ['ruleI', 'ruleII', 'ruleIII', 'ruleIV']:
        execute_rule(player_input)
    else:
        print("""That is not a valid option; please choose one of the following:
              \nruleI\nruleII\nruleIII\nruleIV\n\n Enter 'm' for the Menu""")
        game_input()

    return player_input


if __name__ == '__main__':
    mu_game()
