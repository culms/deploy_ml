import pickle
import numpy as np
import pandas as pd
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

with open('model.pkl', 'rb') as file:
    model = pickle.load(file)
model_result = ['Less - Likely', 'More - Likely']


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)
    proba = model.predict_proba(final_features)[0].max()
    res = model_result[prediction[0]]
    return render_template('index.html', prediction_text='Result = {}, \n Chances = {}'.format(res,proba))


@app.route('/predict_api', methods=['POST'])
def predict_api():
    # For direct API calls trought request
    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])
    return jsonify(model_result[prediction])


if __name__ == '__main__':
    app.run(debug=True)
