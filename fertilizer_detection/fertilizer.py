from fertilizer_detection.fertilizer_dic import fertilizer_dic
import pandas as pd

def fert_recommend(msg_received):
    try:
        crop_name = str(msg_received['cropname'])
        N = int(msg_received['nitrogen'])
        P = int(msg_received['phosphorous'])
        K = int(msg_received['pottasium'])
        # ph = float(msg_received['ph'])

        df = pd.read_csv('Data/FertilizerData.csv')

        nr = df[df['Crop'] == crop_name]['N'].iloc[0]
        pr = df[df['Crop'] == crop_name]['P'].iloc[0]
        kr = df[df['Crop'] == crop_name]['K'].iloc[0]

        n = nr - N
        p = pr - P
        k = kr - K
        temp = {abs(n): "N", abs(p): "P", abs(k): "K"}
        max_value = temp[max(temp.keys())]
        if max_value == "N":
            if n < 0:
                key = 'NHigh'
            else:
                key = "Nlow"
        elif max_value == "P":
            if p < 0:
                key = 'PHigh'
            else:
                key = "Plow"
        else:
            if k < 0:
                key = 'KHigh'
            else:
                key = "Klow"

        response = str(fertilizer_dic[key])
        # response = jsonify(response)
        return {"response": f"{response}", }
    except Exception as e:
        return {"Error": str(e), "statusCode": 600}