
# coding: utf-8

# In[102]:



def replaceColumn(df, col, oldval, newval):
    df[col] = df[col].replace(oldval, newval)
    return df

def replaceColumnList(df, col, listOfOldVal, newval):
    newDf = df
    for oldVal in listOfOldVal:
        newDf = replaceColumn(df, col, oldVal, newval)
    return newDf

def transformLabelEncoder(df, col):
    le = preprocessing.LabelEncoder()
    df[col] = le.fit_transform(df[col])
    return df;

def diagColn(oldVal):
    newVal = -99
    if (oldVal.find("E") != -1 or oldVal.find("V") != -1):
        newVal = 0
    if (oldVal == '?'):
        newVal = -1
    if (newVal != -99):
        return newVal

    oldVal = float(oldVal)
    if (oldVal > 1 and oldVal <= 139):
        newVal = 1
        
    if (oldVal > 140 and oldVal <= 239):
        newVal = 2
        
    if (oldVal > 240 and oldVal <= 279):
        newVal = 3
        
    if (oldVal > 280 and oldVal <= 289):
        newVal = 4
        
    if (oldVal > 290 and oldVal <= 319):
        newVal = 5
        
    if (oldVal > 320 and oldVal <= 389):
        newVal = 6
        
    if (oldVal > 390 and oldVal <= 459):
        newVal = 7
        
    if (oldVal > 460 and oldVal <= 519):
        newVal = 8
        
    if (oldVal > 520 and oldVal <= 579):
        newVal = 9
        
    if (oldVal > 580 and oldVal <= 629):
        newVal = 10
        
    if (oldVal > 630 and oldVal <= 679):
        newVal = 11
        
    if (oldVal > 680 and oldVal <= 709):
        newVal = 12
        
    if (oldVal > 710 and oldVal <= 739):
        newVal = 13
        
    if (oldVal > 740 and oldVal <= 759):
        newVal = 14
        
    if (oldVal > 760 and oldVal <= 779):
        newVal = 15
        
    if (oldVal > 780 and oldVal <= 799):
        newVal = 16
        
    if (oldVal > 800 and oldVal <= 999):
        newVal = 17
        
    return newVal


def processDrug(drugJson, encoder, arr):
    for key, value in drugJson.items():
        va = [value]
        arr.append(encoder.transform(va)[0])


# In[109]:


import pandas as pd
import numpy as np
import pickle
from sklearn import preprocessing

dirPath = 'dataset_diabetes/'


def predict(data):
    # load the model from disk
    filename = "finalized_model.sav"
    loaded_model = pickle.load(open(dirPath + filename, 'rb'))
    arr = preprocess(data)
    result = loaded_model.predict(arr)
    print(result)
    return result

data =  {
   "race": "Caucasian",
   "gender": "Female",
   "age": "[0-40)",
   "admission_type_id": 6,
   "discharge_disposition_id": 25,
   "admission_source_id": 1,
   "time_in_hospital": 1,
   "num_lab_procedures": 41,
   "num_procedures": 0,
   "num_medications": 1,
   "number_outpatient": 0,
   "number_emergency": 0,
   "number_inpatient": 0,
   "diag_1": "250.83",
   "diag_2": "?",
   "diag_3": "?",
   "number_diagnoses": 1,
   "max_glu_serum": "None",
   "A1Cresult": "None",
    "drug": {
   "metformin": "No",
   "repaglinide": "No",
   "nateglinide": "No",
   "chlorpropamide": "No",
   "glimepiride": "No",
   "acetohexamide": "No",
   "glipizide": "No",
   "glyburide": "No",
   "tolbutamide": "No",
   "pioglitazone": "No",
   "rosiglitazone": "No",
   "acarbose": "No",
   "miglitol": "No",
   "troglitazone": "No",
   "tolazamide": "No",
   "insulin": "No",
   "glyburide-metformin": "No",
   "glipizide-metformin": "No",
   "glimepiride-pioglitazone": "No",
   "metformin-rosiglitazone": "No",
   "metformin-pioglitazone": "No"
    },
   "change": "No",
   "diabetesMed": "No"
 }

data1 = {
   "race": "Caucasian",
   "gender": "Female",
   "age": "[10-20)",
   "admission_type_id": 1,
   "discharge_disposition_id": 1,
   "admission_source_id": 7,
   "time_in_hospital": 3,
   "num_lab_procedures": 59,
   "num_procedures": 0,
   "num_medications": 18,
   "number_outpatient": 0,
   "number_emergency": 0,
   "number_inpatient": 0,
   "diag_1": "276",
   "diag_2": "250.01",
   "diag_3": "255",
   "number_diagnoses": 9,
   "max_glu_serum": "None",
   "A1Cresult": "None",
    "drug": {
   "metformin": "No",
   "repaglinide": "No",
   "nateglinide": "No",
   "chlorpropamide": "No",
   "glimepiride": "No",
   "acetohexamide": "No",
   "glipizide": "No",
   "glyburide": "No",
   "tolbutamide": "No",
   "pioglitazone": "No",
   "rosiglitazone": "No",
   "acarbose": "No",
   "miglitol": "No",
   "troglitazone": "No",
   "tolazamide": "No",
   "insulin": "Up",
   "glyburide-metformin": "No",
   "glipizide-metformin": "No",
   "glimepiride-pioglitazone": "No",
   "metformin-rosiglitazone": "No",
   "metformin-pioglitazone": "No"
    },
   "change": "Ch",
   "diabetesMed": "Yes"
 }

def preprocess(data):
    metadataList = pickle.load(open(dirPath+"metadataList.p", "rb"))
    keyList = metadataList[0]
    manualInfo = metadataList[1].get("manual")
    encoderInfo = metadataList[1].get("labelencoder")
#     print(manualInfo)
    arr = []
    for key, value in data.items():
#         print(key)
#         print(value)

        if (keyList.get(key) == "manual"):
            newVal = manualInfo.get(key).get(value)
#             print(newVal)
            if (newVal != None):
                arr.append(newVal)
            else:
#                 print(manualInfo.get(key).get("unknown"))
                if (isinstance(value, int)):
                    arr.append(value)
                elif(value.isdigit()):
                    arr.append(value)
                else:
                    newVal = manualInfo.get(key).get("unknown")
                    arr.append(newVal)
        elif(keyList.get(key) == "labelencoder"):
            if (key != 'drug'):
                newVal = encoderInfo.get(key)
                encoder = preprocessing.LabelEncoder()
                encoder.classes_ = np.load(newVal)
                va = [value]
                arr.append(encoder.transform(va)[0])
            else:
                encoderClass = encoderInfo.get(key)
                encoder = preprocessing.LabelEncoder()
                encoder.classes_ = np.load(encoderClass)
                processDrug(value, encoder, arr)
        elif(keyList.get(key) == "diag"):
            newVal = diagColn(str(value))
            arr.append(newVal)
        elif(keyList.get(key) == "onehotencoder"):
            pass
        else:
            arr.append(value)
    numpArr = np.array([arr])
    print(numpArr)
    return numpArr;
# predict(data1)[0]