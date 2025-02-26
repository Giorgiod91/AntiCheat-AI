creating methods to access player name from the demo video then i will extract the parts i need from the best pro player from the given demo to then use this as my example in my model to learn from the best to then later detect cheater

- extract data from the demos with demoparser2
- set guideline from pro player stats ( accuracy and so on)

#Goals:

- let the model (neural network) learn pattern from pro player
- be able to detect inhuman reaction time (pro player reaction time should set the standart of high reaction time)
- see if the model can see difference between a pro player and a cheater stat wise ( movement, accuracy and so on)
- get big data set to work with
- first test it with myself playing

#Aim analyse

- Pitch: ( vertical angle of aim so up and down) ---> 90 is looking straigh up - 90 is looking straight down
- Yaw: (horizontal angle of aim so left and right) ----> represents the rotation around the vertical axis, usually in degrees from 0° to 360°
- Tick: he server tick at which the aim data was recorded.

-------> convert this into a 3d Vektor to analyse

#Getting demos from Cheater to compare the reaction time vector with the pro player ones and see the difference

#Ideas to detect visual cheats like radar hack or wallhack

- i will extract the demos and will set specific points in all of the maps to check if player walk pass these without checking corners
- i could check if someone only has good crosshairplacement if someone is near the suspect

#trying to calc reaction time with the data i have now i have tick, pitch myaw looking for the difference in those vectors from one tick to another to get the reaction time
