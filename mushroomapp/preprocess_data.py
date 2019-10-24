import numpy as np
import pandas as pd
from sklearn.preprocessing import OneHotEncoder, LabelEncoder

class PreprocessData:
    def __init__(self, data):
        self.data = data

    def myfunc(self):
        data_values = self.data.values()
        mushroom_input = pd.DataFrame(list(data_values))
        self.encoder(mushroom_input)

    def encoder(self, arg):
        one_hot = OneHotEncoder()
        mushroom_features = one_hot.fit_transform(arg).toarray()
        print(mushroom_features)
        mushroom_features_df = pd.DataFrame(mushroom_features) 
        return mushroom_features_df       

# 'cap-surface' 'cap-color' 'bruises'	'odor'	'gill-attachment'	'gill-spacing'	'gill-size'	'gill-color'	...	'stalk-surface-below-ring'	'stalk-color-above-ring'	'stalk-color-below-ring'	'veil-type'	'veil-color'	'ring-number'	'ring-type'	'spore-print-color'	'population'	'habitat'