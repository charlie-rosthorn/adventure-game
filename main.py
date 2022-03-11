accepted = "yes"
riddle_answer = "bribes"
guess_count = 0
guess_limit = 3

# 1. Story Introduction

print("Hello traveller,")
print("To enter you must solve this riddle...")
print("Win, and you find treasure...")
print("lose, and you die...")
challenge_offer = input("Do you accept?\n")

# 2. Story Challenge

if challenge_offer == accepted:
    print("Good, Good...")
    print("You have only three guesses...")
    print("If you are justice, please do not lie...")
    guess = input("What is the price for your blind eye?\n")
    while guess_count < guess_limit and (guess != riddle_answer):
        guess = input("No, Try again...\n")
        guess_count += 1

# 3. Story Results

    if guess == riddle_answer:
        print("You have won! Enter to claim Victory!")
    else:
        print("You have failed! Prepare to die! *CRASH*\n")
else:
    print("Then leave here coward, never to return again...\n")
