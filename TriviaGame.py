"""
Filename: trivia_game.py
Author: <Nunez, Bryan>
Created: <9/30/2026>
Instructor: Burgess
"""

#step 1 greet user
print("This program will create a trivia game that will autograde the user’s answers. The game will ask the user a series of questions. \n The program will then check the user’s inputs, and give them a score based on how many questions they answered correctly.")

correct_questions = 0
total_score = 0

# --- STEP 3: THE QUESTIONS ---

# Question 1
print("What is the capital city of France?")
# .lower() makes sure if they type "Paris" or "PARIS" it still counts as correct!
answer1 = input("Answer: ").lower()

if answer1 == "paris":
    total_score = total_score + 2
    correct_questions = correct_questions + 1
    print("Correct! You have been awarded 2 points!\n")
else:
    if total_score > 0:
        total_score = total_score - 1
        print("Incorrect! You have been penalized 1 point!\n")
    else:
        print("Incorrect! Your score is 0, so no points were taken away.\n")


# Question 2
print("What planet is known as the Red Planet?")
answer2 = input("Answer: ").lower()

if answer2 == "mars":
    total_score = total_score + 2
    correct_questions = correct_questions + 1
    print("Correct! You have been awarded 2 points!\n")
else:
    if total_score > 0:
        total_score = total_score - 1
        print("Incorrect! You have been penalized 1 point!\n")
    else:
        print("Incorrect! Your score is 0, so no points were taken away.\n")


# Question 3
print("What is the largest mammal in the world?")
answer3 = input("Answer: ").lower()

# Accepting either "blue whale" or just "whale"
if answer3 == "blue whale" or answer3 == "whale":
    total_score = total_score + 2
    correct_questions = correct_questions + 1
    print("Correct! You have been awarded 2 points!\n")
else:
    if total_score > 0:
        total_score = total_score - 1
        print("Incorrect! You have been penalized 1 point!\n")
    else:
        print("Incorrect! Your score is 0, so no points were taken away.\n")


# Question 4
print("How many colors are there in a standard rainbow?")
answer4 = input("Answer: ")

# Checking for both the number 7 or the word seven
if answer4 == "7":
    total_score = total_score + 2
    correct_questions = correct_questions + 1
    print("Correct! You have been awarded 2 points!\n")
else:
    if total_score > 0:
        total_score = total_score - 1
        print("Incorrect! You have been penalized 1 point!\n")
    else:
        print("Incorrect! Your score is 0, so no points were taken away.\n")


# Question 5
print("Which ocean is the largest on Earth?")
answer5 = input("Answer: ").lower()

if answer5 == "pacific" or answer5 == "pacific ocean":
    total_score = total_score + 2
    correct_questions = correct_questions + 1
    print("Correct! You have been awarded 2 points!\n")
else:
    if total_score > 0:
        total_score = total_score - 1
        print("Incorrect! You have been penalized 1 point!\n")
    else:
        print("Incorrect! Your score is 0, so no points were taken away.\n")


# Question 6
print("What is H20")
answer6 = input("Answer: ").lower()

if answer6 == "water":
    total_score = total_score + 2
    correct_questions = correct_questions + 1
    print("Correct! You have been awarded 2 points!\n")
else:
    if total_score > 0:
        total_score = total_score - 1
        print("Incorrect! You have been penalized 1 point!\n")
    else:
        print("Incorrect! Your score is 0, so no points were taken away.\n")


# Question 7
print("How many days are in a regular year?")
answer7 = input("Answer: ")

if answer7 == "365":
    total_score = total_score + 2
    correct_questions = correct_questions + 1
    print("Correct! You have been awarded 2 points!\n")
else:
    if total_score > 0:
        total_score = total_score - 1
        print("Incorrect! You have been penalized 1 point!\n")
    else:
        print("Incorrect! Your score is 0, so no points were taken away.\n")


# Question 8
print("Who was the first president of the United States?")
answer8 = input("Answer: ").lower()

if answer8 == "george washington" or answer8 == "washington" or answer8 == "george washingmachine":
    total_score = total_score + 2
    correct_questions = correct_questions + 1
    print("Correct! You have been awarded 2 points!\n")
else:
    if total_score > 0:
        total_score = total_score - 1
        print("Incorrect! You have been penalized 1 point!\n")
    else:
        print("Incorrect! Your score is 0, so no points were taken away.\n")


# Question 9
print("What do bees make using nectar from flowers?")
answer9 = input("Answer: ").lower()

if answer9 == "honey":
    total_score = total_score + 2
    correct_questions = correct_questions + 1
    print("Correct! You have been awarded 2 points!\n")
else:
    if total_score > 0:
        total_score = total_score - 1
        print("Incorrect! You have been penalized 1 point!\n")
    else:
        print("Incorrect! Your score is 0, so no points were taken away.\n")


# Question 10
print("What is the name of the wizarding school that Harry Potter attends?")
answer10 = input("Answer: ").lower()

if answer10 == "hogwarts" or "mogwarts":
    total_score = total_score + 2
    correct_questions = correct_questions + 1
    print("Correct! You have been awarded 2 points!\n")
else:
    if total_score > 0:
        total_score = total_score - 1
        print("Incorrect! You have been penalized 1 point!\n Dont blame yourself for not watching straight mid! \n")
    else:
        print("Incorrect! Your score is 0, so no points were taken away.\n Dont blame yourself for not watching straight mid!\n")


# --- STEP 4: FINAL SCORES ---
print("Thank you for playing the Trivia Game!")
print("You answered " + str(correct_questions) + "/10 questions correctly,")
print("and received a score of " + str(total_score) + "/20!")
