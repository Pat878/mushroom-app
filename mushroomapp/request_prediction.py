import requests
import os
import numpy as np
import ast


class RequestPrediction:
    def __init__(self, data):
        self.data = data

    def submit_dataframe(self):
        URL = os.getenv("API_LINK")
        test = [0., 0., 1., 0., 0., 0., 1., 0., 0., 0., 0., 0., 0., 0., 1., 0., 0.,
                0., 0., 0., 1., 0., 0., 0., 0., 0., 0., 1., 0., 0., 0., 0., 1., 0.,
                1., 1., 0., 0., 0., 0., 1., 0., 0., 0., 0., 0., 0., 0., 0., 0., 1.,
                0., 0., 0., 1., 0., 0., 0., 1., 0., 1., 0., 0., 0., 0., 0., 0., 0.,
                0., 0., 0., 1., 0., 0., 0., 0., 0., 0., 0., 0., 1., 0., 1., 0., 0.,
                1., 0., 0., 1., 0., 1., 0., 0., 0., 0., 0., 0., 0., 1., 0., 0., 0.,
                0., 0., 0., 0., 0., 1., 0., 0., 0., 1., 0., 0., 0., 0., 0.]
        PARAMS = np.array(test).astype(int).tolist()
        # print(np.array(self.data.astype(int).values[0]).astype(int).tolist())

        r = requests.post(url=URL, json=PARAMS)
        response = ast.literal_eval(
            r.text)['predictions'][0]['predicted_label']

        return response
