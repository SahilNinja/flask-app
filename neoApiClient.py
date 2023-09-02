from neo_api_client import NeoAPI
from credentials import access_token, mobile_number, login_password

client = NeoAPI


def on_message(message):
    print(message)


def on_error(error_message):
    print(error_message)


def initializeClient():
    global client
    client = NeoAPI(access_token=access_token, environment='PROD', on_message=on_message, on_error=on_error,
                    on_close=None, on_open=None)
    print("initializeClient result :: ")
    print(client)


def loginGetOtp():
    global client
    result = client.login(mobilenumber=mobile_number, password=login_password)
    print("client login result :: ")
    print(result)


def createSessionUsingOtp(request):
    data = request.json
    otp = data["otp"]
    global client
    client.session_2fa(OTP=otp)


def placeOrder(request):
    global client
    data = request.json
    print("request data :: ")
    print(data)
    response = client.place_order(
        exchange_segment=data["exchange_segment"],
        product=data["product"],
        order_type=data["order_type"],
        quantity=data["quantity"],
        validity=data["validity"],
        price=data["price"],
        trading_symbol=data["trading_symbol"],
        transaction_type=data["transaction_type"],
        amo=data["amo"]
    )
    print("place order response :: ")
    print(response)
    return response


def getOrderBook():
    global client
    return client.order_report()


def getMasterScripFilePaths():
    global client
    return client.scrip_master()
