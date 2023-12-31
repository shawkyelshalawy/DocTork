# -*- coding: utf-8 -*-
"""anemia_manual

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1-lXFSx-rTmFClJ2XkECCFX21dZ4r7MdT
"""

import joblib
import pandas as pd
import numpy as np


def predict_manual(custom_values_list):
    x = ['Hemoglobin', 'MCH', 'MCV']
    custom_data = pd.DataFrame(data=np.array([custom_values_list]), columns=x)
    model = joblib.load(
        'DocTork-master/ML_Model/API_2/Manual/anemia/Model/GradientBoostingModel(anemia-m,f-3features)_2.h5')
    custom_data['Gender_Male'] = np.random.choice([1, 0])
    output = model.predict(custom_data)[0]
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


# predict_manual([15,40,80])
