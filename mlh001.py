# -*- coding: utf-8 -*-

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVC # "Support Vector Classifier"
def reg(file,impacts,outcome,inps):
    data = pd.read_csv(file)
    X = data[impacts]
    Y = data[outcome]
    linear_regressor = LinearRegression()
    linear_regressor.fit(X, Y)
    nx = [inps]
    pred = linear_regressor.predict(nx)
    return pred

def classify(file,impacts,outcome,inps):
    data = pd.read_csv(file)
    X = data[impacts]
    Y = data[outcome]
    Y=Y.round()
    clf = SVC(kernel='linear') 
    clf.fit(X,Y)
    nx = [inps]
    pred = clf.predict(nx)
    return pred

neuroticism=int(input("what is your neuroticism percentage(1,10): "))
agreeableness = int(input("what is your agreeableness percentage(1,10): "))
openness = int(input("what is your openness percentage(1,10): "))
conscientiousness = int(input("what is your conscientiousness percentage(1,10): "))
extraversion = int(input("what is your  extraversion percentage(1,10): "))

ch = int(input("What do you want to perform?\n1. Regression\n2. Classification\nEnter your choice: "))
if ch == 1:
    p = reg('ppm.csv',["neuroticism","agreeableness","openness","conscientiousness","extraversion"],"out",[neuroticism,agreeableness,openness,conscientiousness,extraversion])
    print("The outcome is: ",float(p[0]))
elif ch == 2:
    p = classify('ppm.csv',["neuroticism","agreeableness","openness","conscientiousness","extraversion"],"clss",[neuroticism,agreeableness,openness,conscientiousness,extraversion])

    if int(p[0]) == 0:
        print("not conformed")
    elif int(p[0]) == 1:
        print("conformed")
else:
    print("Invalid choice!")
