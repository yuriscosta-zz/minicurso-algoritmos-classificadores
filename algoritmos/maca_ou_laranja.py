# coding=UTF-8
import numpy as np
from sklearn import tree

caracteristicas = [[150, 0], [170, 0], [140, 1], [130, 1]]
rotulos = [1, 1, 0, 0]

classificador = tree.DecisionTreeClassifier()
classificador = classificador.fit(caracteristicas, rotulos)

# print classificador.predict(np.array([134, 0]).reshape(1, -1))
print classificador.predict(np.array([1000, 1]).reshape(1, -1))
