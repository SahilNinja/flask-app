from flask import Flask, request, jsonify
import neoApiClient

app = Flask(__name__)
neoApiClient.initializeClient()
neoApiClient.loginGetOtp()

data_store = []


@app.route('/')
def hello_world():
    return 'Hello, World!'


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
    neoApiClient.createSessionUsingOtp(request)
    return request.json, 201


@app.route('/placeOrder', methods=['POST'])
def order():
    placeOrderResponse = neoApiClient.placeOrder(request)
    return placeOrderResponse, 201


@app.route('/orderBook', methods=['POST'])
def orderBook():
    return neoApiClient.getOrderBook(), 201


@app.route('/masterScriptFilePaths', methods=['POST'])
def masterScripFilePath():
    return neoApiClient.getMasterScripFilePaths(), 201
