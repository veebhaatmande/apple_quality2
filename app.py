from flask import Flask, request, render_template
from flask import jsonify
from utils import get_apple_quality
import config

# Initialize Flask Application
app = Flask(__name__)
prediction=''
# Define Route

@app.route('/')
def home():
    return render_template('index.html')

# This api is use to predict apple quality. 
@app.route('/predict_apple_quality', methods=['POST'])
def apple_quality():
    print("*"*50)
    #data = request.form
    data = request.json
    print("data ", data)
    Size = float(data['Size'])
    Weight = float(data['Weight'])
    Sweetness = float(data['Sweetness'])
    Crunchiness = float(data['Crunchiness'])
    Juiciness = float(data['Juiciness'])
    Ripeness = float(data['Ripeness'])
    Acidity = float(data['Acidity'])
    print("*"*50)
    result = get_apple_quality(Size, Weight, Sweetness,Crunchiness,Juiciness,Ripeness,Acidity)
    print("*"*50)
    if result==1:
        prediction = "Good"
    else:
        prediction = "Bad"

    print("quality ", prediction)
    return jsonify({'prediction': prediction})

# Added to test commit on got repository.
@app.route('/predict_apple_quality_test', methods=['POST'])
def apple_quality_test_api():
    return jsonify({'prediction': 'Good'})


if __name__ == "__main__":

    app.run(host='0.0.0.0',port=5002,debug=False)