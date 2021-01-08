from flask import Flask, request, redirect, url_for, flash, jsonify
from sklearn.preprocessing import StandardScaler
import numpy as np
import pickle as p
import json


app = Flask(__name__)


@app.route('/api/', methods=['POST'])
def prediction():
    data = request.get_json()
    data = sc.transform(data)
    prediction = np.array2string(model.predict(data))

    return jsonify(prediction)

if __name__ == '__main__':
    modelfile = 'models/randomforest.pickle'
    model = p.load(open(modelfile, 'rb'))
    scaler = 'models/scaler.pkl'
    sc = p.load(open(scaler,'rb'))
    app.run(debug=True)