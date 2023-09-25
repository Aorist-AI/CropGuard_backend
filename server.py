from flask import Flask, request
from flask_cors import CORS, cross_origin

from users import login, signup
from fertilizer_detection.fertilizer import fert_recommend
from crop_detection.crop_prediction import crop_prediction 
from disease_detection.disease import disease

app = Flask(__name__)
CORS(app)

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
         return crop_prediction(msg_received)
    elif  msg_subject == 'crop_disease':
         return disease(msg_received)
    else:
        return {"Message": "Wrong subject provided to Crop_guard", "statusCode": 404}
    