#---------------------------------------
#  Question Bank
#    Student B
#---------------------------------------
import random

# Define the categories and questions
# Simplified example with one category. Expand as needed.
# Simplified example with one category. Expand as needed.
questions = {
    "Science": [
        ("What is the chemical symbol for water?", "H2O"),
        ("Who developed the theory of relativity?", "Albert Einstein"),
        ("Which planet is known as the red planet?", "Mars"),
        ("What does DNA stand for?", "Deoxyribonucleic Acid")
    ],
    "General Education": [
        ("How many time zones are there in Russia?", "11"),
        ("What’s the national flower of Japan?", "Cherry Blossom"),
        ("What’s the national animal of Australia?", "Kangaroo"),
        ("How many days does it take for the Earth to orbit the Sun?", "365")
    ]
}

hints = {
    "Science": [
        "hydrogen", "Einstein", "Mars", "deoxyribonucleic acid"
    ],
    "General Education": [
        "Time zones", "Flowers", "Animal", "One year"
    ]
}

def select_random_question(category):
    """
    Selects a random question from the specified category.

    Parameters:
    - category (str): The category from which to select a question.

    Returns:
    - tuple: A tuple containing the selected question (str) and its corresponding answer (str).
    """
    question = random.choice(questions[category])
    return question

def check_answer(player_answer, correct_answer):
    """
    Checks if the player's answer matches the correct answer.

    Parameters:
    - player_answer (str): The answer provided by the player.
    - correct_answer (str): The correct answer to the question.

    Returns:
    - bool: True if the answers match, False otherwise.
    """
    return player_answer.lower() == correct_answer.lower()

def remove_question(category, question):
    """
    Removes a question from the list once it has been asked.

    Parameters:
    - category (str): The category from which to remove the question.
    - question (str): The question to be removed.

    Returns:
    - None
    """
    questions[category] = [q for q in questions[category] if q[0] != question]

def display_question_and_accept_answer(question):
    """
    Displays a question to the player and accepts their answer via input.

    Parameters:
    - question (str): The question to be displayed.

    Returns:
    - str: The player's answer to the question.
    """
    print(question)
    return input("Your answer: ")

def provide_hint(category, question):
    """
    Provides a hint for the given question based on its category.

    Parameters:
    - category (str): The category of the question.
    - question (str): The question for which to provide a hint.

    Returns:
    - str: The hint for the given question.
    """
    hint_index = questions[category].index((question, None))
    return hints[category][hint_index]

def display_correct_answer(correct_answer):
    """
    Displays the correct answer if the player's answer is incorrect.

    Parameters:
    - correct_answer (str): The correct answer to the question.

    Returns:
    - None
    """
    print("The correct answer is:",correct_answer)