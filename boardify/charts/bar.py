import json
import random
import string

from .chart import BasicChart


class BarChart(BasicChart):
    def __init__(self, data):
        """
        :param data: list with objects {"label": "examplekey", "value": "examplevalue", "color": "rgba(75, 192, 192, 0.2)"}
        :return:
        """

        self.data = data

        # Generate random id for element
        self.id = "".join(random.choice(string.ascii_lowercase) for _ in range(12))

    def generate(self):
        configuration = {
            "type": "bar",
            "data": {
                "labels": self.data.get("labels"),
                "datasets": [{
                    "label": key,
                    "data": value
                } for key, value in self.data.items() if key != "labels"]
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
        script_html = "<script>var ctx=document.getElementById('" + self.id + "').getContext('2d');var myChart=new Chart(ctx," + json.dumps(configuration) + ");</script>"

        return canvas_html + "\n" + script_html + "\n"