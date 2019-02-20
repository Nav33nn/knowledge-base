from gym import spaces
import numpy as np
import random
from itertools import groupby
from itertools import product



class TicTacToe():

    def __init__(self):
        """initialise the board"""
        # initialise state as an array
        self.check = {0: [(0, 1, 2), (0, 3, 6), (0, 4, 8)],
                          1: [(0, 1, 2), (1, 4, 7)],
                          2: [(0, 1, 2), (2, 5, 8), (2, 4, 6)],
                          3: [(0, 3, 6), (3, 4, 5)],
                          4: [(0, 4, 8), (1, 4, 7), (2, 4, 6), (3, 4, 5)],
                          5: [(3, 4, 5), (2, 5, 8)],
                          6: [(0, 3, 6), (2, 4, 6), (6, 7, 8)],
                          7: [(6, 7, 8), (1, 4, 7)],
                          8: [(6, 7, 8), (0, 4, 8), (2, 5, 8)]}
        self.state = [np.nan for _ in range(9)]  # initialises the board position, can initialise to an array or matrix
        self.val_agent = [1, 3, 5, 7, 9]
        self.val_env = [2, 4, 6, 8]
        rand_idxs = random.sample(range(9), 2)
        val_idx = random.randint(0 , 3)
        self.state[rand_idxs[0]] = self.val_agent[val_idx+1]
        self.state[rand_idxs[1]] = self.val_env[val_idx]
        # all possible numbers
        self.all_pos_num = [i+1 for i in np.arange(len(self.state))]  #, can initialise to an array or matrix
        self.reset()

    def is_winning(self, curr_state, curr_action):
        """Takes state as an input and returns whether any row, column or diagonal has winning sum
        Example: Input state- [1, 2, 3, 4, nan, nan, nan, nan, nan]
        Output = False"""
        for r in self.check[curr_action[0]]:
            tcsum = curr_state[r[0]] + curr_state[r[1]] +  curr_state[r[2]]
            if tcsum == 15:
                return True

    def is_terminal(self, curr_state, curr_action):
        # Terminal state could be winning state or when the board is filled up
        if self.is_winning(curr_state, curr_action):
            return True, 'Win'
        elif len(self.allowed_positions(curr_state)) == 0:
            return True, 'Tie'
        else:
            return False, 'Resume'

    def allowed_positions(self, curr_state):
        """Takes state as an input and returns all indexes that are blank"""
        return [i for i, val in enumerate(curr_state) if np.isnan(val)]

    def allowed_values(self, curr_state):
        """Takes the current state as input and returns all possible (unused) values that can be placed on the board"""

        used_values = [val for val in curr_state if not np.isnan(val)]
        agent_values = [val for val in self.all_pos_num if val not in used_values and val % 2 !=0]
        env_values = [val for val in self.all_pos_num if val not in used_values and val % 2 ==0]
        return agent_values, env_values

    def action_space(self, curr_state):
        """Takes the current state as input and returns all possible actions,
        i.e, all combinations of allowed positions and allowed values"""
        agent_actions = list(product(self.allowed_positions(curr_state), self.allowed_values(curr_state)[0]))
        env_actions = list(product(self.allowed_positions(curr_state), self.allowed_values(curr_state)[1]))
        return agent_actions, env_actions

    def state_transition(self, curr_state, curr_action):
        """Takes current state and action and returns the board position just after agent's move.
        Example: Input state- [1, 2, 3, 4, nan, nan, nan, nan, nan], action- [9, 7]
        Output = [1, 2, 3, 4, nan, nan, nan, 9, nan]
        """

        curr_state[curr_action[0]] = curr_action[1]
        return curr_state

    def step(self, curr_state, curr_action):
        """Takes current state and action and returns the next state, reward and whether the state is terminal.
        Hint: First, check the board position after
        agent's move, whether the game is won/loss/tied.
        Then incorporate environment's move and again check the board status.
        Example: Input state- [1, 2, 3, 4, nan, nan, nan, nan, nan], action- [9, 7]
        Output = ([1, 2, 3, 4, nan, nan, nan, 9, nan], -1, False)"""
        next_state = self.state_transition(curr_state, curr_action)
        _, next_env_actions = self.action_space(next_state)
        is_over, status = self.is_terminal(next_state, curr_action)
        reward = -1
        if is_over:
            if status == 'Win':
                reward = 10
        else:
            next_action = next_env_actions[np.random.choice(np.arange(len(next_env_actions)))]
            next_state[next_action[0]] = next_action[1]
            is_over, status = self.is_terminal(next_state, next_action)
            if is_over:
                if status == 'Win':
                    reward = -10
                    status = 'Loss'
        if is_over and status == 'Tie':
            reward = 0
        return next_state, reward, is_over, status

    def reset(self):
        return self.state
