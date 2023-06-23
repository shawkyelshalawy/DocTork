# -*- coding: utf-8 -*-
"""Symptoms, Features and Lab Tests. ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1B7ewo2TzQQldOZg0j2gQOh2HqY1xgL9t
"""
# Importing Packages
import pandas as pd
import numpy as np
import joblib

# Loading Model
model = joblib.load(
    'DocTork-master/ML_Model/API_1/Disease_Symptoms_and_Tests/Disease_Symtopms/Model/EnsembleModel(RF-KNN-LR)(Symtypoms).h5')


def symptoms_tests_features(_symptomscheckedItems):

    # Return Features in Model
    features = list(model.feature_names_in_)

    # Reading Data for Features to Extracting Features for each Disease
    disease_features = pd.read_excel(
        'DocTork-master/ML_Model/API_1/Disease_Symptoms_and_Tests/Features_of_Diseases/Features and Diseases.xlsx')

    # Reading Data for Lab Test to Extracting Required Tests for each Disease
    disease_lab_tests = pd.read_excel(
        'DocTork-master/ML_Model/API_1/Disease_Symptoms_and_Tests/Lab_Test/Diseases and Lab Test.xlsx')

    # list come from Application (Testing only keep the comment after test API )

    # Returning Prediction of Model (Disease) Based on Symptoms
    custom_data_dic = {}
    for feature in features:
        custom_data_dic[feature] = 0
    for symptom in _symptomscheckedItems:
        feature_keys = list(custom_data_dic.keys())
        if symptom in feature_keys:
            custom_data_dic[symptom] = 1
    custom_data = pd.DataFrame([custom_data_dic])
    output = model.predict(custom_data)[0]
    print(output)  # Response from 1st Api

    # Returning Requried Tests for Predicted Disease
    required_tests = disease_lab_tests[disease_lab_tests['Disease']
                                       == output].iloc[:, 1:].dropna(axis=1).values.flatten()
    required_tests = ' , '.join(str(test) for test in required_tests)
    # print(required_tests)  # Response from 1st Api

    # Returning Features (Inputs) for Predicted Disease to be Written in Manual Option
    diseases_features_list = disease_features[disease_lab_tests['Disease'] == output].iloc[:, 1:].dropna(
        axis=1).values.flatten()
    diseases_features_list = list(diseases_features_list)
    # print(diseases_features_list)  # Response from 1st Api
    return output, required_tests, diseases_features_list