# -*- coding: utf-8 -*-
"""rheumatiod_arthities_manual

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1-lXFSx-rTmFClJ2XkECCFX21dZ4r7MdT
"""

import joblib
import pandas as pd
import numpy as np


def predict_manual(custom_values_list):

    x = ['Anti_CPP(u/ml)']
    custom_data = pd.DataFrame(data=np.array([custom_values_list]), columns=x)
    custom_data['Gender'] = np.random.choice([1, 0])
    model = joblib.load('ML_Model/API_2/Manual/Rheumatiod/Model/Rheumatiod.h5')
    output = model.predict(custom_data)[0]
    pred_mapping = {'1': 'Rheumatiod_Arthities',
                    '0': 'Normal'}
    output = pred_mapping[str(output)]

    correct_predication_name = {
        'Anemia': 'Normal Anemia',
        'Good': 'Normal ',
        'Micro': 'Microcytic Anemia',
        'Macro': 'Macrocytic Anemia',
        'CML': 'Chronic Myelogenous Leukemia',
        'Acute L': 'Acute Lymphoblastic Leukemia',
        'HyperTyroid':  'Hyperthyroidism',
        'Hypothyroid': 'Hypothyroidism',
        'Other Thyroid Abnormalities':  'Other Thyroid Abnormalities',
        'Normal':  'Normal ',
        'Hyperuricosuria (Gout)': 'Hyperuricemia (Gout)',
        'Hypouricosuria ':  'Hypouricemia',
        'Jaundice':  'Jaundice',
        'Diabetic': 'Diabetes',
        'Pre Diabetic': 'Prediabetes',
        'Hypoglycemia': 'Hypoglycemia',
        'Prostatic_Cancer':  'Prostatic Cancer',
        'Rheumatiod_Arthities': 'Rheumatoid Arthritis',
        'Hypoparathyroid': 'Hypoparathyroidism',
        'Another Disease':  'Another Disease',
        'Hyperparathyroid': 'Hyperparathyroidism',
        'Acute  L or CML':  'Acute Lymphoblastic Lekumia and Chronic Myelogenous Lekumia',
        'Good':  'Normal',
        'Normal': 'Normal'}

    patient_output_disease = correct_predication_name[output]
    return patient_output_disease


# predict_manual([25])
