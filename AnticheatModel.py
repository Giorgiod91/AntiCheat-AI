import tensorflow as tf
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.losses import BinaryCrossentropy
import numpy as np
#import my method from analyseDemo file
from analyseDemo import get_total_kills
# add more hidden layers to get more accuracy
# ideas for some layer ----> ( is the person trying to access memory ? ) ----->   ( simulate memory scanning  )    binary again 1 for Yes  0 for No 

# using he imported method to get the total kill instead of hard codec value
kill_count = get_total_kills()




# pro player aim vector [ 0.9319481  -0.34341177  0.11636624]
aim_vector_pro = [ 0.9319481,  -0.34341177,  0.11636624]

# hardcoded data for now on just to test my model
HeadshotPercent = ["70","50","40","99","100", "85"]
#kill_count = ["5", "10", "15", "25", "35", "40"]


#method to filter headshot % if its really high

def filtered_Headshot(HeadshotPercent, kill_count):
    filtered_Headshot_percent = []
    for i in HeadshotPercent:
        if i >= 70 and kill_count >= 25:
            filtered_Headshot_percent.append(i)

    return filtered_Headshot_percent

filtered_Headshot(HeadshotPercent=HeadshotPercent, kill_count=kill_count)
    




y = [0, 0, 0, 1, 1,1]
X = np.array(list(zip(HeadshotPercent, kill_count)),dtype=np.int32)
y = np.array(y)



print(f"shape of headshotpercent: {X.shape}")
print(f"shape of killcount: {y.shape}")


# Define the model
model = Sequential()

# input and hidden layer with the default ReLU activation
model.add(Dense(units=10, activation='relu', input_dim=5))  


model.add(Dense(units=5, activation='relu'))  



# outout layer with sigmoid activations since its a binarz classification
model.add(Dense(units=1, activation='sigmoid'))



# Compile the model 
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(X, y, epochs=100)


# Make predictions on new data
try_data = (82, 29)
# reshape into 2D array
try_data_reshaped  = np.array(try_data).reshape(1, -1)
predictions = model.predict(try_data_reshaped)

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

