from flask import Flask, request, render_template
import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler
from src.pipeline.prediction_pipeline import CustomData, PredictPipeline


application = Flask(__name__)

app = application

# Create Route for Home Page

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predictdata', methods = ['GET', 'POST'])
def predict_datapoint():
    if request.method == 'GET':
        return render_template('home.html')
    else:
        data=CustomData(
            gender=request.form.get('gender'),
            race_ethnicity=request.form.get('ethnicity'),
            parental_level_of_education=request.form.get('parental_level_of_education'),
            lunch=request.form.get('lunch'),
            test_preparation_course=request.form.get('test_preparation_course'),
            reading_score=float(request.form.get('writing_score')),
            writing_score=float(request.form.get('reading_score'))
        )
        prediction_df = data.get_data_as_data_frame()
        print(prediction_df)

        predict_pipeline = PredictPipeline()
        results = predict_pipeline.predict(prediction_df)
        return render_template('home.html', results = results[0])

def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()

@app.get('/shutdown')
def shutdown():
    shutdown_server()
    return 'Server shutting down...'

if __name__ == "__main__":
    app.run(host="0.0.0.0")



