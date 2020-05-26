import random

def max_score_action(pairs):
    """
    Returns the good_actions for maximum score player
    """
    max_score = -9999
    good_actions = []

    for action, score in pairs:
        if score > max_score:
            max_score = score
            good_actions = [action]
        elif score == max_score:
            good_actions.append(action)

    return random.choice(good_actions)

def min_score_action(pairs):
    """
    Returns the good_actions for minimum score player
    """
    min_score = 9999
    good_actions = []

    for action, score in pairs:
        if score < min_score:
            min_score = score
            good_actions = [action]
        elif score == min_score:
            good_actions.append(action)

    return random.choice(good_actions)
