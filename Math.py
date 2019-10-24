import random


def MathGame():
    rights = 0
    wrongs = 0

    questions = {}

    for i in range(5):
        int_f = random.randint(0, 10)
        int_l = random.randint(0, 10)
        operators = ['+', '-', '*']
        operator_value = random.choice(operators)
        question = str(int_f) + " " + operator_value + " " + str(int_l)
        answer = str(eval(question))
        question += ": "

        questions.update({question: str(answer)})

    for q in questions.keys():
        user_answer = input(q)
        if questions.get(q) == user_answer:
            print("Correct!")
            rights += 1
        else:
            print("Incorrect.")
            wrongs += 1

    if rights + wrongs == 5 and rights >= 3:
        print('You get a password')
    else:
        print("You failed this task.")
