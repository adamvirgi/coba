from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    model = joblib.load('model.joblib')
    prediction = model.predict(final_features)
    output = int(prediction[0])
    if output == 0:
        result = 'Stunted'
    elif output == 1:
        result = 'Tall'
    elif output == 2:
        result = 'Normal'
    else:
        result = 'Severely Stunted'
    return render_template('index.html', prediction_text='Status: {}'.format(result))

if __name__ == "__main__":
    app.run(debug=True)
