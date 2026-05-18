import numpy as np
import pandas as pd
from sklearn.datasets import fetch_california_housing
import matplotlib.pyplot as plt
from matplotlib import widgets

data = fetch_california_housing(as_frame=True)
data_matrix = data.data
data_targets = data.target
feature_names = data.feature_names

fig, axe = plt.subplots()

x = data_matrix[feature_names[0]]
y = data_targets
axe.scatter(x,y)

slider_space = fig.add_axes([0.15, 0.005, 0.73, 0.05])
The_Slider = widgets.Slider(slider_space, valmin=1, valmax=10000, valstep=1)
plt.show()

def WhenScrolling():
    The_Slider.val

#finish the scrollbar function
#test whether the scrollbar works and understand its properties and methods. 