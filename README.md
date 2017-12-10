# boardify

A web-based dashboard to analyzing your data with Python

![](https://img.shields.io/badge/license-MIT-blue.svg?style=flat-square)
[![PyPI](https://img.shields.io/pypi/v/boardify.svg?style=flat-square&colorB=dfb317)](https://pypi.python.org/pypi/boardify)

![Screenshot](https://raw.githubusercontent.com/Lanseuo/boardify/master/screenshot.png)

## Installation

```bash
pip3 install boardify
```

## Usage

```python
from boardify import *


# Class for the dashboard
class FruitDashboard(BasicDashboard):
    def config(self):
        self.name = "Fruit Company"

        # Add Blocks to the dashboard
        self.add_block(Products())
        self.add_block(NicestFruit())


# Block contains HTML Code
class Products(BasicBlock):
    def config(self):
        self.name = "Products"
        self.description = "A list of our products"

    def data(self):
        return """<ul>
        <li>Apple</li>
        <li>Orange</li>
        <li>Banana</li>
        <li>Kiwifruit</li>
        <li>Blueberry</li>
        <li>Grapes</li>
        </ul>"""


# Block renders a bar chart
class NicestFruit(BasicBlock):
    def config(self):
        self.name = "Nicest Fruit"
        self.description = "A survey of 145 people asked them \"Which is the nicest fruit?\""

    def data(self):
        # Define the data for the chart
        data = [
            {"label": "Apple", "value": 35, "color": "rgba(247, 0, 0, 0.2)"},
            {"label": "Orange", "value": 20, "color": "rgba(254, 114, 0, 0.2)"},
            {"label": "Banana", "value": 45, "color": "rgba(237, 250, 0, 0.2)"},
            {"label": "Kiwifruit", "value": 10, "color": "rgba(12, 250, 0, 0.2)"},
            {"label": "Blueberry", "value": 30, "color": "rgba(0, 85, 250, 0.2)"},
            {"label": "Grapes", "value": 5, "color": "rgba(177, 0, 250, 0.2)"}
        ]

        # Generate the bar chart
        return BarChart(data, label="Fruits").generate()


# Run the server
dashboard = FruitDashboard()
dashboard.run()
```
