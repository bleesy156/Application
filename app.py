from flask import Flask,render_template,request
import pickle 
import numpy as np 
import os
print(os.getcwd())


model = pickle.load(open('model.pkl','rb'))
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict_quality():
    aluminium = float(request.form.get('aluminium'))
    ammonia = float(request.form.get('ammonia'))
    arsenic = float(request.form.get('arsenic'))
    barium= float(request.form.get('barium'))
    cadmium = float(request.form.get('cadmium'))
    chloramine = float(request.form.get('chloramine'))
    chromium = float(request.form.get('chromium'))
    copper = float(request.form.get('copper'))
    flouride = float(request.form.get('flouride'))
    bacteria = float(request.form.get('bacteria'))
    viruses = float(request.form.get('viruses'))
    lead = float(request.form.get('lead'))
    nitrates = float(request.form.get('nitrates'))
    nitrites = float(request.form.get('nitrites'))
    mercury = float(request.form.get('mercury'))
    perchlorate = float(request.form.get('perchlorate'))
    radium = float(request.form.get('radium'))
    selenium = float(request.form.get('selenium'))
    silver = float(request.form.get('silver'))
    uranium = float(request.form.get('uranium'))

    #prediction
    result = model.predict(np.array([aluminium,ammonia,arsenic,barium,cadmium,chloramine,chromium,copper,flouride,bacteria,viruses,lead,nitrates,nitrites,mercury,perchlorate,radium,selenium,silver,uranium]).reshape(1,20))

    if result[0] == 1:
        result ='Fit for Drinking'
    else:
        result ='Unfit' 

    return render_template('index.html',result=result)

    

if __name__ == "__main__":
    app.run(debug = True, host = '0.0.0.0', port = 8080)