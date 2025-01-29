from demoparser2 import DemoParser
import numpy as np
import pandas as pd



#analyse demo for the models
pd.set_option('display.max_rows', 500)
parser = DemoParser("./demos/demo1.dem")


csv_data = []

df = parser.parse_event("player_death", player=["last_place_name", "team_name"], other=["total_rounds_played", "is_warmup_period"])
# filter out team-kills and warmup
print(df.columns)
print(df.head())
df = df[df["attacker_team_name"] != df["user_team_name"]]
df = df[df["is_warmup_period"] == False]
df = df.groupby(["total_rounds_played","attacker_name"]).size().to_frame(name='total_kills').reset_index()


# method to print out the rows to then use specific ones i need for my model
def get_row(df):
    for row in df:
        print(row)







# knowign the rows now i can access the one that give me the player
def get_Player(df, user_name):
    if user_name in df['user_name'].values:
        return df[df['user_name'] == user_name]
    else:
        print(f"Error: Could not find {user_name} in the DataFrame.")
        return None





def get_total_kills(df ,player_name):

    pd.set_option('display.max_rows', 500)
    if "event_type" in df.columns:
        df = df[df["event_type"] == "kill"]
       

    total_kills = (
         df[df['attacker_name'] == player_name]   # Filter for the specific user 
        .groupby(["total_rounds_played",  "attacker_name", ])  # Group by rounds played
        .size()  
        .to_frame(name="total_kills")  # Convert to DataFrame
        .reset_index()  # Reset index for cleaner output
    )

    return total_kills

#playing around with visualizing the data

donk_kills = get_total_kills(df, "donk")
print(donk_kills)
total_kills_sum = donk_kills["total_kills"].sum()
print(f"Total kills by donk: {total_kills_sum}")

# get the scoreboiard
max_tick = parser.parse_event("round_end")["tick"].max()
filterd_df = ["kills_total"]
filterd_df_new = parser.parse_ticks(filterd_df, ticks=[max_tick])
print(filterd_df_new)

# method to get the suspected player
def get_suspected_player():
    suspect = input("Enter the name of the suspected player: ")
    return suspect

get_suspected_player()

# method to filter the filtered df
def filter_filtered_df(filterd_df_new , suspect):
    for index, row in filterd_df_new.iterrows(): 
        if suspect in row['name']:
            
            return row
        
# set the suspect to the player you want to investigate
suspect = get_suspected_player()
print(filter_filtered_df(filterd_df_new, suspect= suspect))



# analyse aim of the player 
player_hurt_events = parser.parse_event("player_hurt")
df_aim  = parser.parse_ticks(["pitch", "yaw"])
print(df_aim.head())


df_head = parser.parse_header(["headshot"])
df_total_kills = get_total_kills(df, suspect)
# meothod to get the headshotCount 
def get_headshot_count(df_head, df_total_kills):
    headshot_count = df_head["headshot"].sum()
    total_kills = df_total_kills["total_kills"].sum()
    headshot_percent = (headshot_count / total_kills) * 100
    return headshot_percent

get_headshot_count(df_head, df_total_kills)
    


for (idx, event) in player_hurt_events.iterrows():
    start_tick = event["tick"] - 300
    end_tick = event["tick"]
    attacker = event["attacker_steamid"]
    
    # 
    if attacker != None:
        subdf = df_aim[(df_aim["tick"].between(start_tick, end_tick)) & (df_aim["name"] == suspect)]
        # save the data to a file csv to later train my model with
       # f = open("aim.txt", "w")
        #f.write(str(subdf))
        #f.close()
        

# convert the pitch and yaw to a 3d vector
def pitch_and_yawn_to_vector(subdf):
    # filter out the pitch and yaw
    for index, row in subdf.iterrows():
        pitch = row['pitch']
        yaw = row['yaw']
        new_pitch = np.radians(pitch)
        new_yaw = np.radians(yaw)

        x = np.cos(new_pitch) * np.cos(new_yaw)
        y = np.cos(new_pitch) * np.sin(new_yaw)
        z = -np.sin(new_pitch) 
        #returns a 3d vector
    return np.array([x, y, z])


      
print(pitch_and_yawn_to_vector(subdf))



# pro player aim vector [ 0.9319481  -0.34341177  0.11636624]