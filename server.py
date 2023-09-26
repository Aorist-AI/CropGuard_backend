import os
import logging

from flask import Flask, request
from flask_cors import CORS, cross_origin

from users import login, signup
from fertilizer_detection.fertilizer import fert_recommend
from crop_recommendation.crop_recommendation import recommend
from disease_detection.disease import disease
from flask_socketio import SocketIO, emit, join_room

# from safeproxyfix import  SaferProxyFix

app = Flask(__name__)

socketio = SocketIO(app, cors_allowed_origins="*")  # ,async_mode="gevent_uwsgi"
app.config["socket"] = socketio
CORS(app)
cwd = os.getcwd()

app.config["DOWNLOAD"] = os.path.join(cwd, "download#stats")
try:
    os.mkdir(app.config["DOWNLOAD"])
except:
    pass


@app.route('/', methods=["GET", "POST"])
@cross_origin(origin='*')
def agro_ai():
    header = request.headers.get('Authorization')
    headers_list = request.headers.getlist("X-Forwarded-For")
    e = headers_list  # headers_list[0] if headers_list else request.remote_addr
    ip = str(e).split(",")[0]

    disallowed_characters = "[<>]/*-;+/:()%$#@!/?_\""

    for character in disallowed_characters:
        ip = ip.replace(character,'')
    msg_received = request.get_json()
    try:
        msg_subject = msg_received["subject"]
    except (KeyError, TypeError):
        return {"Message": "No subject provided to AgroAI", "statusCode": 404}
    
    if msg_subject == 'login':
        return login.login(msg_received)
    elif  msg_subject == 'signup':
         return signup(msg_received)
    elif  msg_subject == 'fert_recommend':
         return fert_recommend(msg_received)
    elif  msg_subject == 'crop_recommend':
         return recommend(msg_received)
    elif  msg_subject == 'crop_disease':
         return disease(msg_received)
    else:
        return {"Message": "Wrong subject provided to Crop_guard", "statusCode": 404}
    
    
def log(info):
    gunicorn_logger = logging.getLogger("gunicorn.error")
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)
    app.logger.critical(info)


if __name__ == "__main__":
    # pip install pyopenssl
    # app.run(host="0.0.0.0", port=5004, debug=True, threaded=True)
    socketio.run(app, host="0.0.0.0", port=5004, debug=True,
                 allow_unsafe_werkzeug=True)  # threaded=True, allow_unsafe_werkzeug=True
