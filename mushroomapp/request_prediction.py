import requests
import os
import numpy as np
import ast


class RequestPrediction:
    def __init__(self, data):
        self.data = data

    def submit_dataframe(self):
        URL = os.getenv("API_LINK")
        PARAMS = self.data

        r = requests.post(url=URL, json=PARAMS)
        response = ast.literal_eval(
            r.text)['predictions'][0]['predicted_label']

        return response
