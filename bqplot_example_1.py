import pandas as pd
import numpy as np
symbol = 'Security 1'
price_data = pd.DataFrame(np.cumsum(np.random.randn(150, 2).dot([[0.5, 0.4], [0.4, 1.0]]), axis=0) + 100,
                          columns=['Security 1', 'Security 2'], index=pd.date_range(start='01-01-2007', periods=150))

dates_actual = price_data.index.values
prices = price_data[symbol].values

from bqplot import *
from bqplot.interacts import *
from traitlets import link

from IPython.display import display
from ipywidgets import Latex, ToggleButtons, VBox


## call back for selectors
def interval_change_callback(name, value):
    db.value = str(value)

## call back for selectors
def date_interval_change_callback(name, value):
    db_date.value = str(value)
    
from datetime import datetime as py_dtime

dt_x = DateScale(min=np.datetime64(py_dtime(2006, 6, 1)))


lc2_y = LinearScale()

lc2 = Lines(x=dates_actual, y=prices,
            scales={'x': dt_x, 'y': lc2_y})

x_ax1 = Axis(label="Date", scale = dt_x)
x_ay2 = Axis(label=(symbol + " Price"), scale = lc2_y, orientation="vertical", tick_format="0.2f")

intsel_date = FastIntervalSelector(scale=dt_x, marks=[lc2])
db_date = Latex()
db_date.value = str(intsel_date.selected)
display(db_date)
lc2.on_trait_change(date_interval_change_callback, name='selected')

fig = Figure(marks=[lc2], axes=[x_ax1, x_ay2], interaction=intsel_date)
display(fig)

intsel_date = BrushIntervalSelector(scale=dt_x, marks=[lc2], color='blue')
lc2.on_trait_change(date_interval_change_callback, name='selected')
fig.interaction = intsel_date