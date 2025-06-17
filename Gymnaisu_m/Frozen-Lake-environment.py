import gymnasium as gym 
import matplotlib.pyplot as plt 
import os 

# Create output folder
out_folder = "out-images"
os.makedirs(out_folder, exist_ok=True)

# Image save paths
path_initial = os.path.join(out_folder, "initial-frozen-lake_1.png")
path_final   = os.path.join(out_folder, "final-frozen-lake_1.png")

# Create environment
env = gym.make("FrozenLake-v1", 
               map_name="4x4",  
               is_slippery=False, 
               render_mode="rgb_array")

# Reset and get initial state
initial_state, info = env.reset()

# Save initial state image
initial_image = env.render()
plt.imsave(path_initial, initial_image)

# Action sequence (1=down, 2=right)
actions = [1, 1, 2, 1, 2, 2]

# Simulate the episode
for action in actions:
    state, reward, terminated, truncated, _ = env.step(action)
    if terminated or truncated:
        if reward == 1:
            print("Reached the goal!")
        else:
            print("Fell into a hole.")
        break  # Exit early if episode ends

# Save final state image
final_image = env.render()
plt.imsave(path_final, final_image)


############# question 
## how many action we ahve ############ 
print(f"we have {env.action_space.n} actions ")