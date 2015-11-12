#########CODE##########
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
				"action_id":"sine_wave_plot"},
				{ "type":"radiobuttons",
				"key":"func_type",
				"label":"func_type",
				"action_id":"sine_wave_plot",
				"options":[
					{"label":"Sine","value":"sin","checked":True},
					{"label":"Cosine","value":"cos"}]},
				{ "type":"dropdown",
				"key":"datatoplot",
				"options":[
					{"label":"x","value":"y1"},
					{"label":"2x","value":"y2"}],
				"label":"Data to Plot",
				"action_id":"sine_wave_plot"},
				{ "type":"slider",
				"key":"x_slider",
				"value":100,
				"min":1,
				"max":200,
				"label":"x_axis",
				"action_id":"sine_wave_plot"},
				{ "type":"checkboxgroup",
				"key":"checkboxes",
				"options":[
					{"label":"show x gridlines","value":"showx","checked":True},
					{"label":"show y gridlines","value":"showy"}
				],
				"label":"Plot Options",
				"action_id":"sine_wave_plot"}]
	tabs=["Plot","Data"]
	outputs = [{"type":"plot",
				"id":"wave_plot",
				"tab":"Plot",
				"control_id":"sine_wave_plot"},
				{"type":"table",
				"id":"wave_data",
				"tab":"Data",
				"control_id":"sine_wave_plot"}]
	controls = [{"type":"HIDDEN",
                 "id":"sine_wave_plot"}]
	def getPlot(self, params):
		f = float(params['freq'])
		data = params['datatoplot']
		checkboxlist=params['checkboxes']
		df=self.getData(params)
		fig = plt.figure()
		splt1 = fig.add_subplot(1,1,1)
		splt1.plot(df.x,df[data])
		if 'showx' in checkboxlist:
			splt1.xaxis.grid(True)
		if 'showy' in checkboxlist:
			splt1.yaxis.grid(True)
		return fig
	def getData(self,params):
		f=float(params['freq'])
		index=int(params['x_slider'])
		functouse=params['func_type']
		funcdict={"sin":np.sin,"cos":np.cos}
		func=funcdict[functouse]
		x = pd.Series(np.arange(0,2*np.pi,np.pi/150))
		y1 = pd.Series(func(f*x))
		y2 = pd.Series(func(2*f*x))
		df=pd.concat([x,y1,y2],axis=1)
		df.columns=['x','y1','y2']
		return df[:index]

if __name__ == '__main__':
	app = SimpleSineApp()
	app.launch()
#########################