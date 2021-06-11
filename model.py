import pickle
import numpy as np
import pandas as pd
from sklearn.metrics import f1_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
def build_model():

    data = pd.read_csv('pima-indians-diabetes.csv',header = None)
    columns = 'A B C D E F G H TARGET'.split(' ')
    data.columns= columns

    data_x = data.drop('TARGET',axis =1)
    data_y = data['TARGET']

    train_x,test_x,train_y,test_y = train_test_split(data_x,data_y, test_size = 0.2, stratify = data_y)

    clf = RandomForestClassifier(n_estimators=1000, n_jobs =-1)

    clf.fit(train_x,train_y)

    with open('model.pkl','wb') as file:
        pickle.dump(clf,file)

    with open('model.pkl','rb') as file:
        clf2 = pickle.load(file)

    pred = clf2.predict(test_x)

    score = f1_score(test_y,pred )
    print(score)

if __name__=='__main__':
    build_model()