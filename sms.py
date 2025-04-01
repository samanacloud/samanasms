import sys
import logging
from slack_sdk import WebClient
from flask import request, Flask
import os
import json

app = Flask(__name__)
log = logging.getLogger(__name__)

@app.route("/sms")
def sms():
    dest = phonemap.get(request.args.get('to'))
    if request.args.get('api-key') != nexmoapikey:
        log.error(f"Invalid nexmo api key. {request.args}")
        return ""
    if dest is None:
        log.error(f"Destination doesn't exist {request.args}")
        return
    msg = [
            "====================================",
            f"Message from: {request.args.get('msisdn')}",
            f"Received at: {request.args.get('message-timestamp')}",
            "------------------------------------",
            f"{request.args.get('text')}",
            "===================================="
    ]
    response = client.chat_postMessage(channel=dest, text="\n".join(msg))
    if not response.get("ok", False):
        log.error(f"Message could not be sent. {str(response)}")
        return ""
    return ""

@app.route("/")
def index():
    return ""

token = os.getenv("SLACK_TOKEN")
nexmoapikey = os.getenv("NEXMO_API_KEY")
with open("numbermaps.json", "r") as f:
    phonemap = json.load(f)
client = WebClient(token=token)
