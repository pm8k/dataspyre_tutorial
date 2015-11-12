from __future__ import print_function
from bqplot import pyplot as plt
from bqplot import topo_load
from bqplot.interacts import panzoom
from numpy import *
import pandas as pd

random.seed(0)
size = 100
y_data = cumsum(random.randn(size) * 100.0)
y_data_2 = cumsum(random.randn(size))
y_data_3 = cumsum(random.randn(size) * 100.)

plt.figure(1)
n = 100
x = linspace(0.0, 10.0, n)
plt.plot(x, y_data, axes_options={'y': {'grid_lines': 'dashed'}})
plt.show()