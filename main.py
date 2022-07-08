from twilio.twiml.messaging_response import MessagingResponse
from twiliohelper import *
from flask import *

app = Flask(__name__)
initTwilio(app)

@app.route("/msg", methods=["POST"])
def on_message():
  message = request.sender + " texted \"" + request.message + "\""
  print(message)
  return sendMessage(message)

app.run(host="0.0.0.0")
