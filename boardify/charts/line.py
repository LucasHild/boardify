import json
import random
import string

from .chart import BasicChart


class LineChart(BasicChart):
    def __init__(self, data):
        """
        :param data: list with objects
        :return:
        """
        self.data = data

        # Generate random id for element
        self.id = "".join(random.choice(string.ascii_lowercase) for _ in range(12))

    def generate(self):
        configuration = {
            "type": "line",
            "data": {
                "labels": self.data.get("labels"),
                "datasets": [{
                    "label": key,
                    "data": value,
                    "fill": False,
                    "backgroundColor": self.data.get("color").get(key),
                    "borderColor": self.data.get("color").get(key)
                } for key, value in self.data["datasets"].items()]
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
