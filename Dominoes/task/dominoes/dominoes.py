# Write your code here
import sys
from random import randint
from random import shuffle


def main():
    # Initialisation
    player, computer, stock = shuffle_dominos()
    snake = get_starting_domino(player, computer)
    current_player = get_starting_player(computer, player)
    # Game loop
    while True:
        display_interface(stock, player, computer, snake)
        game_is_over(player, computer, snake)
        if current_player == "player":
            print("Status: It's your turn to make a move. Enter your command:")
            handle_user_input(stock, player, snake)
            current_player = "computer"
        elif current_player == "computer":
            print("Status: Computer is about to make a move. Press Enter to continue...")
            handle_computer_decision(stock, computer, snake)
            current_player = "player"


def game_is_over(player, computer, snake):
    """Checks if one of the players won or if the game can not be won anymore"""

    if len(player) == 0:
        print("\nStatus: The game is over. You won!")
        sys.exit()
    elif len(computer) == 0:
        print("\nStatus: The game is over. The computer won!")
        sys.exit()
    elif snake[0][0] == snake[-1][1]:
        counter = 0
        for tile in snake:
            counter += tile.count(snake[0][0])
            if counter == 8:
                print("\nStatus: The game is over. It's a draw!")
                sys.exit()


def swap(value):
    temp = value[0]
    value[0] = value[1]
    value[1] = temp


def play_move(chosen_number, player, snake, stock):
    if chosen_number == 0:
        if len(stock) == 0:
            pass
        else:
            value = stock.pop()
            player.append(value)
    elif chosen_number < 0:
        index = abs(chosen_number) - 1
        value = player[index]
        # We need to check if re-orientation is needed
        if snake[0][0] != value[1]:
            swap(value)
        snake.insert(0, value)
        player.remove(value)
    elif chosen_number > 0:
        index = chosen_number - 1
        value = player[index]
        if snake[-1][1] != value[0]:
            swap(value)
        snake.append(value)
        player.remove(value)


def move_is_not_valid(chosen_number, player, snake):
    if chosen_number == 0:
        return False
    elif chosen_number < 0:
        index = abs(chosen_number) - 1
        value = player[index]
        # Inserting to the right of the snake. The second coord of player should
        # match with the first fo the snake
        if snake[0][0] not in value:
            return True
    elif chosen_number > 0:
        index = chosen_number - 1
        value = player[index]
        if snake[-1][1] not in value:
            return True
    return False


def handle_user_input(stock, player, snake):
    is_valid = False
    while not is_valid:
        try:
            user_choice = int(input())
            if abs(user_choice) > len(player):
                raise ValueError
            if move_is_not_valid(user_choice, player, snake):
                raise InvalidMoveException
            play_move(user_choice, player, snake, stock)
            is_valid = True
        except ValueError:
            print("Invalid input. Please try again.")
        except InvalidMoveException:
            print("Illegal move. Please try again.")


def handle_computer_decision(stock, computer, snake):
    # Wait for user to enter something to continue
    input()
    # Pick random number
    is_valid = False
    while not is_valid:
        random_number = randint(-len(computer), len(computer))
        if not move_is_not_valid(random_number, computer, snake):
            play_move(random_number, computer, snake, stock)
            is_valid = True


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


def is_draw(snake):
    if snake[0][0] == snake[-1][1]:
        counter = 0
        for tile in snake:
            counter += tile.count(snake[0][0])
            if counter == 8:
                return True
    return False


def display_snake(snake):
    if len(snake) < 6:
        for i in snake:
            print(i, end="")
        print()
    else:
        for i in range(3):
            print(snake[i], end="")
        print("...", end="")
        for i in range(len(snake)-3, len(snake), 1):
            print(snake[i], end="")
        print()


def display_interface(stock, player, computer, snake):
    print("="*70)
    print(f"Stock size: {len(stock)}")
    print(f"Computer pieces: {len(computer)}")
    display_snake(snake)
    display_player_pieces(player)


def get_starting_player(computer_set, player_set):
    if len(computer_set) < len(player_set):
        return "player"
    return "computer"


class InvalidMoveException(Exception):
    """When the dominos don't match"""
    pass


if __name__ == "__main__":
    main()
