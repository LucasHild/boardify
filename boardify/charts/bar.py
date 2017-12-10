import random
import string

from .chart import BasicChart


class BarChart(BasicChart):
    def __init__(self, data, label=None):
        """
        :param data: list with objects {"label": "examplekey", "value": "examplevalue", "color": "rgba(75, 192, 192, 0.2)"}
        :return:
        """

        self.data = data
        self.label = label

        # Generate random id for element
        self.id = "".join(random.choice(string.ascii_lowercase) for _ in range(12))

    def generate(self):
        labels = [d["label"] for d in self.data]
        data = [d["value"] for d in self.data]
        label = "label: '" + self.label + "'," if self.label else ""

        if None not in [d.get("color") for d in self.data]:
            colors = ",backgroundColor:" + str([d.get("color") for d in self.data]).replace("', '", "','") + ",borderColor:" + str([d.get("color") for d in self.data]).replace("'0.2'", "1")
        else:
            colors = ",backgroundColor:['rgba(255, 99, 132, 0.2)','rgba(54, 162, 235, 0.2)','rgba(255, 206, 86, 0.2)','rgba(75, 192, 192, 0.2)','rgba(153, 102, 255, 0.2)','rgba(255, 159, 64, 0.2)'],borderColor:['rgba(255,99,132,1)','rgba(54, 162, 235, 1)','rgba(255, 206, 86, 1)','rgba(75, 192, 192, 1)','rgba(153, 102, 255, 1)','rgba(255, 159, 64, 1)']"

        canvas_html = "<canvas id=\"" + self.id + "\"></canvas>"
        script_html = "<script>var ctx=document.getElementById('" + self.id + "').getContext('2d');var myChart=new Chart(ctx,{type:'bar',data:{labels:" + str(labels) + ",datasets:[{" + label + "data:" + str(data) + colors + ",borderWidth:1}]},options:{scales:{yAxes:[{ticks:{beginAtZero:true}}]}}});</script>"

        return canvas_html + "\n" + script_html + "\n"