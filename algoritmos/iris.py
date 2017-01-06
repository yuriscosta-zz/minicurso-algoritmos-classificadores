# coding=UTF-8
import numpy as np
from sklearn.datasets import load_iris
from sklearn import tree

iris = load_iris()
# print iris.feature_names
# print iris.target_names
# print iris.data[0]
# print iris.target[0]

# for i in range(len(iris.target)):
#    print ("Exemplo: " + str(i) + "\nCaracterísticas: " + str(iris.data[i]) +
#    "\nRótulo: " + str(iris.target[i]) + "\n")

test_index = [0, 50, 100]

# dados de treinamento
train_target = np.delete(iris.target, test_index)
train_data = np.delete(iris.data, test_index, axis=0)

# dados de teste
test_target = iris.target[test_index]
test_data = iris.data[test_index]

# classificador
classificador = tree.DecisionTreeClassifier()
classificador.fit(train_data, train_target)

print classificador.predict(test_data)

# viz code
from sklearn.externals.six import StringIO
import pydot

dot_data = StringIO()
tree.export_graphviz(classificador,
			out_file = dot_data,
			feature_names = iris.feature_names,
 			class_names = iris.target_names,
			filled = True, rounded = True,
			impurity = False)

graph = pydot.graph_from_dot_data(dot_data.getvalue())
graph.write_pdf("iris.pdf")
