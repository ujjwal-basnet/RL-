import gymnasium as gym 
import os 
import matplotlib.pyplot as plt 


#create enviroment 
env= gym.make(id='CliffWalking' , render_mode="rgb_array")

out_folder = "out-images"
os.makedirs(out_folder, exist_ok=True)

# Image save paths
path_initial = os.path.join(out_folder, "initial-cliff walking-lake_1.png")
path_final   = os.path.join(out_folder, "final-cliff walking_1.png")


# Reset and get initial state
state = env.reset()[0]

# Save initial state image
initial_image = env.render()
plt.imsave(path_initial, initial_image)


transitions = env.unwrapped.P[state][1]

print() 
##disply transtion detials
for prob, next_state, reward, done in iter(transitions):
    print(f" Probability : {prob} , Next state: {next_state} , reward : {reward} , Done {done}")
    



######### define policy 
policy= {} 
starting_position= 36 
policy[starting_position] = 0 ###  i.e from 36 take upwards (which is denoted by 2 ) so after upward it moves to 26 

for s in range(24,35):
    policy[s]= 1 # right  go right 11 times 
    
policy[35]= 2 #down down then you reach the destiny



done = False
step_count = 0
max_steps = 100  # Adjust as needed

while not done and step_count < max_steps: ############# if its taking more then 100 step to find the solution end loop 
    action = policy.get(state, 1)
    state, reward, done, truncated, info = env.step(action)
    step_count += 1


final_image = env.render()
plt.imsave(path_final, final_image)