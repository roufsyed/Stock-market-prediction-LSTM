import numpy as np
from flask import Flask, request,  render_template
import pickle
import tensorflow as tf
app = Flask(__name__)
# model = pickle.load(open('model.pkl', 'rb'))
from tensorflow import keras
model = tf.keras.models.load_model('model', custom_objects={'leaky_relu': tf.nn.leaky_relu})
# model = keras.models.load_model('model')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [[float(x)] for x in request.form.values()]
    prediction = model.predict([int_features])
    prediction1 = "Predicted Open for tomorrow is: " + str(prediction[0][0])
    prediction2 = "Predicted Close for tomorrow is: " + str(prediction[0][1])
    prediction3 = "Predicted High for tomorrow is: " + str(prediction[0][2])
    prediction4 = "Predicted Low for tomorrow is: " + str(prediction[0][3])
    prediction5 = "Predicted Adjusted Low for tomorrow is: " + str(prediction[0][4])


        


    return render_template('index.html', prediction_text1=prediction1,prediction_text2=prediction2,prediction_text3=prediction3,prediction_text4=prediction4,prediction_text5=prediction5)



if __name__ == "__main__":
    app.run(debug=True)