import os
import requests
import json
from config import my_number, account_sid, auth_token
from flask import Flask, render_template, request
from twilio.rest import Client

app = Flask(__name__)

client = Client(account_sid, auth_token)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        message = request.form['message']
        client.messages.create(
            to=my_number,
            from_="+14159407338",
            body=message)
        return render_template('success.html', message=message)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8000))
    app.run(host='0.0.0.0', port=port, debug=True)

