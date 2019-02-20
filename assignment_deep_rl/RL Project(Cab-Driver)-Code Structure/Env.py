# Import routines

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


class CabDriver():

    def __init__(self):
        """initialise your state and define your action space and state space"""
        self.action_space = list(permutations(range(0,m) ,2)) #action space is unique 2 values(source & destination)
        self.state_space = list(product(*[list(range(0,m)), list(range(0,t)), list(range(0,d))])) #State space from MDP:
        #𝑠=𝑋𝑖𝑇𝑗𝐷𝑘 𝑤ℎ𝑒𝑟𝑒 𝑖=0…𝑚−1;𝑗=0….𝑡−1;𝑘=0…..𝑑−1, Where 𝑋𝑖 represents a driver’s current location, 𝑇𝑗 represents time component (more specifically hour of the day), 𝐷𝑘 represents the day of the week
        self.state_init = random.choice(self.state_space) #Initialises to any random self_space
        
        #Starting 1st trip
        Time_matrix = np.load("TM.npy")

        # Start the first round
        self.reset()


    ## Encoding state (or state-action) for NN input

    def state_encod_arch1(self, state):
        """convert the state into a vector so that it can be fed to the NN. This method converts a given state into a vector format. Hint: The vector is of size m + t + d."""
       
        #Encoded values of m + t + d
        
        pos = (state[0]*24*7) + (state[1]*7) + state[2] 
        state_encod =  np.zeros(840)
        state_encod[pos] = 1
        
        
        return state_encod


    # Use this function if you are using architecture-2 
    # def state_encod_arch2(self, state, action):
    #     """convert the (state-action) into a vector so that it can be fed to the NN. This method converts a given state-action pair into a vector format. Hint: The vector is of size m + t + d + m + m."""

        
    #     return state_encod


    ## Getting number of requests

    def requests(self, state):
        """Determining the number of requests basis the location. 
        Use the table specified in the MDP and complete for rest of the locations"""
        location = state[0]
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
            


        if requests >15:
            requests =15

        possible_actions_index = random.sample(range(1, (m-1)*m +1), requests) # (0,0) is not considered as customer request
        actions = [self.action_space[i-1] for i in possible_actions_index]

        
        actions.append([0,0])

        return possible_actions_index,actions   



    def reward_func(self, state, action, Time_matrix):
        """Takes in state, action and Time-matrix and returns the reward"""
        
        if action == [0,0]:
            reward = -C 
            return reward
        
        p = action[0]
        q = action[1]
        i = state[0]
        time = state[1]
        day = state[2]
        t_pq = Time_matrix[p][q][time][day]
        t_ip = Time_matrix[i][p][time][day]
        
        
        reward = (R*t_pq)-(C*(t_pq+t_ip))

     
        return reward




    def next_state_func(self, state, action, Time_matrix):
        """Takes state and action as input and returns next state"""
        
        p = action[0]
        q = action[1]
        i = state[0]
        time_curr = state[1]
        day_curr = state[2]
        
        time_next = time_curr + Time_matrix[p][q][time_curr][day_curr]

        day_next = day_curr+int(time_next/24)
        time_next = time_next % 24
            
        next_state = (q,time_next,day_next)
        
                      
        return next_state




    def reset(self):
        return self.action_space, self.state_space, self.state_init
