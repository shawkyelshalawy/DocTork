# -*- coding: utf-8 -*-
"""diabetes_manual

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1-lXFSx-rTmFClJ2XkECCFX21dZ4r7MdT
"""

import joblib
import pandas as pd
import numpy as np


def predict_manual(custom_values_list):

    model_hba1c = joblib.load(
        "ML_Model/API_2/Manual/Diabetes/Hb_A1C_Test/Model/HbA1c.h5")
    model_fpg = joblib.load(
        "ML_Model/API_2/Manual/Diabetes/FPG_Test/Model/FPG.h5")
    model_2hrpp = joblib.load(
        "ML_Model/API_2/Manual/Diabetes/HrPP_Test/Model/HrPP.h5")
    faatures_hbalc = list(model_hba1c.feature_names_in_)
    faatures_fpg = list(model_fpg.feature_names_in_)
    faatures_2hrpp = list(model_2hrpp.feature_names_in_)
    features = faatures_hbalc + faatures_fpg + faatures_2hrpp
    features.pop(1)
    features.pop(2)
    custom_data = pd.DataFrame(data=np.array(
        [custom_values_list]), columns=features[:-1])
    custom_data['Gender'] = np.random.choice([1, 0])
    pred_hbalc = model_hba1c.predict(
        custom_data[list(model_hba1c.feature_names_in_)])[0]
    pred_fpg = model_fpg.predict(
        custom_data[list(model_fpg.feature_names_in_)])[0]
    pred_2hrr = model_2hrpp.predict(
        custom_data[list(model_2hrpp.feature_names_in_)])[0]
    # Model Output Meaning :
    # 0 >> Normal
    # 1 >> Diabetic
    # 2 >> Prediabetic
    # 3 >> Hypoglycemia

    if pred_hbalc == 1:
        output = 'Diabetic'

    elif (pred_hbalc == 0) and (pred_fpg == 1) and (pred_2hrr == 1):
        output = 'Diabetic'

    elif (pred_hbalc == 2) and (pred_fpg == 1) and (pred_2hrr == 1):
        output = 'Diabetic'

    elif (pred_hbalc == 2) and (pred_fpg == 2):
        output = 'Pre Diabetic'

    elif (pred_hbalc == 2) and (pred_fpg == 0):
        output = 'Pre Diabetic'

    elif (pred_hbalc == 0) and (pred_fpg == 2):
        output = 'Pre Diabetic'

    elif (pred_hbalc == 0) and (pred_fpg == 0):
        output = 'Normal'

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


# predict_manual([5,160,230])
