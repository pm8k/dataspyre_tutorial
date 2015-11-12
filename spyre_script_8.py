#####################
#Display this Code
#####################
from spyre import server

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os
import cherrypy
class SimpleSineApp(server.App):
	title = "Simple Sine App"
	inputs = [{ "type":"text",
				"key":"freq",
				"value":5,
				"label":"frequency",
				"action_id":"sine_wave_plot"}]
	outputs = [{"type" : "html",
            	"id" : "initiate_directs",
            	"on_page_load" : True },
				{"type":"html",
				"id":"wave_plot_and_data",
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
	def wave_plot_and_data(self, params):
		f = float(params['freq'])
		df=self.getplotData(params)
		fig = plt.figure()
		splt1 = fig.add_subplot(1,1,1)
		splt1.plot(df.x,df.y)
		fig.savefig('public/ourfig'+str(f)+'.png')
		dfhtml=df[:20].to_html(index=False)
		html='<figure><img src="static/ourfig'+str(f)+'.png"/></figure>'
		finalhtml=html+"<br>"+dfhtml
		return finalhtml
	def getplotData(self,params):
		f=float(params['freq'])
		x = pd.Series(np.arange(0,2*np.pi,np.pi/150))
		y = pd.Series(np.sin(f*x))
		df=pd.concat([x,y],axis=1)
		df.columns=['x','y']
		return df

if __name__ == '__main__':
	app = SimpleSineApp()
	app.launch()
#####################