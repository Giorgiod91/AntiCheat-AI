from awpy.plot import heatmap
import polars as pl
from awpy import Demo


dem = Demo("demos/demo1.dem", verbose=False)


player_locations = list(
    dem.ticks.filter(pl.col("health") > 0, pl.col("side") == "ct")[["X", "Y", "Z"]].sample(100000).iter_rows()
)
fig, ax = heatmap(map_name="de_dust2", points=player_locations, method="hex", size=20)