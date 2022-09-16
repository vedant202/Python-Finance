from itertools import count
from sklearn import svm,model_selection,neighbors
from sklearn.ensemble import VotingClassifier,RandomForestClassifier
# import pandas as pd
import numpy as np
import preprocessing_data_ML as pp_data
from collections import Counter

def do_ml(ticker):
    X,y,df = pp_data.extract_featues_sets(ticker)

    X_train, X_test, y_train, y_test= model_selection.train_test_split(X,y,test_size=0.25)
    
    # print("X Train ",np.count_nonzero(np.isinf(X_train)))
    # print("X Test ",np.count_nonzero(np.isinf(X_test)))

    X_train1 = np.nan_to_num(X_train,posinf=0,neginf=0)
    X_test1 = np.nan_to_num(X_test,posinf=0,neginf=0)

    # print("X Train1 ",np.count_nonzero(np.isinf(X_train1)))
    # print("X Test1 ",np.count_nonzero(np.isinf(X_test1)))
    
    # clf = neighbors.KNeighborsClassifier()

    # clf = svm.LinearSVC(max_iter=10000)

    clf = VotingClassifier([('lsvc',svm.LinearSVC()),
                            ('knn',neighbors.KNeighborsClassifier()),
                            ('rfor',RandomForestClassifier())],n_jobs=-1)
    
    clf.fit(X_train1,y_train)
    confidence = clf.score(X_test1,y_test)
    print("Accuracy: ",confidence)
    predictions =  clf.predict(X_test1)
    print("Predicted predictions ",Counter(predictions))
    print()

# print("-----------Wipro---------")
# do_ml('WIPRO')

print("-----------RELIANCE---------")
do_ml('RELIANCE')

# print("-----------TATAMOTORS---------")
# do_ml('TATAMOTORS')


