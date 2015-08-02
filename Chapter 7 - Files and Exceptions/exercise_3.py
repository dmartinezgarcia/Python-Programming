# Exercise 3
#
# Change the way the high-scores functionality you created in the last challenge is implemented. This time,
# use a plain text file to store the list.
#


import sys

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

def score_file_update(file_obj, name, score):
    rd_ptr = file_obj.tell()
    file_obj.seek(0)
    lines = file_obj.readlines()
    file_obj.seek(rd_ptr)
    lowest_score = 100
    lowest_ind = None

    if len(lines) < 10:
        file_obj.writelines([name+"\n", str(score)+"\n"])
    else:
        for i in range(0, len(lines), 2):
            lscore = int(lines[i + 1].replace("\n", ""))
            if lscore < lowest_score:
                lowest_score = lscore
                lowest_ind = i

        if lowest_score < score:
            lines[lowest_ind] = name + "\n"
            lines[lowest_ind+1] = str(score) + "\n"
            file_obj.seek(0)
            file_obj.truncate()
            file_obj.writelines(lines)

def score_get(file_obj):
    def score_get_item(element):
        return element[1]
    rd_ptr = file_obj.tell()
    file_obj.seek(0)
    lines = file_obj.readlines()
    file_obj.seek(rd_ptr)
    scores = []

    for i in range(0, len(lines), 2):
        if len(lines[i][0]) != "\n":
            lines[i] = lines[i].replace("\n", "")
            lines[i+1] = lines[i+1].replace("\n", "")
            scores.append((lines[i], int(lines[i + 1])))
    scores.sort(key=score_get_item, reverse=True)

    return scores

def main():
    trivia_file = open_file("trivia.txt", "r")
    scores_file = open("scores_3.txt", "a+")
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
    score_file_update(scores_file, player_name, score)
    scores = score_get(scores_file)
    scores_file.close()


    print("That was the last question!")
    print("You're final score is", score)
    print("######################")
    print("#### HALL OF FAME ####")
    print("######################")
    for i in scores:
        print("# - " + i[0] + "\t\t" + str(i[1]))

main()
input("\n\nPress the enter key to exit.")
