# Write your code here
from random import randint
from random import shuffle

AMOUNT_OF_INIT_DOMINOES_PER_PLAYER = 7
AMOUNT_OF_STOCK_PIECES = 14


def generate_domino_set():
    domino_set = []
    for i in range(7):
        for j in range(i, 7):
            domino_set.append([i, j])
    return domino_set


def get_starting_domino(computer_set, player_set):
    computer_set.sort()
    player_set.sort()
    starting_domino = []
    if computer_set[-1] > player_set[-1]:
        starting_domino.append(computer_set[-1])
        computer_set.remove(starting_domino[0])
    else:
        starting_domino.append(player_set[-1])
        player_set.remove(starting_domino[0])
    return starting_domino


def display_interface(stock_pieces, computer_set, player_set, domino_snake, starting_player, is_over, winner):
    print('='*70)
    print(f'Stock size: {len(stock_pieces)}')
    print(f'Computer pieces: {len(computer_set)}')

    # Displaying the snake
    if len(domino_snake) > 6:
        for i in range(3):
            print(domino_snake[i], end="")
            print("...", end="")
            print(domino_snake[-3-i], end="")
        print()
    else:
        for i in domino_snake:
            print(i, end=" ")

    print()
    print(f'\nYour pieces:')
    for i in range(len(player_set)):
        print(f'{i+1}:{player_set[i]}')
    print()
    if not is_over:
        if starting_player == "player":
            print("Status: It's your turn to make a move. Enter your command.")
        else:
            print("Status: Computer is about to make a move. Press Enter to continue...")
            input()
    else:
        if winner == "player":
            print("Status: the game is over. You won!")
        elif winner == "computer":
            print("Status: the game is over. The computer won!")
        elif winner == "draw":
            print("Status: the game is over. Draw")

def get_starting_player(computer_set, player_set):
    if len(computer_set) < len(player_set):
        return "player"
    return "computer"


def convert_input(number, current_player, stock_pieces, domino_snake):
    if abs(number) > len(current_player):
        raise ValueError
    if number < 0:
        # The number starts at 1, so I have to -1 for list manipulation
        domino_snake.insert(0, current_player[abs(number) - 1])
        current_player.remove(domino_snake[0])
    elif number > 0:
        domino_snake.append(current_player[number - 1])
        current_player.remove(domino_snake[-1])
    else:
        # the case when the user enters 0
        if len(stock_pieces) == 0:
            pass
        else:
            current_player.append(stock_pieces[0])
            stock_pieces.remove(current_player[-1])


def is_draw(snake):
    return snake[0][0] == snake[-1][1] and snake.count(snake[0][0])==8


def main():
    # Initialisation of the game
    domino_set = generate_domino_set()
    shuffle(domino_set)
    player_set = domino_set[0:AMOUNT_OF_INIT_DOMINOES_PER_PLAYER]
    computer_set = domino_set[AMOUNT_OF_INIT_DOMINOES_PER_PLAYER:AMOUNT_OF_STOCK_PIECES]
    stock_pieces = domino_set[AMOUNT_OF_STOCK_PIECES:]
    domino_snake = get_starting_domino(computer_set, player_set)
    current_player = get_starting_player(computer_set, player_set)
    winner = ""
    is_over_game = False
    # Game loop
    while not is_over_game:
        display_interface(stock_pieces, computer_set, player_set, domino_snake, current_player, is_over_game, winner)
        if current_player == "player":
            is_valid = False
            while not is_valid:
                try:
                    user_input = int(input())
                    convert_input(user_input, player_set, stock_pieces, domino_snake)
                    is_valid = True
                    current_player = "computer"
                except ValueError:
                    print("Invalid input. Please try again.")
        else:
            random_choice = randint(-len(computer_set), len(computer_set))
            convert_input(random_choice, computer_set, stock_pieces, domino_snake)
            current_player = "player"

        # check the game state
        if len(player_set) == 0:
            is_over_game = True
            winner = "player"
        elif len(computer_set) == 0:
            is_over_game = True
            winner = "computer"
        elif is_draw(domino_snake):
            is_over_game = True
            winner = "draw"
    display_interface(stock_pieces, computer_set, player_set, domino_snake, current_player, is_over_game, winner)

if __name__ == "__main__":
    main()
