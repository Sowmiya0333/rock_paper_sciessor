import random

def player(prev_play, opponent_history=[]):
 
    if prev_play:
        opponent_history.append(prev_play)

    if len(opponent_history) == 0:
        return "R"

    most_common_move = max(set(opponent_history), key=opponent_history.count)

    if most_common_move == "R":
        return "P" 
    elif most_common_move == "P":
        return "S"  
    else:
        return "R" 