# -*- coding: utf-8 -*-
"""diabetes

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1-lXFSx-rTmFClJ2XkECCFX21dZ4r7MdT
"""

import cv2
import pytesseract
import re
import numpy as np
import pandas as pd
import joblib
import easyocr

pytesseract.pytesseract.tesseract_cmd = r"C:/Program Files/Tesseract-OCR/tesseract.exe"


def predict_image(path):

    keywords = ['HB', 'FPG', 'HRPP']
    try:

        try:

            img = cv2.imread(path)
            # Convert the image to gray scale
            img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            ocr_output = pytesseract.image_to_string(img_gray)
            dictionary = {}
            for line in ocr_output.split('\n'):
                if 'MCHC' in line:
                    continue

                for keyword in keywords:
                    try:
                        try:
                            if re.search(keyword, line, re.IGNORECASE):
                                if '=' in line:
                                    list_ = line.split('=')
                                    result = list_[1]
                                    dictionary[keyword] = float(result)
                                    break
                                elif ':' in line:
                                    list_ = line.split(':')
                                    result = list_[1]
                                    dictionary[keyword] = float(result)
                                    break
                        except:
                            if re.search(keyword, line, re.IGNORECASE):
                                list_ = str(line.split())
                                result = list_[1]
                                dictionary[keyword] = float(result)
                                break
                    except:
                        continue

            model_hba1c = joblib.load(
                "ML_Model/API_2/CV_ML_model_images/Diabetes/Model/HbA1c.h5")
            model_fpg = joblib.load(
                "ML_Model/API_2/CV_ML_model_images/Diabetes/Model/FPG.h5")
            model_2hrpp = joblib.load(
                "ML_Model/API_2/CV_ML_model_images/Diabetes/Model/HrPP.h5")
            faatures_hbalc = list(model_hba1c.feature_names_in_)
            faatures_fpg = list(model_fpg.feature_names_in_)
            faatures_2hrpp = list(model_2hrpp.feature_names_in_)
            features = faatures_hbalc + faatures_fpg + faatures_2hrpp
            features.pop(1)
            features.pop(2)
            data_dic = {}
            data_dic[features[0]] = dictionary['HB']
            data_dic[features[1]] = dictionary['FPG']
            data_dic[features[2]] = dictionary['HRPP']
            data_dic[features[3]] = np.random.choice([0, 1])
            custom_data = pd.DataFrame(data=[data_dic])
            # print('-----'*10)
            # print('Your Input :\n',custom_data)
            # print('-----'*10)
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

        except:
            # this needs to run only once to load the model into memory
            reader = easyocr.Reader(['en'], gpu=False)
            img = path
            output = reader.readtext(img, detail=1)
            dictionary = {}
            for i in output:
                probability = i[-1]

                if probability >= 0.6:
                    text = i[1]

                for keyword in keywords:
                    try:
                        try:
                            if re.search(keyword, text, re.IGNORECASE):
                                if '=' in text:
                                    result = output[output.index(i) + 1][1]
                                    dictionary[keyword] = float(result)
                                    break
                                elif ':' in text:
                                    result = output[output.index(i) + 1][1]
                                    dictionary[keyword] = float(result)
                                    break
                                elif output[output.index(i) + 1][1] == ':':
                                    dictionary[keyword] = float(
                                        output[output.index(i) + 2][1])
                                    break
                                elif output[output.index(i) + 1][1] == '8':
                                    dictionary[keyword] = float(
                                        output[output.index(i) + 2][1])
                                    break
                                else:
                                    result = output[output.index(i) + 1][1]
                                    dictionary[keyword] = float(result)
                        except:
                            if re.search(keyword, text, re.IGNORECASE):
                                list_ = str(text.split())
                                result = re.search(
                                    '\d+\.{0,1}\d*', list_).group()
                                dictionary[keyword] = float(result)
                                break
                    except:
                        continue

            model_hba1c = joblib.load(
                "ML_Model/API_2/CV_ML_model_images/Diabetes/Model/HbA1c.h5")
            model_fpg = joblib.load(
                "ML_Model/API_2/CV_ML_model_images/Diabetes/Model/FPG.h5")
            model_2hrpp = joblib.load(
                "ML_Model/API_2/CV_ML_model_images/Diabetes/Model/HrPP.h5")
            faatures_hbalc = list(model_hba1c.feature_names_in_)
            faatures_fpg = list(model_fpg.feature_names_in_)
            faatures_2hrpp = list(model_2hrpp.feature_names_in_)
            features = faatures_hbalc + faatures_fpg + faatures_2hrpp
            features.pop(1)
            features.pop(2)
            data_dic = {}
            data_dic[features[0]] = dictionary['HB']
            data_dic[features[1]] = dictionary['FPG']
            data_dic[features[2]] = dictionary['HRPP']
            data_dic[features[3]] = np.random.choice([0, 1])
            custom_data = pd.DataFrame(data=[data_dic])
            # print('-----'*10)
            # print('Your Input :\n',custom_data)
            # print('-----'*10)
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

    except:
        print('Your uploaded image can\'t be detected')
        print('-----'*10)
        model_hba1c = joblib.load(
            "ML_Model/API_2/CV_ML_model_images/Diabetes/Model/HbA1c.h5")
        model_fpg = joblib.load(
            "ML_Model/API_2/CV_ML_model_images/Diabetes/Model/FPG.h5")
        model_2hrpp = joblib.load(
            "ML_Model/API_2/CV_ML_model_images/Diabetes/Model/HrPP.h5")
        faatures_hbalc = list(model_hba1c.feature_names_in_)
        faatures_fpg = list(model_fpg.feature_names_in_)
        faatures_2hrpp = list(model_2hrpp.feature_names_in_)
        features = faatures_hbalc + faatures_fpg + faatures_2hrpp
        features.pop(1)
        features.pop(2)
        return 'Your uploaded image can\'t be detected\n \t Enter Manually the Following Please : ', features[:-1]
