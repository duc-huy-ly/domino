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


def play_move(chosen_number, player, snake,stock):
    if chosen_number == 0:
        if len(snake)==0:
            pass
        else:
            value = stock.pop()
            player.append(value)
    elif chosen_number < 0:
        index = abs(chosen_number) - 1
        value = player[index]
        snake.insert(0, value)
        player.remove(value)
    elif chosen_number > 0:
        index = chosen_number - 1
        value = player[index]
        snake.append(value)
        player.remove(value)


def handle_user_input(stock, player, snake, current_player):
    is_valid = False
    while not is_valid:
        try:
            user_choice = int(input())
            if abs(user_choice) > len(player) or (user_choice==0 and len(stock)==0):
                raise ValueError
            play_move(user_choice, player, snake, stock)
            is_valid = True
        except ValueError:
            print("Invalid input. Please try again.")


def handle_computer_decision(stock, computer, snake):
    # Wait for user to enter something to continue
    input()
    # Pick random number
    random_number = randint(-len(computer), len(computer))
    play_move(random_number, computer, snake, stock)



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
            current_player = "computer"
        elif current_player == "computer":
            handle_computer_decision(stock, computer, snake)
            current_player = "player"

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
        if len(player) == 0:
            print("Status : The game is over. You won!")
        else:
            print("Status: Computer is about to make a move. Press Enter to continue...")
    elif starting_player == "player":
        if len(computer) == 0:
            print("Status : The game is over. The computer won")
        else:
            print("Status: It's your turn to make a move. Enter your command:")


def display_snake(snake):
    if len(snake) < 6:
        for i in snake:
            print(i, end="")
        print()
    else:
        for i in range(3):
            print(snake[i], end="")
        print("...", end="")
        for i in range(len(snake)-3, len(snake),1):
            print(snake[i], end="")
        print()
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
