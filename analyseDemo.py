import numpy as np
import pandas as pd
from awpy import Demo
# link i use https://github.com/pnxenopoulos/awpy/blob/main/docs/examples/parse_demo.ipynb
#analyse demo for the models
from demoparser2 import DemoParser

dem = Demo("demos/demo1.dem", verbose=False)





parser = DemoParser("demos/demo1.dem")
last_tick = parser.parse_event("round_end")["tick"].to_list()[-1]
df = parser.parse_ticks(["crosshair_code"],ticks=[last_tick])
print(df)

df_for_aim = parser.parse_ticks(["pitch", "yaw"])



#df_for_player_position = parser.parse_event(player=["X", "Y"])






my_function_called = False
csv_data = []

data_1 = dem.weapon_fires
#converting to dataFrame
df = pd.DataFrame(data_1)
df_kills = pd.DataFrame(dem.kills)
print(df_kills)

# method to print out the rows to then use specific ones i need for my model
def get_row(df):
    for row in df:
        pd.set_option('display.max_rows', 20)
        print(df)
        
# filter for specific player i need now hard coded later will be based on input
player_name = "donk"
# knowing the rows now i can access the one that give me the player
if "player_name" in df.columns:
    player_data = df[df["player_name"] == player_name]
    if not player_data.empty:
        print(player_data)  
    else:
        print(f"Error: Could not find {player_name} in the DataFrame.")
else:
    print("Error: Column 'player_name' not found in the DataFrame.")


#def get_total_kills(df ,player_name):

#playing around with visualizing the data



# method for user to get the crosshair from a player

# players allways want the crosshaircode from pro players 


# method to get the suspected player
def get_suspected_player():
    suspect = input("Enter the name of the suspected player: ")
    return suspect



# method to filter the filtered df
def filter_filtered_df(filterd_df_new , suspect):
    for index, row in filterd_df_new.iterrows(): 
        if suspect in row['name']:
            
            return row
        
# set the suspect to the player you want to investigate





# analyse aim of the player 

# filter out headshots
def filter_headshots(df):
    for row in df:
        if "headsthot" in df:
            print(f"filtered headshots:  {row}")

# meothod to get the headshotCount 
def get_headshot_count(df, df_total_kills):
    headshot_count = df.columns["headshot"].sum()
    total_kills = df_total_kills["total_kills"].sum()
    headshot_percent = (headshot_count / total_kills) * 100
    my_function_called = True
    return headshot_percent

#headshot_count_for_txt = get_headshot_count(df_head, df_total_kills)



def create_txt_file(headshot_count_for_txt):
    f = open("headshot.txt", "w")
    f.write(str(headshot_count_for_txt))
    f.close()
# if i analysed for headshot count then it should create a file but only then 
#if my_function_called == True:
 #   create_txt_file(headshot_count_for_txt)
   

suspect = get_suspected_player()

player_hurt_events = parser.parse_event("player_hurt")
for (idx, event) in player_hurt_events.iterrows():
     start_tick = event["tick"] - 300
     end_tick = event["tick"]
     attacker = event["attacker_steamid"]
 
     # 
     if attacker != None:
         subdf = df_for_aim[(df_for_aim["tick"].between(start_tick, end_tick)) & (df_for_aim["name"] == suspect)]
         # save the data to a file csv to later train my model with
        # f = open("aim.txt", "w")
         #f.write(str(subdf))
         #f.close()
 





        
#get_Crosshair(df=df, player_name=get_suspected_player)
# convert the pitch and yaw to a 3d vector
def pitch_and_yaw_to_vector(data):
    vectors = []
    # filter out the pitch and yaw
    for index, row in data.iterrows():
        # pitch -90 means looking straight down +90 means looking  straight up
        pitch = row['pitch']
        yaw = row['yaw']
        new_pitch = np.radians(pitch)
        new_yaw = np.radians(yaw)

        x = np.cos(new_pitch) * np.cos(new_yaw)
        y = np.cos(new_pitch) * np.sin(new_yaw)
        z = np.sin(new_pitch) 
        #returns a 3d vector

        vectors.append([x,y,z])
    return np.array(vectors)

aim_vector_pro = pitch_and_yaw_to_vector(data=df_for_aim)


#if "m0NESY" in dem:
 #   new_aim_vector = pitch_and_yaw_to_vector(dem)
#elif "donk" in dem:
 #   vector_pro = pitch_and_yaw_to_vector(dem)
#else:
 #   vector_cheat = pitch_and_yaw_to_vector(dem)

# compare them now for the length they have to be same length to work in my model

def compare_cheat_with_legit_aim_vector_lenght(vector,vector_pro, vector_cheat):
    norm_vector = np.linalg.norm(vector)
    norm_cheat = np.linalg.norm(vector_cheat)
    norm_pro = np.linalg.norm(vector_pro)

    if norm_cheat > norm_pro:
        print(f"Cheater's aim vector is longer ({norm_cheat}) than pro's ({norm_pro})")
    else:
        print(f"Pro's aim vector is longer ({norm_pro}) than cheater's ({norm_cheat})")



#claculate the distance to get the reaction time from one tick to another
def  euclidean_distance(v1,v2):
    return np.linalg.norm(v1-v2)



# get player positions on weapon fires for now on later switch up
def get_player_position(df_for_player_position):
    player_name = input("enter a player name")
   
    if player_name in df_for_player_position:    
                player_data = df_for_player_position[df_for_player_position['player_name'] == player_name]
                player_X = player_data['X']
                player_Y = player_data['Y']

                print(player_X)
                print(player_Y)

                return player_X , player_Y
    else:
        print("player position not found!")
        





#track overlap of player postion and heatmap fields
def overlap_player_heatmap_point(player_X, player_Y):
    heatmap_X = ["red"]
    if player_X == heatmap_X:
        print("Player stepped on field {heatmap_X}")
        heatmap_X = ["green"]
        heatmap_X = ["red"]
       

    



    








# if __name__ == "__main__":