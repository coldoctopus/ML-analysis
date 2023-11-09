import pandas as pd
import matplotlib
import numpy
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics  #calculate accuracy


iris = datasets.load_iris()

data = pd.DataFrame({'sepallength': iris.data[:, 0], 'sepalwidth': iris.data[:, 1],
                     'petallength': iris.data[:, 2], 'petalwidth': iris.data[:, 3],
                     'species': iris.target})

X, y = datasets.load_iris( return_X_y = True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.30)

X2 = data[['petallength', 'petalwidth']]
y2 = iris.target
X2_train, X2_test, y2_train, y2_test = train_test_split(X2, y2, test_size = 0.30)


#print(iris.target_names)
#print(iris.feature_names)

#train model & predict
iris_model = RandomForestClassifier(n_estimators = 100)
iris_model.fit(X_train,y_train)
y_predict = iris_model.predict(X_test)

iris_model2 = RandomForestClassifier(n_estimators = 100)
iris_model2.fit(X2_train,y2_train)
y_predict2 = iris_model2.predict(X2_test)
#feature_imp = pd.Series(iris_model.feature_importances_, index = iris.feature_names).sort_values(ascending = False)


print("Acc: ", metrics.accuracy_score(y2_test, y_predict2)*100)
print("Acc: ", metrics.accuracy_score(y_test, y_predict)*100)
#print(feature_imp)









