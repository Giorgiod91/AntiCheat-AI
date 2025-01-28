from demoparser2 import DemoParser
import pandas as pd


#analyse demo for the models
pd.set_option('display.max_rows', 500)
parser = DemoParser("./demos/demo1.dem")

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
for (idx, event) in player_hurt_events.iterrows():
    start_tick = event["tick"] - 300
    end_tick = event["tick"]
    attacker = event["attacker_steamid"]
    
    # attacker can be none when player gets hurt by c4 etc.
    if attacker != None:
        subdf = df_aim[(df_aim["tick"].between(start_tick, end_tick)) & (df_aim["name"] == suspect)]
        print(subdf)



