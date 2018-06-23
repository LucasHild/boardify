import json
from .block import BaseBlock


class BarChart(BaseBlock):
    def __init__(self):
        self.orientation = None
        super().__init__()

    def generate(self):
        data = self.data()

        if self.orientation == "horizontal":
            orientation = "horizontalBar"
        elif self.orientation == "vertical":
            orientation = "bar"
        elif not self.orientation:
            orientation = "bar"
        else:
            orientation = self.orientation

        configuration = {
            "type": orientation,
            "data": {
                "labels": data.get("labels"),
                "datasets": [{
                    "label": key,
                    "data": value,
                    "backgroundColor": data.get("background_color")
                } for key, value in data["datasets"].items()]
            },
            "options": {
                "scales": {
                    "yAxes": [{
                        "ticks": {
                            "beginAtZero": True
                        }
                    }]
                }
            }
        }

        canvas_html = "<canvas id=\"" + self.id + "\"></canvas>"
        script_html = "<script>var ctx=document.getElementById('" + self.id + \
            "').getContext('2d');var myChart=new Chart(ctx," + \
            json.dumps(configuration) + ");</script>"

        return canvas_html + "\n" + script_html + "\n"
