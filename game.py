import random
from player_class import Player

player = Player("player")
cpu = Player("cpu")


def start() -> None:
    print("Welcome to Rock papper scissors!!!")
    start_game = (input("wanna play?(yes or no): ")).upper()

    if start_game == "YES":
        play()
    else:
        end()


def play() -> None:
    possible_moves = ["ROCK", "PAPER", "SCISSORS"]
    possible_outcomes = {"ROCK-SCISSORS", "PAPER-ROCK", "SCISSORS-PAPER"}

    cpu_move = random.choice(possible_moves)

    player_move = (input(f"what is you move?({possible_moves}): ")).upper()
    if player_move not in possible_moves:
        print(f">unvalid input\n>please type one of {possible_moves}")
        paly_again()

    if player_move == cpu_move:
        print("draw")
        paly_again()

    for move in possible_outcomes:
        player_won = f"{player_move}-{cpu_move}" == move
        if player_won:
            print(f"player won")
            player.increase_score()
            paly_again()

    print(f"player losed")
    cpu.increase_score()
    paly_again()


def paly_again() -> None:
    print(f"{player.name} {player.score} - {cpu.score} {cpu.name}")
    if (input("do you wanna play again?(yes or no): ")).upper() == "YES":
        play()
    else:
        end()


def end() -> None:
    print("have nice time, cya :)")
