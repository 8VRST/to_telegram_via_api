import json
from flask import Flask, request, Response

from bot import send_info_to_bot, bot, time
from messages_blanks import main_info


credentials_file = open('creds.json')
server_credentials = json.load(credentials_file)["server"]


app = Flask(__name__)


@app.route('/send_info/', methods=['POST'])
def send_info():

    secret_key = server_credentials["key"]
    header_secret_key = request.headers["Key"]

    client_name = request.form["Name"]
    client_phone_number = request.form["Contact-Number"]
    telegram_username = request.form["Telegram-Username"]
    message_from_app = request.form["Text-Message"]
    pdf_file = request.form["Attached-Pdf"]
    design_photo = request.form["Attached-Picture"]

    message = main_info(client_name=client_name, client_phone_number=client_phone_number,
                        telegram_username=telegram_username, message_from_app=message_from_app)

    if header_secret_key != secret_key:
        return Response(status=401, mimetype='application/json')
    else:
        send_info_to_bot(info=message, pdf_file=pdf_file, design_photo=design_photo)
        return "The info has been sent"


if __name__ == '__main__':
    app.run(host=server_credentials["host"], port=server_credentials["port"])