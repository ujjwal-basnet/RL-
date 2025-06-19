# RL
This repo in 3 pars 
1) openai gym
2) deep learing rl 
3) llm rl 


!) 
## 📘 What is an MDP?

A **Markov Decision Process (MDP)** is a mathematical framework for modeling decision making in situations where outcomes are partly random and partly under the control of an agent.

An MDP is defined by:
- **States (S):** Possible situations
- **Actions (A):** Choices the agent can make
- **Transition probabilities (P):** Likelihood of moving from one state to another
- **Rewards (R):** Feedback received after taking actions
- **Discount factor (γ):** Future reward importance

## 🧠 Example Code

```python
import gym

# Define the environment
env = gym.make('FrozenLake', is_slippery=True)

# Access action and state space
num_actions = env.action_space.n
num_states = env.observation_space.n

print("Number of actions:", num_actions)
print("Number of states:", num_states)

```
Code is in the [`Gymnaisu_m`](https://github.com/ujjwal-basnet/RL-/tree/main/Gymnaisu_m) folder.

---

## 🖼️ Visuals with Linked Code

Click on each image to view the related code:

### ❄️ Frozen Lake

[![Frozen Lake](https://github.com/ujjwal-basnet/RL-/raw/main/out-images//home/ujjwal/ujjwal/RL-/out-images/initial-frozen-lake_1.png)](https://github.com/ujjwal-basnet/RL-/blob/main/Gymnaisu_m/Frozen-Lake-environment.py)

---

### 🧗 Cliff Walking

[![Cliff Walking](https://github.com/ujjwal-basnet/RL-/out-images/cliffwalking)](https://github.com/ujjwal-basnet/RL-/blob/main/Gymnaisu_m/cliff_walking.py)

---

### 🚗 Mountain Car

[![Mountain Car](https://github.com/ujjwal-basnet/RL-/out-images/out-images/mountaincar_render1.png)](https://github.com/ujjwal-basnet/RL-/blob/main/Gymnaisu_m/setting-up-mountian-car.py)

---