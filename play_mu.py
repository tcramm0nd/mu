from mu import MU, Rules
 # check if load is accurate

def mu_game():
    print('''Welcome to MU, a puzzle game invented by Douglas Hofstadter in his book Godel Escher Bach''')
    name = input('Please enter your name: ')

    # options to play a game, view the rules
    # game_option = menu_options()
    play = True

    rules = Rules()
    game = MU()

    while play:
        game_input(game)
        # if game.lose:
        #     play = False

def menu_options(game):
    menu = {'New Game': 'n',
            'Display Rules': 'd',
            'Display Current Game':'c',
            'Back to Game': 'g',
            'Save Game': 's',
            'Load Game': 'l',
            'Quit': 'q'}

    for o in menu.keys():
        print(f'{menu[o]}: \t{o}')
    selected_option = input()

    if selected_option == menu['New Game']:
        print('start new game')
        mu_game()
    elif selected_option == menu['Display Rules']:
        print('rules')
    elif selected_option == menu['Display Current Game']:
        print(game)
    elif selected_option == menu['Back to Game']:
        return
    elif selected_option == menu['Save Game']:
        game.save()
    elif selected_option == menu['Load Game']:
        game.load()
    elif selected_option == menu['Quit']:
        quit()
    else:
        print('Not a valid option, please try again')
        menu_options(game)

def game_input(game):

    ingame_menu = {'Main Menu': 'm',
                   'Display Rules': 'd',
                   'Undo': 'u',
                   'Redo': 'r',
                   'Back to Game': 'g',
                   'Quit': 'q'}

    if len(game.history) == 1:
        player_input = input('Enter a rule, or press m for Menu: ')
    elif len(game.history) > 1:
        player_input = input('Enter a Rule, u for Undo, or m for Menu: ')
    elif len(game.history) >= 1 and len(game.redo_history) >= 1:
        player_input = input('Enter a Rule, u for Undo, r for Redo, or m for Menu: ')

    print(f'You selected {player_input}.')
    if player_input in game.rules.values():
        game.execute_rule(player_input)
    elif player_input == ingame_menu['Main Menu']:
        menu_options(game)
    elif player_input == ingame_menu['Undo']:
        game.undo()
    elif player_input == ingame_menu['Redo']:
        game.redo()

    else:
        print("""That is not a valid option; please choose one of the following:
              \nruleI\nruleII\nruleIII\nruleIV\n\nEnter 'm' for the Menu""")
        game_input(game)


if __name__ == '__main__':
    mu_game()
