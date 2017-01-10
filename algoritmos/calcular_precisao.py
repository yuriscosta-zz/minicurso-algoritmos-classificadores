# coding=UTF-8
from sklearn import datasets
iris = datasets.load_iris()

# dados para treinamento e teste
X = iris.data
Y = iris.target

from sklearn.cross_validation import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = .5)

print Y_test
'''
# classificador com arvore de decisao
from sklearn import tree
classificador = tree.DecisionTreeClassifier()
'''

#classificador com KNN
from sklearn.neighbors import KNeighborsClassifier
classificador = KNeighborsClassifier()

classificador.fit(X_train, Y_train)

predicoes = classificador.predict(X_test)
# print predicoes

# calcular a precisaoS
from sklearn.metrics import accuracy_score
# print ("Precisão usando árvore de decisão: %f" %(accuracy_score(Y_test, predicoes)))
# print ("Precisão usando KNN: %f" %(accuracy_score(Y_test, predicoes)))
