# Write your code here
from random import randint
from random import shuffle

AMOUNT_OF_INIT_DOMINOES_PER_PLAYER = 7
AMOUNT_OF_STOCK_PIECES = 14


def main():
    # Initialisation
    player, computer, stock = initialise()
    snake = get_starting_domino(player, computer)
    starter = get_starting_player(computer,player)
    print_result(stock, player, computer, snake, starter)


def initialise():
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


def print_result(stock, player, computer, starting_domino, starting_player):
    print(f"Stock pieces: {stock}")
    print(f"Computer pieces: {computer}")
    print(f"Player pieces: {player}")
    print(f"Domino snake: {starting_domino}")
    print(f"Status: {starting_player}")


def get_starting_player(computer_set, player_set):
    if len(computer_set) < len(player_set):
        return "player"
    return "computer"


if __name__ == "__main__":
    main()
