import json

from .block import BaseBlock


class LineChart(BaseBlock):
    def generate(self):
        data = self.data()

        configuration = {
            "type": "line",
            "data": {
                "labels": data.get("labels"),
                "datasets": [{
                    "label": key,
                    "data": value,
                    "fill": False,
                    "backgroundColor": data.get("color").get(key),
                    "borderColor": data.get("color").get(key)
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
