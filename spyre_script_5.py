#####################
#Display this Code
#####################
from spyre import server

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

class SimpleSineApp(server.App):
	title = "Simple Sine App"
	inputs = [{ "type":"text",
				"key":"freq",
				"value":5,
				"label":"frequency",
				"action_id":"sine_wave_plot"}]
	tabs=["Plot1","Plot2","Data"]
	outputs = [{"type":"plot",
				"id":"wave_plot",
				"tab":"Plot1",
				"control_id":"sine_wave_plot"},
				{"type":"plot",
				"id":"wave_plot2",
				"tab":"Plot2",
				"control_id":"sine_wave_plot"},
				{"type":"table",
				"id":"wave_data",
				"tab":"Data",
				"control_id":"sine_wave_plot"}]
	controls = [{"type":"HIDDEN",
                 "id":"sine_wave_plot"}]
	def wave_plot(self, params):
		f = float(params['freq'])
		df=self.wave_data(params)
		fig = plt.figure()
		splt1 = fig.add_subplot(1,1,1)
		splt1.plot(df.x,df.y1)
		return fig
	def wave_plot2(self, params):
		f = float(params['freq'])
		df=self.wave_data(params)
		fig = plt.figure()
		splt1 = fig.add_subplot(1,1,1)
		splt1.plot(df.x,df.y2)
		return fig
	def wave_data(self,params):
		f=float(params['freq'])
		x = pd.Series(np.arange(0,2*np.pi,np.pi/150))
		y1 = pd.Series(np.sin(f*x))
		y2 = pd.Series(np.sin(2*f*x))
		df=pd.concat([x,y1,y2],axis=1)
		df.columns=['x','y1','y2']
		return df

if __name__ == '__main__':
	app = SimpleSineApp()
	app.launch()
#####################