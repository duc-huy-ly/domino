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


def print_result(stock_pieces, computer_set, player_set, starting_domino, starting_player):
    print(f"Stock pieces: {stock_pieces}")
    print(f"Computer pieces: {computer_set}")
    print(f"Player pieces: {player_set}")
    print(f"Domino snake: {starting_domino}")
    print(f"Status: {starting_player}")


def get_starting_player(computer_set, player_set):
    if len(computer_set) < len(player_set):
        return "player"
    return "computer"


def main():
    domino_set = generate_domino_set()
    shuffle(domino_set)
    player_set = domino_set[0:AMOUNT_OF_INIT_DOMINOES_PER_PLAYER]
    computer_set = domino_set[AMOUNT_OF_INIT_DOMINOES_PER_PLAYER:AMOUNT_OF_STOCK_PIECES]
    stock_pieces = domino_set[AMOUNT_OF_STOCK_PIECES:]
    starting_domino = get_starting_domino(computer_set, player_set)
    starting_player = get_starting_player(computer_set, player_set)
    print_result(stock_pieces, computer_set, player_set, starting_domino, starting_player)


if __name__ == "__main__":
    main()
