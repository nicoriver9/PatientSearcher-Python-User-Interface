from flask import Flask, render_template, request
from flask_cors import CORS, cross_origin
import requests

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method == 'POST':        
        
        userForm        = request.form['data1'].replace(" ", "")
        passwordForm    = request.form['data2'].replace(" ", "")
        hcForm          = request.form['data3'].replace(" ", "")
        dniForm         = request.form['data4'].replace(" ", "")
        
        if hcForm == '':
            hcForm = -1
        if dniForm == '':
           dniForm = -1

        payload = {
            "user" : userForm ,
            "password" : passwordForm ,
            "dni" : dniForm ,
            "hc" : hcForm ,
        }

        urlToken = 'http://10.101.5.54:8001/'
        response = requests.get(urlToken, json=payload)
        data = response.json()
        token = data['token'] 
        headers = {'token': token}

        url = 'http://10.101.5.54:8000/paciente/'
        responsePatient = requests.post(url, json=payload, headers = headers)        
        
        return responsePatient.text
        
    if request.method == 'GET':        
        return render_template('index.html')

if __name__ == '__main__':
    app.run()
