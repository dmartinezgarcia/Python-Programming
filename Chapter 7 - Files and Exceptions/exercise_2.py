# Exercise 2
#
# Improve the Trivia Challenge game so that it maintains a high scores list in a file. The program should record the
# player's name and score if the player makes the list. Store the high scores using a pickled object.
#


import sys
import shelve

def open_file(file_name, mode):
    """Open a file."""
    try:
        the_file = open(file_name, mode)
    except IOError as e:
        print("Unable to open the file", file_name, "Ending program.\n", e)
        input("\n\nPress the enter key to exit.")
        sys.exit()
    else:
        return the_file

def next_line(the_file):
    """Return next line from the trivia file, formatted."""
    line = the_file.readline()
    line = line.replace("/", "\n")
    return line

def next_block(the_file):
    """Return the next block of data from the trivia file."""
    category = next_line(the_file)

    question = next_line(the_file)

    answers = []
    for i in range(4):
        answers.append(next_line(the_file))

    correct = next_line(the_file)
    if correct:
        correct = correct[0]

    explanation = next_line(the_file)

    points = next_line(the_file)
    if points:
        points = int(points)

    return category, question, answers, correct, explanation, points

def welcome(title):
    """Welcome the player and get his/her name."""
    print("\t\tWelcome to Trivia Challenge!\n")
    print("\t\t", title, "\n")

def score_file_update(shelf, name, score):
    lowest_key = ""
    lowest_score = 100

    if len(shelf) < 10:
        shelf[name] = score
    else:
        for key in shelf:
            score_shelf = shelf[key]
            if score_shelf < lowest_score:
                lowest_score = score_shelf
                lowest_key = key

        if shelf[lowest_key] < score:
            del shelf[lowest_key]
            shelf[name] = score

    shelf.sync()

def score_get(shelf):
    def score_get_item(element):
        return element[1]
    score_list = []

    for key in shelf:
        score_list.append((key, shelf[key]))
    score_list.sort(key=score_get_item, reverse=True)
    return score_list

def main():
    trivia_file = open_file("trivia.txt", "r")
    scores_shelf = shelve.open("scores.txt", "c")
    title = next_line(trivia_file)
    welcome(title)
    score = 0

    # Get player name
    player_name = input("Player, what is your name? ")
    # get first block
    category, question, answers, correct, explanation, points = next_block(trivia_file)
    while category:
        # ask a question
        print(category)
        print(question)
        for i in range(4):
            print("\t", i + 1, "-", answers[i])

        # get answer
        answer = input("What's your answer?: ")

        # check answer
        if answer == correct:
            print("\nRight!", end=" ")
            score += points
        else:
            print("\nWrong.", end=" ")
        print(explanation)
        print("Score:", score, "\n\n")

        # get next block
        category, question, answers, correct, explanation, points = next_block(trivia_file)

    trivia_file.close()
    score_file_update(scores_shelf, player_name, score)
    scores = score_get(scores_shelf)
    scores_shelf.close()


    print("That was the last question!")
    print("You're final score is", score)
    print("######################")
    print("#### HALL OF FAME ####")
    print("######################")
    a = 1
    for i in scores:
        print("# - " + str(a) + "\t\t" + i[0] + "\t\t" + str(i[1]))
        a += 1

main()
input("\n\nPress the enter key to exit.")
