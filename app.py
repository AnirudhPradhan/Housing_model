import numpy as np
from flask import Flask, request , jsonify, render_template
import pickle
# Create a flask app
app= Flask(__name__)

# load the pickle model
model=pickle.load(open("model.pkl","rb"))

@app.route("/")
def HOME():
    return render_template("index.html")

@app.route("/predict",methods=["POST"])
def predict():
    float_features= [float(x) for x in request.form.values()]
    features= [np.array(float_features)]
    prediction= model.predict(features)

    return render_template("index.html", prediction_text= " the price of the house is {}".format(prediction[0]))

if __name__=="__main__":
    app.run(debug=True)