import random
from collections import defaultdict

# Transition matrix (counts)
transition_matrix = defaultdict(lambda: defaultdict(int))

def update_transition_matrix(prev_seq, next_move):
    transition_matrix[prev_seq][next_move] += 1

def predict_next_move(last_seq):
    if last_seq not in transition_matrix:
        return random.choice(['R', 'P', 'S'])
    
    next_moves = transition_matrix[last_seq]
    return max(next_moves, key=next_moves.get)

def player(prev_play, opponent_history=[]):
    if prev_play:
        opponent_history.append(prev_play)
    
    n = 3  # Number of previous moves to consider in the sequence

    if len(opponent_history) <= n:
        return random.choice(['R', 'P', 'S'])
    
    # Create the last sequence
    last_seq = "".join(opponent_history[-n:])
    
    # Update the transition matrix with the new sequence
    if len(opponent_history) > n:
        prev_seq = "".join(opponent_history[-(n+1):-1])
        update_transition_matrix(prev_seq, opponent_history[-1])
    
    # Predict the opponent's next move
    predicted_next_move = predict_next_move(last_seq)
    
    # Counter the predicted next move
    counter_move = {'R': 'P', 'P': 'S', 'S': 'R'}
    guess = counter_move[predicted_next_move]
    
    return guess

