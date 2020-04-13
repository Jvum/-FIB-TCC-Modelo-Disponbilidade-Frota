import sklearn
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier # Import Decision Tree Classifier
from sklearn.model_selection import train_test_split # Import train_test_split function
from sklearn import metrics #Import scikit-learn metrics module for accuracy calculation
from matplotlib import pyplot as plt
from sklearn.svm import LinearSVC
from sklearn.metrics import confusion_matrix
from sklearn import preprocessing
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import mutual_info_classif
from sklearn.metrics import log_loss
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score
import joblib
import seaborn as sb
import numpy as np
import pandas as pd

class ModelDisponibilidade:
    def __init__ (self, fileTrain):
        self.fileTrain = fileTrain
        self.dataDisp = pd.read_excel(fileTrain)

    def preProcess(self):
        self.dataDisp['target'] = np.where(self.dataDisp['STATUS']=='Ativa', 0, 1)
        # Organizar nossos dados
        label_names_disp = np.asarray(['Ativa','Inativa'])
        labels_disp = np.asarray(self.dataDisp['target'])
        feature_names_disp = np.asarray(self.dataDisp.drop(['STATUS','SIGLA','PLACA','target'], axis=1).columns)
        features_disp = np.asarray(self.dataDisp.drop(['STATUS','SIGLA','PLACA','target'], axis=1))

        return(labels_disp, features_disp, feature_names_disp, label_names_disp)
        

    def training(self):

        labels_disp, features_disp, feature_names_disp, label_names_disp = self.preProcess()
        # Dividir nossos dados
        train_disp, test_disp, train_labels_disp, test_labels_disp = train_test_split(features_disp,
                                                          labels_disp,
                                                          test_size=0.33, random_state=42)

        # random forest model creation
        rfc = RandomForestClassifier()
        rfc.fit(train_disp,train_labels_disp)
        # predictions
        rfc_predict = rfc.predict(test_disp)
        print(accuracy_score(test_labels_disp, rfc_predict))
        print(rfc_predict)

        return rfc
    
    def createModel(self):

        model = self.training()
        filename = 'random_forest_disp.sav'
        joblib.dump(model, filename)

ob = ModelDisponibilidade("DadosTreinamento.xlsx")

ob.createModel()

#import json 
#import requests

#IPs = ["4", "5"]
#api_url = 'http://127.0.0.1:5000/api/v1/resources/disponibilidade/verifica'
#r = requests.post(url = api_url, json=IPs)
#r.text
#response = [123373,208,11,212,7,14,4,20,34,8,3,1,0,0,0,0,4,60]
#r = requests.post(url = api_url, json=response)