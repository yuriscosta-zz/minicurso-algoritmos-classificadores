# coding=UTF-8
import numpy as np
from sklearn import tree

caracteristicas = [[140, 1], [130, 1], [144, 1], [136, 1], [150, 0], [170, 0],
[156, 0], [167, 0], [180, 0], [165, 0], [170, 0], [183, 0]]
rotulos = [0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2]
classificador = tree.DecisionTreeClassifier()
classificador = classificador.fit(caracteristicas, rotulos)

def toString(rotulo):
    if rotulo == 0:
        return "Maçã"
    elif rotulo == 1:
        return "Laranja"
    else:
        return "Banana"

'''
print toString(classificador.predict(np.array([134, 0]).reshape(1, -1))) # maçã
print toString(classificador.predict(np.array([123, 1]).reshape(1, -1))) # maçã
print toString(classificador.predict(np.array([150, 0]).reshape(1, -1))) # laranja
print toString(classificador.predict(np.array([150, 1]).reshape(1, -1))) # laranja
print toString(classificador.predict(np.array([160, 0]).reshape(1, -1))) # laranja
print toString(classificador.predict(np.array([160, 1]).reshape(1, -1))) # laranja
print toString(classificador.predict(np.array([180, 0]).reshape(1, -1))) # banana
print toString(classificador.predict(np.array([164, 0]).reshape(1, -1))) # banana
print toString(classificador.predict(np.array([173, 1]).reshape(1, -1))) # laranja
print toString(classificador.predict(np.array([130, 0]).reshape(1, -1))) # maçã
print toString(classificador.predict(np.array([122, 1]).reshape(1, -1))) # maçã
print toString(classificador.predict(np.array([153, 0]).reshape(1, -1))) # laranja
print toString(classificador.predict(np.array([154, 1]).reshape(1, -1))) # laranja
print toString(classificador.predict(np.array([165, 0]).reshape(1, -1))) # banana
print toString(classificador.predict(np.array([162, 1]).reshape(1, -1))) # banana
print toString(classificador.predict(np.array([181, 0]).reshape(1, -1))) # banana
print toString(classificador.predict(np.array([166, 0]).reshape(1, -1))) # banana
print toString(classificador.predict(np.array([178, 1]).reshape(1, -1))) # banana
'''

rotulos_teste = [0, 0, 1, 1, 1, 1, 2, 2, 1, 0, 0, 1, 1, 2, 2, 2, 2, 2]
caracteristicas_teste = [[134, 0], [123, 1], [150, 0], [150, 1], [160, 0],[160, 1],
[180, 0], [164, 0], [173, 1], [130, 0], [122, 1], [153, 0], [154, 1], [165, 0],
[162, 1], [181, 0], [166, 0], [178, 1]]
predicoes = classificador.predict(caracteristicas_teste)

from sklearn.metrics import accuracy_score
print ("Precisão do algoritmo: %f" %(accuracy_score(rotulos_teste, predicoes)))
