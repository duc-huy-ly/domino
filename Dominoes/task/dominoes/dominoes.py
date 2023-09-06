# Write your code here
from random import randint
from random import shuffle

AMOUNT_OF_INIT_DOMINOES_PER_PLAYER = 7
AMOUNT_OF_STOCK_PIECES = 14


def game_is_over(player, computer, snake):
    if len(player) == 0 or len(computer) == 0:
        return True
    if is_draw(snake):
        return True


def is_valid(user_input, player, stock):
    if user_input == 0:
        if len(stock) > 0:
            return True
        return False
    return abs(user_input) <= len(player)


def add_domino_to_snake(index, player, snake, stock):
    if index < 0:
        # Add to the left
        value = player[abs(index) - 1]
        snake.insert(0, value)
        player.remove(value)
    elif index > 0:
        value = player(index - 1)
        snake.append(value)
        player.remove(value)
    elif index == 0:
        if len(stock) > 0:
            element_from_stock = stock.pop()
            player.append(element_from_stock)
        else:
            print("Nothing to take from stock")
            pass


def handle_user_input(stock, player, snake, current_player):
    try:
        user_input = int(input())
        if is_valid(user_input, player, stock):
            add_domino_to_snake(user_input, player, snake, stock)
    except ValueError:
        print("Illegal move. Please try again")
    pass


def handle_computer_decision(stock, computer, snake, current_player):
    # TODO
    #here
    pass


def main():
    # Initialisation
    player, computer, stock = shuffle_dominos()
    snake = get_starting_domino(player, computer)
    current_player = get_starting_player(computer, player)
    status = ""
    # Game loop
    while not game_is_over(player, computer, snake):
        display_interface(stock, player, computer, snake, current_player)
        if current_player == "player":
            handle_user_input(stock, player, snake, current_player)
        elif current_player == "computer":
            handle_computer_decision(stock, computer, snake, current_player)

    display_interface(stock, player, computer, snake, current_player)


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


def is_draw(snake):
    return snake[0][0] == snake[-1][1] and snake.count(snake[0][0]) == 8



def display_status(starting_player, computer, player, stock):
    if is_draw(stock):
        print("Status : Draw")
    elif starting_player == "computer":
        if len(computer) == 0:
            print("Status : computer won")
        else:
            print("Status: Computer is about to make a move. Press Enter to continue...")
    elif starting_player == "player":
        if len(player) == 0:
            print("Status : you won!")
        else:
            print("Status: It's your turn to make a move. Enter your command:")


def display_snake(snake):
    if len(snake) < 6:
        for i in snake:
            print(i)
    pass


def display_interface(stock, player, computer, snake, starting_player):
    print("="*70)
    print(f"Stock size: {len(stock)}")
    print(f"Computer pieces: {len(computer)}")
    display_snake(snake)
    display_player_pieces(player)
    display_status(starting_player, computer, player, stock)


def get_starting_player(computer_set, player_set):
    if len(computer_set) < len(player_set):
        return "player"
    return "computer"


if __name__ == "__main__":
    main()
