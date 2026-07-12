import random

# Choices
choices = {
    "s": "Snake",
    "w": "Water",
    "g": "Gun"
}

print("====== Snake Water Gun Game ======")
print("Enter:")
print("s = Snake")
print("w = Water")
print("g = Gun")

user = input("\nChoose (s/w/g): ").lower()

if user not in choices:
    print("❌ Invalid Choice!")
else:
    computer = random.choice(["s", "w", "g"])

    print(f"\nYou chose     : {choices[user]}")
    print(f"Computer chose: {choices[computer]}")

    if user == computer:
        print("🤝 It's a Draw!")

    elif (
        (user == "s" and computer == "w") or
        (user == "w" and computer == "g") or
        (user == "g" and computer == "s")
    ):
        print("🎉 You Win!")

    else:
        print("💻 Computer Wins!")