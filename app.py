#!/usr/bin/python3
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({'status' : 'Rodando... nao consegue'})

@app.route('/nova-rota')
def nova_rota():
    return jsonify({'rota' : 'rota TRE'})

app.run(host='0.0.0.0', port=8080)
