from random import randint # importing random integer generator from module random


def main():
    # initialise variables questions_asked and correct_answers
    questions_asked = 0
    correct_answers = 0

    # Asks the user questions 10 times
    while questions_asked < 10:
        # randomly generates an opperator to use in the question, one of ["+", "-", "x", "/"]
        opperator = rand_opperator()

        # generates 3 numbers to be used in the equation
        a, b, c = opperation(opperator)

        # randomly selects a position in the equation, the value of which the user will have to work out
        removed_pos = remove_rand()

        # Asks the user the question and recieves their answer
        answer = ask_the_user(a, b, c, opperator, removed_pos)

        # checks their answer and increments correct_answers if they got the question right, prints out the result
        match removed_pos:
            case "a":
                if check_answer(a, answer) == True:
                    correct_answers += 1
            case "b":
                if check_answer(b, answer) == True:
                    correct_answers += 1
            case "c":
                if check_answer(c, answer) == True:
                    correct_answers += 1
        
        # increments the questions_asked counter
        questions_asked += 1

    # prints out the users score
    print(f"You got {correct_answers} questions right out of {questions_asked} questions!!!")



def rand_opperator():
    """
    Picks a random opporator from addition, multiplication, subtraction and division and returns it

    Returns
    -------
    String: Returns the random opperator as a string
    """

    # Defines a list of opperators
    opperators = ["+", "-", "x", "/"]

    # returns a random opperator from the list using random module
    return opperators[randint(0, 3)]



def opperation(opperand):
    """
    Returns 3 numbers to be used in the question in the format a [+,-,x,/] b = c

    Args
    ----
    opperand (str): The opperand which is used in the question asked to the user, can take values ["+", "-", "x", "/"]

    Returns
    -------
    tup of int: contains the values of a, b and c
    """

    # initialised variables a, b and c
    a = b = c = 0

    # if statement to determine which two values of the three to randomly generate
    if opperand == "/":
        b, c = randint(1, 10), randint(1, 10)
    else:
        a, b = randint(1, 10), randint(1, 10)

    # determines what the final value should be
    match opperand:
        case "/":
            a = c * b
        case "+":
            c = a + b
        case "-":
            c = a - b
        case "x":
            c = a * b

    # returns a tupple containing the values for a, b and c
    return a, b, c


def remove_rand():
    """
    Randomly selects a position in the equation to remove, this is the position of the equation where the user has to deduce what the value is

    Returns
    -------
    String: random letter a, b or c which correlates to a position in the equation a [+,-,x,/] b = c
    """
    # defines a list of the available options to be removed
    options = ["a", "b", "c"]
    
    # returns a random letter from the options list
    return options[randint(0, 2)]



def ask_the_user(a, b, c, opperand, removed):
    """
    Asks the user the question and returns their answer

    Args
    ----
    a, b, c (int): The numbers used in the equation that the user will be asked
    opperand (str): The opperand used in the equation, one of ["+", "-", "x", "/"]
    removed (str): The postion of the number that won't be shown to the user and they have to work out

    Returns
    -------
    int: The users answer is returned
    """
    # prints the question for the user, removing a randomly generated position
    match removed:
        case "a":
            print(f"? {opperand} {b} = {c}")
        case "b":
            print(f"{a} {opperand} ? = {c}")
        case "c":
            print(f"{a} {opperand} {b} = ?")

    # asks the user to input their answer and returns this, if a number is not input it asks them again
    while True:
        try:
            # returns the users answer
            return int(input("What is the missing number? "))
        except ValueError:
            print("Your answer must be an number")
    



def check_answer(answer, their_answer):
    """
    Checks the users answer, prints a message for the user and returns True or False based on if their answer is correct

    Args
    ----
    answer (int): The correct answer
    their_answer (int) :The answer the user gave to the question

    Returns
    -------
    bool: True if their answer was correct (answer == their_answer) else False
    """
    # checks if the user's answer and actual answer are the same
    if answer == their_answer:
        print("Correct!!!!")
        return True
    else:
        print(f"Incorrect, the answer was {answer}")
        return False


main()
