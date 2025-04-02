import tensorflow as tf
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.losses import BinaryCrossentropy
import numpy as np
import time
import random
import matplotlib.pyplot as plt
#import my method from analyseDemo file

#import the vectors i need for my model
from analyseDemo import aim_vector_pro
from analyseDemo import aim_vector_cheater
from analyseDemo import new_aim_vector
# add more hidden layers to get more accuracy
# ideas for some layer ----> ( is the person trying to access memory ? ) ----->   ( simulate memory scanning  )    binary again 1 for Yes  0 for No 

# using he imported method to get the total kill instead of hard codec value




# aim vector pro [-0.66405502 -0.74712906  0.02879411]  best player demo2
# pro player aim vector [ 0.9319481  -0.34341177  0.11636624] i extracted from the demos i picked the current best player to be my top point anything above this reaction time is gonna be weird



# hardcoded data for now on just to test my model
HeadshotPercent = ["70","50","40","99","100", "85"]
#kill_count = ["5", "10", "15", "25", "35", "40"]


#method to check if the kill is allways in  the same time ms 

def aim_reaction_the_same(kills):
    #milisecond
    suspect_reaction_time =0
    ms = time.time_ns() // 1_000_000
    pro_reaction_time = random.randint(150, 200)

    if suspect_reaction_time < pro_reaction_time:
        print(f"suspicious")





#method to filter headshot % if its really high

def filtered_Headshot(HeadshotPercent, kill_count):
    filtered_Headshot_percent = []
    #convert string to int
    for i in map(int, HeadshotPercent):
        if i >= 70 and kill_count >= 25:
            filtered_Headshot_percent.append(i)

    return filtered_Headshot_percent



#def check_all_indications():

    



# the model will now work with one x feature atm for testing purpose

# those x features i picked are the key factors to detect unfair gameplay(cheating)
X_cheater = np.hstack([
    
    aim_vector_cheater  # 3D aim vector (X, Y, Z)
])
X_pro = np.hstack([
    
    aim_vector_pro  # 3D aim vector (X, Y, Z)
])

#combine cheater and pro data
X = np.vstack([X_cheater, X_pro])
# Create Labels (0 = Pro, 1 = Cheater)
y_cheater = np.ones(len(X_cheater))  # Cheaters → 1
y_pro = np.zeros(len(X_pro))  # Pros → 0

y = np.hstack([y_cheater, y_pro])  # Combine labels



#print(f"shape of headshotpercent: {X.shape}")
#print(f"shape of killcount: {y.shape}")


# Define the model
model = Sequential()
# input and hidden layer with the default ReLU activation
model.add(Dense(units=10, activation='relu', input_dim=3))  

model.add(Dense(units=5, activation='relu'))  

# outpout layer with sigmoid activations since its a binary classification
model.add(Dense(units=1, activation='sigmoid'))


# Compile the model 
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(X, y, epochs=3)
# Make predictions on new data
predictions = model.predict(new_aim_vector)



model.save("AnticheatModel")

print(f"Shape of new_aim_vector: {np.shape(new_aim_vector)}")


# Display predictions
print("Predictions (probability of being a cheater):", predictions)


predictions_binary = (predictions > 0.5).astype(int)
print("Predictions (binary classification):", predictions_binary)

# only for testing with hard coded values
def get_player_data():
    headshot_numbers = input("Enter headshot%")
    kill_number = input("Enter the kill count")

    print(headshot_numbers , kill_number)


    return headshot_numbers, kill_number


#Plot 
fig = plt.figure(figsize=(7,5))
ax = fig.add_subplot(111, projection='3d')  # Create a 3D subplot
# with : and 0 and 1 and 2 selecting all values from the vectors so its X,Y and z

# plot for cheaters
ax.scatter(aim_vector_cheater[:, 0], aim_vector_cheater[:, 1], aim_vector_cheater[:, 2], 
           color='red', label='Cheaters')

# plot for pros
ax.scatter(aim_vector_pro[:, 0], aim_vector_pro[:, 1], aim_vector_pro[:, 2], 
           color='blue', label='Pros')


# plot the suspect to visualize if person could be cheating
ax.scatter(new_aim_vector[:,0], new_aim_vector[:,1], new_aim_vector[:,2] , color="green", label="suspect")

ax.set_xlabel("X-axis ")
ax.set_ylabel("Y-axis ")
ax.set_zlabel("Z-axis ")
ax.set_title("3D Aim Vector Comparison")
plt.legend()
plt.show()







#::TODO:: create  false positive method

