from spyre import server

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from bokeh.charts import Donut
from bokeh.resources import INLINE
from bokeh.resources import CDN
from bokeh.embed import components
from bokeh.plotting import figure, show, output_file, vplot

class SimpleSineApp(server.App):
    title = "Simple Sine App"
    inputs = [{ "type":"text",
                "key":"freq",
                "value":5,
                "label":"frequency",
                "action_id":"sine_wave_plot"}]
    tabs=["Plot","Data"]
    outputs = [{"type":"html",
                "id":"wave_plot",
                "tab":"Plot",
                "control_id":"sine_wave_plot"},
                {"type":"table",
                "id":"wave_data",
                "tab":"Data",
                "control_id":"sine_wave_plot"}]
    controls = [{"type":"HIDDEN",
                 "id":"sine_wave_plot"}]
    def getHTML(self, params):
        f = float(params['freq'])
        df=self.getData(params)

        TOOLS = "pan,wheel_zoom,box_zoom,reset,save,box_select"

        p2 = figure(title="Another Sine Example", tools=TOOLS)

        p2.circle(df.x, df.y, legend="sin(x)")
        p2.line(df.x, df.y, legend="sin(x)")

        
        script, div = components(p2, CDN)
        html = "%s\n%s"%(script, div)
        return html
        
        return fig
    def getData(self,params):
        f=float(params['freq'])
        x = pd.Series(np.arange(0,2*np.pi,np.pi/150))
        y = pd.Series(np.sin(f*x))
        df=pd.concat([x,y],axis=1)
        df.columns=['x','y']
        return df
    def getCustomJS(self):
        return INLINE.js_raw[0]

    def getCustomCSS(self):
        return INLINE.css_raw[0]
if __name__ == '__main__':
    app = SimpleSineApp()
    app.launch()