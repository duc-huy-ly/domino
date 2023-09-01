# Write your code here
import random


def generate_domino_set():
    domino_set = []
    for i in range(7):
        for j in range(i, 7):
            domino_set.append([i, j])
    return domino_set


def pick_random_dominos(domino_set, param):
    new_domino_set = []
    for i in range (param):
        random_number = random.randint(0, len(domino_set)-1)
        new_domino_set.append(domino_set[random_number])
        domino_set.remove(domino_set[random_number])
    return new_domino_set, domino_set


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
    player_set, domino_set = pick_random_dominos(domino_set, 7)
    computer_set, domino_set = pick_random_dominos(domino_set, 7)
    stock_pieces, domino_set = pick_random_dominos(domino_set, 14)
    starting_domino = get_starting_domino(computer_set, player_set)
    starting_player = get_starting_player(computer_set, player_set)
    print_result(stock_pieces, computer_set, player_set, starting_domino, starting_player)


if __name__ == "__main__":
    main()