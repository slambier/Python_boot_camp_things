i = 0

while i == 0:
    i = 1
    person1 = input("Person 1 -- Enter rock, paper, or scissors: ").lower()
    person2 = input("Person 2 -- Enter rock, paper, or scissors: ").lower()

    if person1 == person2:
        print("\nYou picked the same value. It's a tie!")
        i = 0
    elif person1 == "rock" and person2 == "scissors":
        print("\nRock beats scissors! Player 1 wins!")
    elif person1 == "scissors" and person2 == "rock":
        print("\nRock beats scissors! Player 2 wins!")
    elif person1 == "rock" and person2 == "paper":
        print("\nPaper beats rock! Player 2 wins!")
    elif person1 == "paper" and person2 == "rock":
        print("\nPaper beats rock! Player 1 wins!")
    elif person1 == "paper" and person2 == "scissors":
        print("\nScissors beats paper! Player 2 wins!")
    elif person1 == "scissors" and person2 == "paper":
        print("\nScissors beats paper! Player 2 wins!")
    else:
        print("\nSomeone entered the wrong value. Please try again.")
        i = 0