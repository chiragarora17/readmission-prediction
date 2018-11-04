
# coding: utf-8

# In[2]:

#Load the data into data frame and separate Y and  X

import pandas as pd
dataFrameX = pd.read_csv("diabetic_data.csv")
index_mapping =  pd.read_csv("IDs_mapping.csv")
dataFrameY = dataFrameX[dataFrameX.columns[len(dataFrameX.columns)-1]]
dataFrameX.drop(dataFrameX.columns[len(dataFrameX.columns)-1], axis=1, inplace=True)
#X_train, X_test, y_train, y_test = train_test_split(dataFrameX, dataFrameY, test_size=0.3) # 70% training and 30% test


# In[5]:

#Preprocessing data 
import numpy as np

#create List of map that contians cols with list of its unique values
uniqueColVals = []
for index, column in enumerate(dataFrameX.columns):
    if(index < 23):
        continue
    else:
        colDict={}
        colDict[column]=dataFrameX[column].unique().tolist()
        uniqueColVals.append(colDict)


print uniqueColVals

print len(uniqueColVals)
            
        
        
        

        
        


        


# In[6]:

#Assign categories to each cols according to each value
for index,row in dataFrameX.iterrows():
    if(index==0 ):
        continue
    elif index > 20:
        break
    else:
        for i,col in enumerate(uniqueColVals):
            for key,val in col.items():
                    assignValueTo = str(dataFrameX.iat[index,i+23])
                    assignValue =  val.index(assignValueTo)
                    dataFrameX.iat[index, i+23]=assignValue
                    print dataFrameX.iat[index, i+23]
                    
    

                    
            


# In[12]:

#import to csv

dataFrameX.to_csv("dataCategorizedNew.csv", sep=',',header=False)


# In[ ]:



