from flask import Flask, request, Response
from flask_slack import Slack
from app import *


app = Flask(__name__)

SLACK_WEBHOOK_SECRET = os.environ.get('SLACK_WEBHOOK_SECRET')
SLACK_RAGE_BOT = os.environ.get('SLACK_RAGE_BOT')
@app.route('/slack', methods=['POST'])
def inbound():
    if request.form.get('token') == SLACK_WEBHOOK_SECRET:
        channel = request.form.get('channel_name')
        username = request.form.get('user_name')
        channel_id = get_channel_id_from_name(channel)
        message = request.form.get('text')[5:]
        send_message(channel_id=channel_id, message=message)
        return Response(), 200


@app.route('/rage', methods=['POST'])
def RAGE():
    print(request.form.get('text'))
    if request.form.get('token') == SLACK_RAGE_BOT:
        # channel = request.form.get('channel_name')
        # channel_id = get_channel_id_from_name(channel)

       #  send_message(channel_id=channel_id, message=request.form.get('text'))
        response = {'response_type' : 'ephemeral',
		'text': 'yee',
	}
	return request.form.get('text')
    return None

@app.route('/botsco', methods=['POST'])
def BOTSCO():
    if request.form.get('token') == 'MEtufTdVQi9ssXynjZRO8Gif':
        channel = request.form.get('channel_name')
        channel_id = get_channel_id_from_name(channel)

        send_message(channel_id=channel_id, message=request.form.get('text'))
        return Response(), 200

@app.route('/', methods=['GET'])
def test():
    return Response('It works!')


if __name__ == "__main__":
    app.run(debug=True)

