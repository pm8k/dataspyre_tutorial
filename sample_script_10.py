from spyre import server

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pygal
import cherrypy
import os 

class SimpleSineApp(server.App):
    title = "Simple Sine App"
    inputs = [{ "type":"text",
                "key":"freq",
                "value":5,
                "label":"frequency",
                "action_id":"sine_wave_plot"}]
    tabs=["Plot","Data"]
    outputs = [{"type" : "html",
                "id" : "initiate_directs",
                "on_page_load" : True },
                {"type":"html",
                "id":"wave_plot",
                "tab":"Plot",
                "control_id":"sine_wave_plot"},
                {"type":"table",
                "id":"wave_data",
                "tab":"Data",
                "control_id":"sine_wave_plot"}]

    controls = [{"type":"HIDDEN",
                 "id":"sine_wave_plot"}]
    
    def initiate_directs(self,params):
        root=self.getRoot()
        current_dir=os.path.dirname(os.path.abspath("__file__"))
        config_public={
        '/':{
            'tools.staticdir.root' : current_dir,
            },
         '/static': {
             'tools.staticdir.on': True,
             'tools.staticdir.dir': 'public',
             'tools.staticdir.content_types':{'.min.js':"text/javascript",'svg':"image/svg+xml"}
         }
        }
        cherrypy.tree.mount(root, "/", config=config_public)
    def wave_plot(self, params):
        #self.initiate_directs(params)
        f = float(params['freq'])
        df=self.getData(params)
        line_chart = pygal.Line(height=400,width=600,show_minor_x_labels=False,x_label_rotation=45)
        line_chart.title = 'Sine Wave in Pygal'
        line_chart.x_labels = ["{0:.2f}".format(a) for a in df.x.tolist()]
        line_chart.add('Sin(y)',df.y.tolist())
        line_chart.add('Sin(2y)',df.y2.tolist())
        
        line_chart.x_labels_major=line_chart.x_labels[::30]
        line_chart.render_to_file('public/pygalspyre.svg')
        html="""<head></head><body><figure><embed type="image/svg+xml" src="static/pygalspyre.svg" /></figure></body>"""

        return html
        
    def getData(self,params):
        f=float(params['freq'])
        x = pd.Series(np.arange(0,2*np.pi,np.pi/150))
        y = pd.Series(np.sin(f*x))
        y2= pd.Series(np.sin(f*x*2))
        df=pd.concat([x,y,y2],axis=1)
        df.columns=['x','y','y2']
        return df

if __name__ == '__main__':
    app = SimpleSineApp()
    app.launch()