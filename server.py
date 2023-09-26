import os
import logging

from flask import Flask, request
from flask_cors import CORS, cross_origin

from util import get_country
from users.login import login
from users.register import (normal_signup, cont_normal_signup, update_normal_signup)
from users.verify import (email_verification, phone_number_verification)
from users.persistence import get_user_personal_info

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
    
    
    # ACCOUNT CREATION
    if msg_subject == "login_normal":
        return login(msg_received)

    elif msg_subject == "register_normal":
        return update_normal_signup.register(msg_received, header)

    elif msg_subject == "update_registration":
        return cont_normal_signup.update(msg_received, header)
    
    elif msg_subject == "sendVerification":
        if msg_received["form"] == "email":
            return email_verification.send(msg_received)

        elif msg_received["form"] == "phoneNumber":
            return phone_number_verification.send(msg_received)
        else:
            return {"Message": "Wrong form provided (1)", "statusCode": 401}
    
    # core functions
    elif  msg_subject == 'fert_recommend':
         return fert_recommend(header,msg_received)
    
    elif  msg_subject == 'crop_recommend':
         return recommend(header, msg_received)
    
    elif  msg_subject == 'crop_disease':
         return disease(header, msg_received)
    
    # UTIL
    elif msg_subject == "getCountry":
        return get_country.get(ip)

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
