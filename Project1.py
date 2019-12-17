from pandas import read_csv
from matplotlib import pyplot
from pandas.plotting import scatter_matrix
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import StratifiedKFold
from sklearn.model_selection import cross_val_score

#names = ['Experience', 'Salary']
dataset = read_csv("salary_data.csv")
#pyplot.scatter(x ='YearsExperience',y ='Salary')

#x=dataset['YearsExperience']
#y=dataset['Salary']
#pyplot.plot(x, y, 'o', color='green');
#pyplot.show()

dataset = read_csv('salary_data.csv')
X = dataset.iloc[:, :-1].values #get a copy of dataset exclude last column
y = dataset.iloc[:, 1].values #get array of dataset in column 1st


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=0)

#kfold = StratifiedKFold(n_splits=1, random_state=1)
#cv_results = cross_val_score(LinearRegression(), X_train, y_train, cv=kfold, scoring='accuracy')



regressor = LinearRegression()
regressor.fit(X_train, y_train)



print(regressor.predict(8.7))
#print(regressor.predict(X_test))


## Visualizing the Training set results
#viz_train = pyplot
#viz_train.scatter(X_train, y_train, color='red')
#viz_train.plot(X_train, regressor.predict(X_train), color='blue')
#viz_train.title('Salary VS Experience (Training set)')
#viz_train.xlabel('Year of Experience')
#viz_train.ylabel('Salary')
#viz_train.show()

# Visualizing the Test set results
viz_test = pyplot
viz_test.scatter(X_test, y_test, color='red')
viz_test.plot(X_train, regressor.predict(X_train), color='blue')
viz_test.title('Salary VS Experience (Test set)')
viz_test.xlabel('Year of Experience')
viz_test.ylabel('Salary')
viz_test.show()







