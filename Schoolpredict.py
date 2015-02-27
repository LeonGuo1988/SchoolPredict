# -*- coding: utf-8 -*-
"""
Created on Fri Feb 27 16:07:55 2015

@author: Angie
"""

from sklearn import linear_model
from sklearn.externals import joblib

def featurecalculate():
    features=[0]*11
    features[0]=1       # The Bachelor school
    features[1]=1       # The Master school
    features[2]=3.5     # The GPA of Bachelor 
    features[3]=3.5     # The GPA of Master
    features[4]=1100    # GRE
    features[5]=90      # TOELF
    features[6]=2       # The number of paper
    features[7]=1       # The number of SCI paper
    features[8]=1       # The major of Bachelor
    features[9]=1       # The major of Master
    features[10]=1      # The major of applying       
    return features
    
def modeltrain(features,labels):
    regr = linear_model.LinearRegression()
    # Train the model using the training sets
    regr.fit(features, labels)
    joblib.dump(regr, 'D:\lr.model')  
    
if __name__=="__main__":
    features = featurecalculate()
    regr = joblib.load('D:\lr.model')
    result = regr.predict(features)
    

 
    