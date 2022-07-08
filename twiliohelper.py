from twilio.twiml.messaging_response import MessagingResponse
from flask import request

def initTwilio(app):
  @app.before_request
  def addAttr():
    request.message = request.form["Body"]
    request.sender = request.form["From"]

def sendMessage(message):
  msg_resp = MessagingResponse()
  msg = msg_resp.message()
  msg.body(message)
  return str(msg_resp)
