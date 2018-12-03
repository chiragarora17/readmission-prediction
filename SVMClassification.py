
# coding: utf-8

# In[1]:

from sklearn import metrics
from sklearn import svm
import pandas as pd
from sklearn.model_selection import train_test_split

df =  pd.read_csv('dataCategorizedNew.csv',skiprows=1, header=None,dtype='float')
dataFrameX = df.sample(frac=1).reset_index(drop=True)
dataFrameY = dataFrameX[dataFrameX.columns[len(dataFrameX.columns)-1]]
dataFrameX.drop(dataFrameX.columns[len(dataFrameX.columns)-1], axis=1, inplace=True)

x_train, x_test, y_train, y_test = train_test_split(dataFrameX, dataFrameY, test_size=0.3) 




# In[ ]:

#Following different SVM classifier are used to train the model


# In[ ]:

#SVM liear classifier

# classifier1 =svm.LinearSVC()
# classifier1.fit(x_train, y_train)
# y_pred=classifier1.predict(x_test)
# print("F1-score on validation data:",metrics.f1_score(y_test, y_pred, average="macro"))


# In[ ]:

#SVM SVC with default values for the parameters. Kernal used is rbf ,  
classifier2 =  svm.SVC()
classifier2.fit(x_train, y_train)
y_pred=classifier2.predict(x_test)
print("F1-score on validation data:",metrics.f1_score(y_test, y_pred, average="macro"))


# In[ ]:

# classifier3 =  svm.SVC(kernel='poly')
# classifier3.fit(x_train, y_train)
# y_pred=classifier3.predict(x_test)
# print("F1-score on validation data:",metrics.f1_score(y_test, y_pred, average="macro"))


# In[ ]:



