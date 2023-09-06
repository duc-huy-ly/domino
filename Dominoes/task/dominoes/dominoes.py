# Write your code here
from random import randint
from random import shuffle

AMOUNT_OF_INIT_DOMINOES_PER_PLAYER = 7
AMOUNT_OF_STOCK_PIECES = 14


def main():
    # Initialisation
    player, computer, stock = shuffle_dominos()
    snake = get_starting_domino(player, computer)
    starter = get_starting_player(computer,player)
    display_interface(stock, player, computer, snake, starter)


def shuffle_dominos():
    domino_set = []
    for i in range(7):
        for j in range(i, 7):
            domino_set.append([i, j])
    shuffle(domino_set)
    player = domino_set[0:7]
    computer = domino_set[7:14]
    stock = domino_set[14:]
    return player, computer, stock


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


def display_player_pieces(player):
    print("Your pieces:")
    j = 1
    for i in player:
        print(f"{j}:{i}")
        j += 1
    pass


def display_status(starting_player):
    if starting_player == "computer":
        print("Status: Computer is about to make a move. Press Enter to continue...")
    else:
        print("Status: It's your turn to make a move. Enter your command.")


def display_snake(snake):
    print(snake[0])
    pass


def display_interface(stock, player, computer, snake, starting_player):
    print("="*70)
    print(f"Stock size: {len(stock)}")
    print(f"Computer pieces: {len(computer)}")
    display_snake(snake)
    display_player_pieces(player)
    display_status(starting_player)


def get_starting_player(computer_set, player_set):
    if len(computer_set) < len(player_set):
        return "player"
    return "computer"


if __name__ == "__main__":
    main()
