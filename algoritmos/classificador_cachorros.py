# coding=UTF-8
import numpy as np
import matplotlib.pyplot as plt

greyhounds = 500
labs = 500

grey_height = 28 + 4 * np.random.randn(greyhounds)
lab_height = 24 + 4 * np.random.randn(labs)

# gerar histograma
plt.hist([grey_height, lab_height], stacked=True, color=['r', 'b'])
plt.show()
