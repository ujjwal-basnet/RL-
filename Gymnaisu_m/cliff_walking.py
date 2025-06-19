import gymnasium as gym 
import os 


#create enviroment 
env= gym.make(id='CliffWalking' , render_mode="rgb_arra")


# Compute the size of the action space
num_actions = env.action_space.n

# Compute the size of the state space
num_states = env.observation_space.n

print("Number of actions:", num_actions)
print("Number of states:", num_states)
