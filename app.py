import pickle
import numpy as np
from flask import Flask, render_template, request

app = Flask(__name__)

# Load the saved model
with open('gwp.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        # Collect form data in the same order as your model features
        features = [
            float(request.form['quarter']),
            float(request.form['department']),
            float(request.form['day']),
            float(request.form['team']),
            float(request.form['targeted_productivity']),
            float(request.form['smv']),
            float(request.form['over_time']),
            float(request.form['incentive']),
            float(request.form['idle_time']),
            float(request.form['idle_men']),
            float(request.form['no_of_style_change']),
            float(request.form['no_of_workers']),
            float(request.form['month'])
        ]
        final_features = np.array(features).reshape(1, -1)
        prediction = model.predict(final_features)[0]
        return render_template('submit.html', prediction=prediction)
    return render_template('predict.html')

if __name__ == "__main__":
    app.run(debug=True)