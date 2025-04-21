from flask import Flask, request, jsonify
import numpy as np
from tensorflow.keras.models import load_model
from demoparser2 import DemoParser

# Create a Flask application instance
app = Flask(__name__)


#load my pretrained model

model = load_model("myAntiCheatModel")

# Define a route for my frontend that compares the aim to the suspect to my model build from analyse pro player aim
@app.route('/predict' , method=["POST"])
def predict():          

    demoName = ""
    suspectName = ""
    prohability = ""
    parserTwo = DemoParser(demoName)
    last_tick = parserTwo.parse_event("round_end")["tick"].to_list()[-1]
    dfTwo = parserTwo.parse_ticks(["crosshair_code"],ticks=[last_tick])
    df_for_aim_two = parserTwo.parse_ticks(["pitch", "yaw"])
    

    #::TODO create a method to be able to use the model on the input name !!!


    predictions = model.predict(df_for_aim_two)
    predictions_binary = (predictions > 0.5).astype(int)
    # condition to check if  the model predicts a cheater or not 
    if predictions_binary.sum() > 0:
        ## using sum here cause i get an array of 0 and 1 in the prediction
        result = "most likey a cheater"
    
    else:
        result = "not a cheater" 

    return jsonify({"result": result})






# Run the application
if __name__ == '__main__':
    app.run(debug=True)
