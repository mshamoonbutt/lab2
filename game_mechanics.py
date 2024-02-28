import random
from question_bank import *
#---------------------------------------
#  Game Mechanics
#    Student A (team lead)
#---------------------------------------

def welcome_message():
    """
    Display the game's welcome message to the player.

    Parameters: None
    Returns: None
    """
    #------------------------
    print("Welcome to the Quiz Game!")
    #------------------------
    #------------------------

#---------------------------------------

def choose_category(categories):
    """
    Ask the player to choose a quiz category from a list of categories.

    Parameters:
    - categories (list of str): A list of category names.

    Returns:
    - str: The chosen category.
    """
    #------------------------
    print("Choose a category:")
    for idx, category in enumerate(categories, 1):
        print(f"{idx}. {category}")
    choice = input("Enter the number of your choice: ")
    while not choice.isdigit() or int(choice) not in range(1, len(categories) + 1):
        print("Invalid input! Please enter a valid number.")
        choice = input("Enter the number of your choice: ")
    return categories[int(choice) - 1]
    #------------------------
    #------------------------
    
#---------------------------------------
    

def display_score(score, round_number):
    """
    Display the current score and round number to the player.

    Parameters:
    - score (int): The player's current score.
    - round_number (int): The current round number.

    Returns: None
    """
    #------------------------
    print(f"Score: {score} | Round: {round_number}")
    #------------------------
    #------------------------

#---------------------------------------

def game_over_message(final_score):
    """
    Display a "game over" message along with the player's final score.

    Parameters:
    - final_score (int): The player's final score at the end of the game.

    Returns: None
    """
    #------------------------
    print(f"Game Over! Final Score: {final_score}")
    #------------------------
    #------------------------

#---------------------------------------

def run_game_rounds(categories):
    """
    Implement a basic loop to run the game for 5 rounds.

    Parameters:
    - categories (list of str): A list of quiz categories.

    Returns: None
    """
    #------------------------
    score = 0
    for round_number in range(1, 6):
        print("\nRound", round_number)
        display_score(score, round_number)
        category = choose_category(categories)
        question, correct_answer = select_random_question(category)
        player_answer = display_question_and_accept_answer(question)
        if check_answer(player_answer, correct_answer):
            print("Correct!")
            score += 1
        else:
            print("Incorrect!")
            display_correct_answer(correct_answer)
        remove_question(category, question)

    game_over_message(score)
    #------------------------
    #------------------------

#---------------------------------------

def validate_answer(player_answer, correct_answer):
    """
    Validate the player's answer (correct or incorrect).

    Parameters:
    - player_answer (str): The answer provided by the player.
    - correct_answer (str): The correct answer to the question.

    Returns:
    - bool: True if the player's answer is correct, False otherwise.
    """
    #------------------------
    return player_answer.lower() == correct_answer.lower()
    #------------------------
    #------------------------

#---------------------------------------

def update_score(score, correct):
    """
    Implement a scoring system, where each correct answer awards points.

    Parameters:
    - score (int): The current score of the player.
    - correct (bool): Whether the player's answer was correct.

    Returns:
    - int: The updated score.
    """
    #------------------------
    if correct:
        score += 1
    return score
    #------------------------
    #------------------------
    
#---------------------------------------

def next_round(round_number):
    """
    Increase the round number after each question.

    Parameters:
    - round_number (int): The current round number.

    Returns:
    - int: The next round number.
    """
    #------------------------
    return round_number + 1
    #------------------------
    #------------------------
    
#---------------------------------------
    

def check_game_over(incorrect_answers):
    """
    Implement a "game over" condition if the player makes 3 incorrect answers.

    Parameters:
    - incorrect_answers (int): The number of incorrect answers given by the player.

    Returns:
    - bool: True if the game should be over, False otherwise.
    """
    #------------------------
    return incorrect_answers >= 3
    #------------------------
    #------------------------
#---------------------------------------

def restart_or_exit():
    """
    Restart the game or exit after the game is over.

    Parameters: None
    Returns: None
    """
    #------------------------
    choice = input("Do you want to restart the game? (yes/no): ")
    if choice.lower() == "yes":
        pass
    else:
        print("Thank you for playing!")
        exit()
    #------------------------
    #------------------------    