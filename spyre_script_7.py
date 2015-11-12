#####################
#Display this Code
#####################
from spyre import server

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

class SimpleSineApp(server.App):
	title = "Simple Sine App"
	inputs = [{ "type":"slider",
				"key":"x_slider",
				"value":200,
				"min":1,
				"max":200,
				"label":"x_axis",
				"action_id":"sine_wave_plot"},{ "type":"text",
				"key":"freq",
				"value":5,
				"label":"frequency",
				"action_id":"sine_wave_data"}]
	tabs=["Plot","Data"]
	outputs = [{"type":"plot",
				"id":"wave_plot",
				"tab":"Plot",
				"control_id":"sine_wave_data"},
				{"type":"table",
				"id":"wave_data",
				"tab":"Data",
				"control_id":"sine_wave_plot"}]
	controls = [{"type":"HIDDEN",
                 "id":"sine_wave_plot"},
                 {"type":"HIDDEN","id":"sine_wave_data"}]
	def getPlot(self, params):
		f = float(params['freq'])
		index=int(params['x_slider'])
		df=self.getData(params)
		fig = plt.figure()
		splt1 = fig.add_subplot(1,1,1)
		splt1.plot(df.x,df.y)
		return fig
	def getData(self,params):
		f=float(params['freq'])
		index=int(params['x_slider'])
		x = pd.Series(np.arange(0,2*np.pi,np.pi/150))
		y = pd.Series(np.sin(f*x))
		df=pd.concat([x,y],axis=1)
		df.columns=['x','y']
		return df[:index]

if __name__ == '__main__':
	app = SimpleSineApp()
	app.launch()
#####################