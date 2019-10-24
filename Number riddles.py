import random


def riddleGame():
    print("You enter a square room with nothing but a piece of white paper in the middle. The paper reads:\n"
          "\nAnswer the riddle for you to proceed\nThe answer to the riddle is a number you see\nWhen multiples are present,"
          "\nthe answer is low to high with only space between the first and the second.\n")

    riddles = {
        "How many times can you subtract the number 5 from 25?": "1",
        "What two whole, positive numbers that have a one-digit answer when multiplied and a two-digit answer when added?": "1 9",
        "What whole, positive number have the same answer when multiplied together as when added together?": "2",
        "What three whole, positive numbers have the same answer when multiplied together as when added together?": "1 2 3",
        "What two-digit number equals two times the result of multiplying its digits?": "36",
        "What two two-digit numbers are each equal to their right-most digit squared?": "25 36",
        "What is the highest number that can be written with three digits?": "(9^9)^9",
        "What digit is the most frequent between the numbers 1 and 1,000 (inclusive)?": "1",
        "What digit is the least frequent between the numbers 1 and 1,000 (inclusive)?": "0",
        "I have a calculator that can display ten digits. "
        "How many different ten-digit numbers can I type using just the 0-9 keys once each, "
        "and moving from one keypress to the next using the knight’s move in chess?": "4"
    }

    random_riddle = list(riddles.keys())
    for r in range(1):
        key = random.choice(random_riddle)
        i = input(key + ': ')
        if i == riddles[key]:
            print('A wooden door appears before you as the answer to the riddle is correct, bright light shines through the small crevices...')
        else:
            print('The white piece of paper goes up in flames and the room becomes dark... Was the answer correct?')


riddleGame()
