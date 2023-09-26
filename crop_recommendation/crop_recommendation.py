import numpy as np
import pickle
from agro_config.config import weather_config
import requests

def recommend(msg_received):
    try:
        N = int(msg_received['nitrogen'])
        P = int(msg_received['phosphorous'])
        K = int(msg_received['pottasium'])
        ph = float(msg_received['ph'])
        rainfall = float(msg_received['rainfall'])

        # state = request.form.get("stt")
        city = msg_received['city']

        if city != None:
            temperature, humidity = weather_fetch(msg_received)
            data = np.array([[N, P, K, temperature, humidity, ph, rainfall]])
            my_prediction = crop_recommendation_model.predict(data)
            final_prediction = my_prediction[0]

            return  final_prediction

        else :
            return {
                "code": -1,
                "msg": "Unknown Error please try again",
            }
    except Exception as e:
        return {
            "code": -1,
            "msg": str(e),
        }


def weather_fetch(msg_received):
    """
    Fetch and returns the temperature and humidity of a city
    :params: city_name
    :return: temperature, humidity
    """
    try:
            
        city_name = msg_received['city']
        key = weather_config()
        api_key = key['weather_api_key']
        api_key = str(api_key)
        base_url = "http://api.openweathermap.org/data/2.5/weather?"

        complete_url = base_url + "appid=" + api_key + "&q=" + city_name
        response = requests.get(complete_url)
        x = response.json()
        
            # Alternative
        # Check if the 'main' key exists in the dictionary.
        # if "main" in x.keys():
        #     # Get the temperature and humidity from the dictionary.
        #     temperature = x["main"]["temp"]
        #     humidity = x["main"]["humidity"]

        #     return str(temperature), str(humidity)
                  
        # else:
        #     # The 'main' key does not exist, so raise an error.
        #     raise KeyError("The 'main' key does not exist in the weather data response.")
        
        if x["cod"] != "404":
            y = x["main"]
            print(y)
            temperature = round((y["temp"] - 273.15), 2)
            humidity = y["humidity"]
            return temperature, humidity
        else:
            raise KeyError("The 'main' key does not exist in the weather data response.")
    except Exception as  e:
        return {"error": str(e)}

crop_recommendation_model_path = 'Trained_Model/RandomForest.pkl'
crop_recommendation_model = pickle.load(
    open(crop_recommendation_model_path, 'rb'))
