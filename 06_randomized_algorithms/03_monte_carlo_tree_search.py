"""
Monte Carlo Tree Search (MCTS)
------------------------------
What it does:
An intelligent decision-making algorithm that explores possible future moves by:
1. Selection: Navigating down known good paths.
2. Expansion: Adding a new possible move to the tree.
3. Simulation (Rollout): Playing random moves to the end of the game to see who wins.
4. Backpropagation: Sending the win/loss score back up to update previous decisions.
It balances trying proven moves (exploitation) with trying less-explored options (exploration).

Real-World Use Cases:
- AI game engines for Go, Chess, and Shogi (AlphaGo, Leela Chess Zero).
- Autonomous robot motion and navigation in complex obstacle fields.
- Planning multi-step chemical reactions to synthesize new medical drugs.
"""

import math
import random

class MCTSNode:
    def __init__(self, state, parent=None):
        self.state = state
        self.parent = parent
        self.children = []
        self.visits = 0
        self.wins = 0

    def is_fully_expanded(self, all_actions):
        return len(self.children) == len(all_actions)

    def best_child(self, exploration_weight=1.414):
        # Upper Confidence Bound for Trees (UCT) formula
        choices_weights = [
            (child.wins / child.visits) + exploration_weight * math.sqrt(math.log(self.visits) / child.visits)
            for child in self.children
        ]
        return self.children[choices_weights.index(max(choices_weights))]

def mcts_demo():
    print("MCTS balances exploration and exploitation to find winning paths without checking every possibility.")

if __name__ == "__main__":
    mcts_demo()
