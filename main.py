# -*- coding: utf-8 -*-

from flask import Flask, request, jsonify
from neoApiClient import (initializeClient, createSessionUsingOtp, loginGetOtp, placeOrder, getOrderBook,
                          getMasterScripFilePaths)

app = Flask(__name__)

data_store = []


@app.route('/api/data', methods=['POST'])
def add_data():
    try:
        data = request.json  # Assuming the incoming data is in JSON format
        data_store.append(data)
        print(data["name"])
        return data, 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400


@app.route('/otp', methods=['POST'])
def otp():
    createSessionUsingOtp(request)
    return request.json, 201


@app.route('/placeOrder', methods=['POST'])
def order():
    placeOrderResponse = placeOrder(request)
    return placeOrderResponse, 201


@app.route('/orderBook', methods=['POST'])
def orderBook():
    return getOrderBook(), 201


@app.route('/masterScriptFilePaths', methods=['POST'])
def masterScripFilePath():
    return getMasterScripFilePaths(), 201


if __name__ == 'main':
    initializeClient()
    loginGetOtp()
    app.run(debug=True, port=5002)
