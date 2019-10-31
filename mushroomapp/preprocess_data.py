import numpy as np
import pandas as pd
from sklearn.preprocessing import OneHotEncoder, LabelEncoder


class PreprocessData:
    def __init__(self, data):
        self.data = data

    def create_preprocessed_dataframe(self):
        data_values = self.data.values()
        mushroom_input = pd.DataFrame(list(data_values))
        return self.encoder(mushroom_input)

    def encoder(self, arg):
        one_hot = OneHotEncoder()
        mushroom_features = one_hot.fit_transform(arg).toarray()
        mushroom_features_df = pd.DataFrame(mushroom_features)
        return mushroom_features_df
