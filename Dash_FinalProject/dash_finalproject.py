from flask import Flask, render_template, request
import joblib
import pickle
import pandas as pd

app = Flask(__name__)

#halaman home
@app.route('/')
def home():
    return render_template('home.html')

#halaman dataset
@app.route('/database', methods=['POST', 'GET'])
def dataset():
    return render_template('dataset.html')

# #halaman visualisasi
@app.route('/visualize', methods=['POST', 'GET'])
def visual():
    return render_template('plot.html')

# #halaman input prediksi
@app.route('/predict', methods = ['POST', 'GET'])
def predict():
    return render_template('predict.html')

# #halaman hasil prediksi
@app.route('/result', methods = ['POST', 'GET'])
def result():
    if request.method == 'POST':
        input = request.form

        df_predict = pd.DataFrame({
            '10percentage':[input['10percentage']],
            '12percentage':[input['12percentage']],
            '12graduation':[input['12graduation']],
            'GraduationYear':[input['GraduationYear']],
            'collegeGPA':[input['collegeGPA']],
            'English':[input['English']],  
            'Quant':[input['Quant']], 
            'Domain':[input['Domain']],
            'Gender':[input['Gender']],
            '10board':[input['10board']],
            '12board':[input['12board']],
            'CollegeTier':[input['CollegeTier']],
            'Specialization':[input['Specialization']], 
            'CollegeState':[input['CollegeState']]
        })


        prediksi = model.predict(df_predict)

        return render_template('result.html',
            data=input, pred=prediksi)

if __name__ == '__main__':
    # model = joblib.load('model_joblib')

    filename = 'C:/Users/LENOVO/Documents/PURWADHIKA/Final Project/Dash_FinalProject/Final_ElasticNet.sav'
    model = pickle.load(open(filename,'rb'))

    app.run(debug=True)