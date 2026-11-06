# Project: Building a self grading quiz

# The topic is open
# 7 questions minimum
# multiple choice (A,B,C,D)
# You need to ask for the user name,
# store it and use it to address the user.
# keep track of correct answers and incorrect answers
# Provide the user with their final score.

# Theme: Sonic The Hedgehog

# Ask for the user's name
userName = input("What is your name? ")
print("\nWelcome to the Sonic quiz, " + userName + "!")
print("Answer each question by typing A, B, C, or D.\n")

# Keep track of correct and incorrect answers
correctAnswers = 0
incorrectAnswers = 0

# Questions choices and correct answers
questions = [
    {
        "question": "1. What Species is Knuckles?",
        "choices": [
            "A) Cat",
            "B) Hedgehog",
            "C) Echidna",
            "D) Fox"
        ],
        "answer": "C"
    },
    {
        "question": "2. How many Chaos Emeralds are there?",
        "choices": [
            "A) 5",
            "B) 6",
            "C) 7",
            "D) 8"
        ],
        "answer": "C"
    },
    {
        "question": "3. What weapon does Amy Rose use?",
        "choices": [
            "A) Piko-Piko Spear",
            "B) Piko-Piko Hammer",
            "C) Piko-Piko Sword",
            "D) Piko-Piko Dagger"
        ],
        "answer": "B"
    },
    {
        "question": "4. What color are Sonic's eyes?",
        "choices": [
            "A) Red",
            "B) Blue",
            "C) Green",
            "D) Purple"
        ],
        "answer": "C"
    },
    {
        "question": "5. Who is the princess of the Sol Empire?",
        "choices": [
            "A) Honey The Cat",
            "B) Sally Acorn",
            "C) Blaze The Cat",
            "D) Trip The Sungazer"
        ],
        "answer": "C"
    },
    {
        "question": "6. What's the name of the first level in Sonic 3?",
        "choices": [
            "A) Angel Island Zone",
            "B) Green Hill Zone",
            "C) Emerald Hill Zone",
            "D) Palmtree Panic"
        ],
        "answer": "A"
    },
    {
        "question": "7. Which game was Cream The Rabbit introduced in?",
        "choices": [
            "A) Sonic Battle",
            "B) Sonic Advance 2",
            "C) Sonic Heroes",
            "D) Sonic Adventure 2"
        ],
        "answer": "B"
    }
]

# Ask each question and grade the answer
for question in questions:
    print(question["question"])

    for choice in question["choices"]:
        print(choice)

    userAnswer = input("What is your choice? (A, B, C, or D): ").strip().upper()

    # Make sure the user enters a valid choice
    while userAnswer not in ["A", "B", "C", "D"]:
        print("Please enter A, B, C, or D.")
        userAnswer = input("What is your choice? (A, B, C, or D): ").strip().upper()

    if userAnswer == question["answer"]:
        print("Correct, " + userName + "! Great job!\n")
        correctAnswers += 1
    else:
        print("Sorry, " + userName + ", that is incorrect.")
        print("The correct answer was " + question["answer"] + ".\n")
        incorrectAnswers += 1

# Calculate and display the final score
totalQuestions = len(questions)
percentage = (correctAnswers / totalQuestions) * 100

print("===== QUIZ RESULTS =====")
print("Great effort, " + userName + "!")
print("Correct answers: " + str(correctAnswers))
print("Incorrect answers: " + str(incorrectAnswers))
print("Final score: " + str(correctAnswers) + "/" + str(totalQuestions))
print("Percentage: " + str(round(percentage, 1)) + "%")

if correctAnswers == totalQuestions:
    print("Aw yeah, This is happenin!")
elif correctAnswers >= 5:
    print("Way past cool!")
elif correctAnswers >= 3:
    print("Not so bad!")
else:
    print("Try again some other time.")
