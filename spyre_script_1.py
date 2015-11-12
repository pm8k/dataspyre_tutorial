#####################
from spyre import server

class SimpleApp(server.App):
    title = "Simple App"
    inputs = [{ "type":"text",
                "key":"words",
                "label": "write here",
                "value":"hello world"}]
    outputs = [{"type":"html",
                "id":"some_html",
                "control_id":"button1"}]
    controls = [{"type":"button",
                 "label":"press to update",
                 "id":"button1"}]
    def getHTML(self, params):
        words = params['words']
        return "Here are some words: <b>%s</b>"%words

app = SimpleApp()
app.launch()