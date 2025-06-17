import gymnasium as gym 
import  matplotlib.pyplot as plt 
import os 


out_folder= "out-images"
os.makedirs(name= out_folder, exist_ok= True)


#create an enviroment 
env  = gym.make(id="MountainCar-v0" , render_mode= "rgb_array")

## reset initial or reset the value 
initial_state, info = env.reset()

## for mountain car this intial state has two values , [position of car , vecotiy of car]

position = initial_state[0]
velocity= initial_state[1]

print(f" The position of the car is {position}")
print(f"The veclocity of the car is {velocity}")

######## visualize

def render_and_save():
    image_state = env.render()
    
    #save image to the fiel 
    output_path= os.path.join(out_folder,"mountaincar_render1.png")
    plt.imsave(fname=output_path ,arr= image_state )
    
    
    #print the images 
    plt.imshow(image_state)
    plt.show()
    
    
render_and_save()
