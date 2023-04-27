import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__) #Initialize the flask App
model = pickle.load(open('model3.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index2.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    feature1=int(request.form['age'])*365
    feature2=int(request.form['gender'])
    feature3=int(request.form['height'])
    feature4=float(request.form['weight'])
    feature5=int(request.form['ap_hi'])
    feature6=int(request.form['ap_lo'])
    feature7=int(request.form['cholesterol'])
    feature8=int(request.form['gluc'])
    feature9=int(request.form['smoke'])
    feature10=int(request.form['alco'])
    feature11=int(request.form['active'])
    int_features=[feature1,feature2,feature3,feature4,feature5,feature6,feature7,feature8,feature9,feature10,feature11]
    #int_features = [int(x) for x in int_features]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    output = prediction

    return render_template('index2.html', prediction_text='Chances of getting Cardio Vascular Diseases  {}%'.format(output))

if __name__ == "__main__":
    app.run(debug=True)
