from signalwire.voice_response import *
from flask import Flask, request, render_template
import os
from pyngrok import ngrok
from signalwire.rest import Client as signalwireClient
from dotenv import load_dotenv

load_dotenv()

# Set up ngrok tunnel
SIGNALWIRE_PROJECT_KEY = os.environ['SIGNALWIRE_PROJECT_ID']
SIGNALWIRE_TOKEN = os.environ['SIGNALWIRE_API_TOKEN']
SIGNALWIRE_SPACE = os.environ['SIGNALWIRE_SPACE_URL']
SIGNALWIRE_NUMBER = os.environ['SIGNALWIRE_FROM_NUMBER']

swClient = signalwireClient(SIGNALWIRE_PROJECT_KEY, SIGNALWIRE_TOKEN, signalwire_space_url=SIGNALWIRE_SPACE)

ngrok.set_auth_token(os.environ['NGROK_AUTH_TOKEN'])
public_url = ngrok.connect()

app = Flask(__name__)


@app.route("/")
def ai_prompt():
    # This should work once

    print()
    print()
    print('Sending message using ph: ' + SIGNALWIRE_NUMBER)
    print()
    print()

    success = swClient.messages.create(to='+14074632925', from_=SIGNALWIRE_NUMBER, body='Important! Grandma Lisa had a high blood sugar reading as of March 24th, 2024. Please verify with her that insulin is being taken appropriately.')

    return render_template('/index.html')


if __name__ == '__main__':
    # Show ngrok URL and tunnel
    print()
    print(public_url)
    print()

    # Run flask server
    app.run(host="0.0.0.0", port=80)
