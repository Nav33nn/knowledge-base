# Import routines
# This cell contains the CabDriver class

import numpy as np
import math
import random
from itertools import permutations,product

# Defining hyperparameters
m = 5 # number of cities, ranges from 1 ..... m
t = 24 # number of hours, ranges from 0 .... t-1
d = 7  # number of days, ranges from 0 ... d-1
C = 5 # Per hour fuel and other costs
R = 9 # per hour revenue from a passenger
Time_matrix = np.load("TM.npy")


class CabDriver():

    def __init__(self):
        """initialise your state and define your action space and state space"""
        self.action_list = list(permutations(range(0,m) ,2))
        self.action_list.append((0,0))
        self.action_space = np.array(self.action_list) #action space is unique 2 values(source & destination) + the no op
        self.state_space = list(product(*[list(range(0,m)), list(range(0,t)), list(range(0,d))])) #State space from MDP:
        #𝑠=𝑋𝑖𝑇𝑗𝐷𝑘 𝑤ℎ𝑒𝑟𝑒 𝑖=0…𝑚−1;𝑗=0….𝑡−1;𝑘=0…..𝑑−1, Where 𝑋𝑖 represents a driver’s current location, 𝑇𝑗 represents time component (more specifically hour of the day), 𝐷𝑘 represents the day of the week
        self.state_size = len(self.state_space)
        self.action_size = len(self.action_space)
        self.state_init = random.choice(self.state_space) #Initialises to any random self_space
        self.encode_vector = np.array([24*7, 7, 1]).reshape(3, 1)
        self.action_map = {v:k for k,v in enumerate(self.action_list)}
        # Start the first round
        self.reset()


    ## Encoding state (or state-action) for NN input

    def state_encod_arch1(self, curr_state, batch_size=1):
        """convert the state into a vector so that it can be fed to the NN. This method converts a given state into a vector format. Hint: The vector is of size m + t + d."""
        curr_state = np.array(curr_state).reshape(1, 3)
        pos_mat = np.dot(curr_state, self.encode_vector)
        state_encod =  np.zeros((1, self.state_size))
        for i in range(batch_size):
            state_encod[i][pos_mat[i]] = 1

        return np.reshape(state_encod, [1, self.state_size])
    

    def requests(self, state):
        """Determining the number of requests basis the location. 
        Use the table specified in the MDP and complete for rest of the locations"""
        location = state[0]
        possible_actions_index = []
        requests = 0
        if location == 0:
            requests = np.random.poisson(2)

        if location == 1:
            requests = np.random.poisson(12)   #MDP Poisson distribution
        
        if location == 2:
            requests = np.random.poisson(4)    #MDP Poisson distribution
            
        if location == 3:
            requests = np.random.poisson(7)    #MDP Poisson distribution

        if location == 4:
            requests = np.random.poisson(8)    #MDP Poisson distribution  
            
        if requests > 15:
            requests = 15
        elif requests == 0:
            requests = 1

        possible_actions_index = random.sample(range(0, (m-1)*m), requests) # (0,0) is not considered as customer request
        if possible_actions_index or len(possible_actions_index) > 0:
            possible_actions_index.append(20)#add the index of No-OP action (0, 0)
        else:
            self.requests(state)
        actions = [self.action_space[i] for i in possible_actions_index]

        return possible_actions_index, actions   



    def reward_func(self, state, action, Time_matrix):
        """Takes in state, action and Time-matrix and returns the reward"""
        if action[0] == action[1]:
            reward = -C 
            return reward

        pickup = action[0]
        drop = action[1]
        current = state[0]
        time_curr = state[1]
        day_curr = state[2]
        #handle situation where current position is the same as pickup point
        if current == pickup:
            t_pq = Time_matrix[pickup][drop][time_curr][day_curr]
            t_ip = 0
        else:
            t_ip = Time_matrix[current][pickup][time_curr][day_curr]
            time_ip, day_ip = self.trip_time_adjust(time_curr, 
                                                             day_curr, 
                                                             start=current, 
                                                             end=pickup)
            t_pq = Time_matrix[pickup][drop][time_ip][day_ip]
            
        
        #reward formula mentioned in the MDP
        reward = (R*t_pq)-(C*(t_pq+t_ip))
        return reward


    def next_state_func(self, state, action, Time_matrix):
        """Takes state and action as input and returns next state"""
        next_state = None
        pickup = action[0]
        drop = action[1]
        current = state[0]
        time_curr = state[1]
        day_curr = state[2]
        
        if pickup != drop:
            if current == pickup:
                time_next, day_next = self.trip_time_adjust(time_curr, day_curr, start=pickup, end=drop)
            else:
                time_interim, day_interim = self.trip_time_adjust(time_curr, 
                                                             day_curr, 
                                                             start=current, 
                                                             end=pickup)
                time_next, day_next = self.trip_time_adjust(time_interim, 
                                                             day_interim, 
                                                             start=pickup, 
                                                             end=drop)
                
            next_state = (drop, time_next, day_next)
        else:
            next_state = state # if there is no action retain the state
        
        return next_state

    #reset env
    def reset(self):
        self.state_init = random.choice(self.state_space)
        return self.action_space, self.state_space, self.state_init
    
    #handle the time/day increase if the drop time goes to the next day
    def trip_time_adjust(self, time_curr, day_curr, start, end):
        time_next = time_curr + Time_matrix[start][end][time_curr][day_curr]
        
        if time_next < 24:
            day_next = day_curr
        else:
            day_next = (day_curr + 1) % 7 #int((day_curr+int(time_next/24)) % 7)
            time_next = time_next % 24
            
        return int(time_next), int(day_next)
