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

    return render_template("homepage.html")


# create a route for the incoming SMS to be received
@app.route("/sms", methods=['Get', 'POST'])
def sms_reply():
    resp = MessagingResponse()

    resp.message("A tasty treat awaits every patient dog.")

    return str(resp)


# run the Flask app when calling the file
if __name__ == "__main__":
    app.debug = True
    app.run(port=5000, host='0.0.0.0')


