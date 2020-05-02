import os
from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse

# create a Flask app
app = Flask(__name__)

app.secret_key = "ABC"
# app.jinja_env.undefined = StrictUndefined


@app.route('/')
def index():
    """Homepage."""
    return '<html><body>Hello</body></html>'


# create a route for the incoming SMS to be received
@app.route("/sms", methods=['Get', 'POST'])
def sms_reply():
    resp = MessagingResponse()

    resp.message("A honey pot full of happiness awaits the hard working bear.")

    return str(resp)


# run the Flask app when calling the file
if __name__ == "__main__":
    app.debug = True
    app.run(port=5000, host='0.0.0.0')


