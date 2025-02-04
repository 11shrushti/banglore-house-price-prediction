from flask import Flask, request,jsonify 
import util
app = Flask(__name__)


@app.route("/")
def get_location__names():
    response = jsonify({
        "location" : util.get_location_names()
    })
    response.header.add("Access-Control-Allow-oriigin", "*")
    return response
    
@app.route("/prdict_home_price", methods = ["POST"])
def predict_home_price():
    total_sqft = float(request.form["total_sqft"])
    location = request.form["location"]
    bhk = int(request.form["bhk"])
    bath = int(request.form["bath"])

    response = jsonify({
        "estimated_price" : util.get_estimated_price(location,total_sqft,bhk,bath)
    })

    response.headers.add("Access-Control-Allow-Origin","*")

    return response



if __name__ == "__main__":
    print("Starting Pyhton Flask Server for the Home Price Prediction...")
    app.run()