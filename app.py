from flask import Flask, request, jsonify
import numpy as np
from tensorflow.keras.models import load_model
from demoparser2 import DemoParser

# Create a Flask application instance
app = Flask(__name__)


#load my pretrained model

model = load_model("AnticheatModel")

# Define a route for my frontend that compares the aim to the suspect to my model build from analyse pro player aim
@app.route('/predict' , method=["POST"])
def predict():          

    demoName = ""
    suspectName = ""
    parserTwo = DemoParser(demoName)
    last_tick = parserTwo.parse_event("round_end")["tick"].to_list()[-1]
    dfTwo = parserTwo.parse_ticks(["crosshair_code"],ticks=[last_tick])
    df_for_aim_two = parserTwo.parse_ticks(["pitch", "yaw"])
    




    predictions

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
