def start_game():
    available_choices = ['X', 'O']
    first_player_choice = 'WRONG'
    second_player_choice = 'O'

    while first_player_choice not in available_choices:
        first_player_choice = input('Welcome to Tic Tac Toe game! Choose which X or O figure you want to play: ')

        if first_player_choice not in available_choices:
            print('Sorry, the wrong input. You can type only X or O. Please try again')

    if first_player_choice == 'O':
        second_player_choice = 'X'

    print(f'Great!'
          f'Now player one is going to play for "{first_player_choice}"'
          f'and second one is playing for "{second_player_choice}"')

    return [first_player_choice, second_player_choice]


def draw_field(current_field, player='None', player_choice=-1):
    if player_choice != -1:
        current_field[player_choice - 1] = '\033[1m' + player + '\033[0m'

    print(f'| {current_field[0]} | {current_field[1]} | {current_field[2]} |')
    print(f'| {current_field[3]} | {current_field[4]} | {current_field[5]} |')
    print(f'| {current_field[6]} | {current_field[7]} | {current_field[8]} |')

    return current_field


def make_move(player, field):
    choice = 'WRONG'
    player_choice = -1
    exit_condition = False

    while not exit_condition:
        choice = input(f'Player for "{player}" please make your choice: ')

        if choice.isdigit():
            player_choice = int(choice)
            if player_choice not in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
                print('Wrong input! Please type number from 1 to 9')

            elif field[player_choice - 1] == '\x1b[1mX\x1b[0m' or field[player_choice - 1] == '\x1b[1mO\x1b[0m':
                print('This field already taken. Please choose another one')

            else:
                exit_condition = True
        else:
            print('Given input is not a digit. Please try again')

    return player_choice


def play_round(field, current_player):
    print('\n')
    choice = make_move(current_player, field)
    current_field = draw_field(field, current_player, choice)

    return current_field


def check_player(current_field, player):
    is_winner = False
    winning_combinations = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    current_player = '\033[1m' + player + '\033[0m'

    current_combination = []
    for combination in winning_combinations:
        for i in range(3):
            current_combination.append(current_field[combination[i]])
        if current_combination.count(current_player) == 3:
            is_winner = True
            break
        else:
            current_combination = []

    return is_winner


def check_if_tie(current_field):
    count_chars = 0

    for cell in current_field:
        if cell not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            count_chars += 1
    return count_chars


def check_ending_rules(current_field, player):
    count_chars = check_if_tie(current_field)
    is_finish = check_player(current_field, player)

    if is_finish:
        print(f'Congratulations for the player {player}. You won!')
    elif count_chars == 9:
        is_finish = 'TIE'
        print('Congratulations, it is a TIE')

    return is_finish


def ask_for_one_more():
    available_choices = ['Y', 'N']
    one_more = 'WRONG'

    while one_more not in available_choices:
        one_more = input('Do you want to play one more? (Y or N): ')

        if one_more not in available_choices:
            print('Wrong input! Please type Y or N to continue')

    return one_more


def play_game():
    one_more_game = 'Y'
    while one_more_game != 'N':
        is_finish = False

        [first_player, second_player] = start_game()

        current_field = draw_field(['1', '2', '3', '4', '5', '6', '7', '8', '9'])

        while not is_finish:
            for current_player in [first_player, second_player]:
                current_field = play_round(current_field, current_player)
                is_finish = check_ending_rules(current_field, current_player)

                if is_finish or is_finish == 'TIE':
                    break

        one_more_game = ask_for_one_more()
        if one_more_game == 'Y':
            play_game()
        else:
            print('Bye!')
            break
