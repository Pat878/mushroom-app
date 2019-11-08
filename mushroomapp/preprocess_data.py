import numpy as np
import pandas as pd
from sklearn.preprocessing import OneHotEncoder, LabelEncoder


class PreprocessData:
    def __init__(self, data):
        self.data = data

    def create_preprocessed_values(self):
        # Calling get_feature_names() on the OneHotEncoder returns the following names
        cols = ['x0_b', 'x0_c', 'x0_f', 'x0_k', 'x0_s', 'x0_x', 'x1_f', 'x1_g',
                'x1_s', 'x1_y', 'x2_b', 'x2_c', 'x2_e', 'x2_g', 'x2_n', 'x2_p',
                'x2_r', 'x2_u', 'x2_w', 'x2_y', 'x3_f', 'x3_t', 'x4_a', 'x4_c',
                'x4_f', 'x4_l', 'x4_m', 'x4_n', 'x4_p', 'x4_s', 'x4_y', 'x5_a',
                'x5_f', 'x6_c', 'x6_w', 'x7_b', 'x7_n', 'x8_b', 'x8_e', 'x8_g',
                'x8_h', 'x8_k', 'x8_n', 'x8_o', 'x8_p', 'x8_r', 'x8_u', 'x8_w',
                'x8_y', 'x9_e', 'x9_t', 'x10_?', 'x10_b', 'x10_c', 'x10_e',
                'x10_r', 'x11_f', 'x11_k', 'x11_s', 'x11_y', 'x12_f', 'x12_k',
                'x12_s', 'x12_y', 'x13_b', 'x13_c', 'x13_e', 'x13_g', 'x13_n',
                'x13_o', 'x13_p', 'x13_w', 'x13_y', 'x14_b', 'x14_c', 'x14_e',
                'x14_g', 'x14_n', 'x14_o', 'x14_p', 'x14_w', 'x14_y', 'x15_p',
                'x16_n', 'x16_o', 'x16_w', 'x16_y', 'x17_n', 'x17_o', 'x17_t',
                'x18_e', 'x18_f', 'x18_l', 'x18_n', 'x18_p', 'x19_b', 'x19_h',
                'x19_k', 'x19_n', 'x19_o', 'x19_r', 'x19_u', 'x19_w', 'x19_y',
                'x20_a', 'x20_c', 'x20_n', 'x20_s', 'x20_v', 'x20_y', 'x21_d',
                'x21_g', 'x21_l', 'x21_m', 'x21_p', 'x21_u', 'x21_w']

        # Populate the DataFrame with a one hot value of 0 as the default value
        default_data = [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,
                        0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,
                        0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,
                        0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,
                        0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,
                        0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,
                        0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.]

        df = pd.DataFrame(np.array(default_data).reshape(1, -1), columns=cols)

        # Take the submitted data from the form (which is accessible as a dictionary)
        # and create a list in the order that matches the original dataset order
        form_list = list([self.data['capshape'], self.data['capsurface'], self.data['capcolor'], self.data['bruises'], self.data['odor'], self.data['gillattachment'],
                          self.data['gillspacing'], self.data['gillsize'], self.data['gillcolor'], self.data['stalkshape'],
                          self.data['stalkroot'], self.data['stalksurfaceabovering'], self.data['stalksurfacebelowring'], self.data[
            'stalkcolorabovering'], self.data['stalkcolorbelowring'], self.data['veiltype'], self.data['veilcolor'], self.data['ringnumber'],
            self.data['ringtype'], self.data['sporeprintcolor'], self.data['population'], self.data['habitat']])

        # Loop through form_list and check if the submitted value
        # matches one of the one hot encoded columns
        # Add a 1 when the submitted value matches the encoded column
        for i, feature_value in enumerate(form_list):
            col_name = 'x' + str(i) + '_' + feature_value

            if col_name in df.columns:
                df[col_name] = 1.

        return np.array(df.values).astype(int).tolist()[0]
