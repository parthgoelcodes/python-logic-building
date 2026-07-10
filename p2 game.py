import random

moves = ["rock","paper","scissors"]

while True:
    player = input("enter your move( rock , paper , scissors ):-")
    if player == "exit":
        break


    computer = random.choice(moves)
    print("computers move:-",computer)

    if computer == player:
        print("draw ")

    elif (computer == "rock" and player == "scissors") or (computer == "paper" and player == "rock") or (computer == "scissors" and player == "paper"):
        print("💻computer won")

    elif (computer == "scissors" and player == "rock") or (computer == "paper" and player == "scissors") or (computer == "rock" and player == "paper"):
        print("🎮player won")

    else:
        print("❌invalid input")