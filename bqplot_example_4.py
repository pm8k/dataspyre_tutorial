import pandas as pd
from IPython.display import display
from ipywidgets import Latex
from bqplot import *
from bqplot.market_map import MarketMap

data = pd.read_csv('data_files/country_codes.csv', index_col=[0])
country_codes = data.index.values
country_names = data['Name']

gdp_data = pd.read_csv('data_files/gdp_per_capita.csv', index_col=[0], parse_dates=True)
gdp_data.fillna(method='backfill', inplace=True)
gdp_data.fillna(method='ffill', inplace=True)

col = ColorScale(scheme='Greens')
continents = data['Continent'].values
ax_c = ColorAxis(scale=col, label='GDP per Capita', visible=False)

data['GDP'] = gdp_data.ix[-1]

market_map = MarketMap(names=country_codes, groups=continents,       # Basic data which needs to set for each map
                       cols=25, row_groups=3,                        # Properties for the visualization
                       ref_data=data,                                # Data frame used for different properties of the map
                       tooltip_fields=['Name', 'Continent', 'GDP'],  # Columns from data frame to be displayed as tooltip
                       tooltip_formats=['', '', '.1f'],
                       scales={'color': col}, axes=[ax_c])           # Axis and scale for color data

deb_output = Latex()
def selected_index_changed(name, value):
    deb_output.value = str(value)
        
market_map.on_trait_change(selected_index_changed, name='selected')

# Creating the figure to be displayed as the tooltip
sc_x = DateScale()
sc_y = LinearScale()

ax_x = Axis(scale=sc_x, grid_lines='dashed', label='Date')
ax_y = Axis(scale=sc_y, orientation='vertical', grid_lines='dashed',
            label='GDP', label_location='end', label_offset='-1em')

line = Lines(x= gdp_data.index.values, scales={'x': sc_x, 'y': sc_y}, colors=['orange'])
fig_tooltip = Figure(marks=[line], axes=[ax_x, ax_y], min_width=600, min_height=400)

market_map = MarketMap(names=country_codes, groups=continents,
                       cols=25, row_groups=3,
                       color=data['GDP'], scales={'color': col}, axes=[ax_c],
                       ref_data=data, tooltip_widget=fig_tooltip)

# Update the tooltip chart
hovered_symbol = ''
def hover_handler(self, content):
    global hovered_symbol
    symbol = content.get('ref_data', {}).get('Country Code', '')
    if(symbol != hovered_symbol):
        hovered_symbol = symbol
        if(gdp_data.get(hovered_symbol) is not None):
            line.y = gdp_data[hovered_symbol].values
            fig_tooltip.title = hovered_symbol
               
# Custom msg sent when a particular cell is hovered on
market_map.on_hover(hover_handler)
display(market_map)