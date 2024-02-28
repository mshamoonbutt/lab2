import random
def choose_difficulty():
    difficulty = input("Choose difficulty (easy, medium, hard): ").lower()
    while difficulty not in ['easy', 'medium', 'hard']:
        print("Invalid input! Please choose from 'easy', 'medium', or 'hard'.")
        difficulty = input("Choose difficulty (easy, medium, hard): ").lower()
    return difficulty

def display_leaderboard(leaderboard):
    if not leaderboard:
        print("Leaderboard is empty.")
    else:
        sorted_leaderboard = sorted(leaderboard.items(), key=lambda x: x[1], reverse=True)
        print("Leaderboard:")
        for idx, (player, score) in enumerate(sorted_leaderboard, 1):
            print(f"{idx}. {player}: {score}")

def save_score(player_name, score, file_path='scores.txt'):
    with open(file_path, 'a') as file:
        file.write(f"{player_name}: {score}\n")

def load_top_scores(file_path='scores.txt'):
    leaderboard = {}
    try:
        with open(file_path, 'r') as file:
            for line in file:
                player, score = line.strip().split(': ')
                leaderboard[player] = int(score)
    except FileNotFoundError:
        print("Leaderboard file not found. Creating a new one...")
    return leaderboard

def provide_feedback(is_correct):
    if is_correct:
        print("Well done!")
    else:
        print("Sorry, that's incorrect.")

def fifty_fifty_lifeline(correct_answer, options):
    incorrect_options = [opt for opt in options if opt != correct_answer]
    random.shuffle(incorrect_options)
    return [correct_answer, incorrect_options[0]]

def skip_question(allowed_skips):
    if allowed_skips > 0:
        print("You have chosen to skip this question.")
        return True
    else:
        print("You have no more skips available.")
        return False