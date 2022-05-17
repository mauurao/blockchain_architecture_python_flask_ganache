"""
This script is responsible for linking the application frontend built in html with the blockchain services simulation script in ganache.  
Created by Mauro Cardoso, 27 of April 2022, 01:55
"""

from backend import *
from flask import Flask, render_template, request

app = Flask(__name__) # instance of the flask class

@app.route('/', methods=['POST','GET']) #Handler of the url request   
def index():
    if request.method == 'POST':
        pass
    return render_template('index.html')


@app.route('/contract_regulator', methods=['POST','GET']) #Handler of the url request   
def contract_regulator():
    if request.method == 'POST':
        create_regulator_contract()
    return render_template('index.html')        

@app.route('/transaction_regulator', methods=['POST','GET']) #Handler of the url request   
def transaction_regulator():
    if request.method == 'POST':
        create_transaction_regulator_to_manufacturer()
    return render_template('index.html')


@app.route('/contract_hospital', methods=['POST','GET']) #Handler of the url request   
def contract_hospital():
    if request.method == 'POST':
        create_hospital_contract()
    return render_template('index.html')


@app.route('/transaction_hospital', methods=['POST','GET']) #Handler of the url request   
def transaction_hospital():
    if request.method == 'POST':
        h_Value = request.form.get('h_Value')
        create_transaction_hospital(h_value = h_Value)
    return render_template('index.html')


@app.route('/contract_distribuitor', methods=['POST','GET']) #Handler of the url request   
def contract_distribuitor():
    if request.method == 'POST':
        create_distribuitor_contract()
    return render_template('index.html')


@app.route('/transaction_distribuitor', methods=['POST','GET']) #Handler of the url request   
def transaction_distribuitor():
    if request.method == 'POST':
        d_Value = request.form.get('d_Value')
        create_transaction_distribuitor(d_value = d_Value)
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True) # Entrance of the app
    # dev server in terminal -> python project name
