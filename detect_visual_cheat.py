from awpy.plot import heatmap
import polars as pl
from awpy import Demo
import numpy as np
import matplotlib.pyplot as plt


dem = Demo("demos/demo1.dem", verbose=False)


# player_locations = list(
 #   dem.ticks.filter(pl.col("health") > 0, pl.col("side") == "ct")[["X", "Y", "Z"]].sample(100000).iter_rows()
#)
#fig, ax = heatmap(map_name="de_dust2", points=player_locations, method="hex", size=20)



#Hexagon(i want to fill out the 2d map with hexagon and then make them color red and if some player over them it should turn green)
player_walks_over = True
def createHexagon():
    a = 2
    R = a
    angles = np.linspace(0, 2 * np.pi, 7)
    x = R * np.cos(angles)
    y = R * np.sin(angles)

    return x,y

x,y = createHexagon()


# created a simple filter function for the color of the hexagon depending on the boolean player_walks_over
def change_hexagon(player_walks_over):
    if player_walks_over == True:
        plt.figure(figsize=(5,5))
        plt.plot(x,y, label="Hexagon")
        plt.fill(x,y, "g")
    
    else:
        plt.figure(figsize=(5,5))
        plt.plot(x,y, label="Hexagon")
        plt.fill(x,y, "r")
    plt.show()

change_hexagon(player_walks_over)














    
