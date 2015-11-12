from __future__ import print_function
import numpy as np
import pandas as pd
from IPython.display import display
from bqplot import *

price_data = pd.DataFrame(np.cumsum(np.random.randn(150, 2).dot([[1.0, -0.8], [-0.8, 1.0]]), axis=0) + 100,
                          columns=['Security 1', 'Security 2'], index=pd.date_range(start='01-01-2007', periods=150))
size = 100
np.random.seed(0)
x_data = range(size)
y_data = np.cumsum(np.random.randn(size) * 100.0)
ord_keys = np.array(['A', 'B', 'C', 'D', 'E', 'F'])
ordinal_data = np.random.randint(5, size=size)
x_sc = LinearScale()
y_sc = LinearScale()

x_data = x_data[:50]
y_data = y_data[:50]

def_tt = Tooltip(fields=['x', 'y'], formats=['', '.2f'])

scatter_chart = Scatter(x=x_data, y=y_data, scales= {'x': x_sc, 'y': y_sc}, default_colors=['dodgerblue'],
                        tooltip=def_tt)
ax_x = Axis(scale=x_sc)
ax_y = Axis(scale=y_sc, orientation='vertical', tick_format='0.2f')

fig = Figure(marks=[scatter_chart], axes=[ax_x, ax_y])
display(fig)