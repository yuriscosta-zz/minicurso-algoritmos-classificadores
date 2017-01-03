import numpy as np
from sklearn import tree

# this variable has to values, the first one is the fruit weight and the last one is the fruit texture, 0 for bumpy and 1 for smooth
features = [[140, 1], [130, 1], [150, 0], [170, 0]]

# the values inside labels indicate the fruit, 0 for apple and 1 for orange
labels = [0, 0, 1, 1]

# the clf is a decision tree and it find the patterns in the data set
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)

# tests 
print clf.predict(np.array([134, 0]).reshape(1, -1))
print clf.predict(np.array([123, 1]).reshape(1, -1))
print clf.predict(np.array([150, 0]).reshape(1, -1))
print clf.predict(np.array([150, 1]).reshape(1, -1))
print clf.predict(np.array([160, 0]).reshape(1, -1))
print clf.predict(np.array([160, 1]).reshape(1, -1))
