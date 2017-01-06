# coding=UTF-8
import numpy as np
from sklearn import tree

caracteristicas = [[140, 1], [130, 1], [150, 0], [170, 0]]
rotulos = [0, 0, 1, 1]
classificador = tree.DecisionTreeClassifier()
classificador = classificador.fit(caracteristicas, rotulos)

print classificador.predict(np.array([134, 0]).reshape(1, -1)) # maçã
print classificador.predict(np.array([123, 1]).reshape(1, -1)) # maçã
print classificador.predict(np.array([150, 0]).reshape(1, -1)) # laranja
print classificador.predict(np.array([150, 1]).reshape(1, -1)) # laranja
print classificador.predict(np.array([160, 0]).reshape(1, -1)) # laranja
print classificador.predict(np.array([160, 1]).reshape(1, -1)) # laranja
