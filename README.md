# boardify

A web-based dashboard to analyzing your data with Python

![](https://img.shields.io/badge/license-MIT-blue.svg?style=flat-square)
[![PyPI](https://img.shields.io/pypi/v/boardify.svg?style=flat-square&colorB=dfb317)](https://pypi.org/project/boardify/)

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
        data = {
            "labels": ["Apple", "Orange", "Banana", "Kiwifruit", "Blueberry", "Grapes"],
            "Survey One": [35, 20, 45, 10, 30, 5],
            "Survey Two": [30, 25, 60, 5, 35, 0]
        }

        # Generate the bar chart
        return BarChart(data, label="Fruits").generate()


# Run the server
dashboard = FruitDashboard()
dashboard.run()
```

Open the dashboard at [http://localhost:7000](http://localhost:7000)

## Made with

- [Flask](http://flask.pocoo.org) - web framework
- [Chart.js](http://www.chartjs.org/) - charts made with JavaScript

## Meta

Lucas Hild - [https://lucas-hild.de](https://lucas.hild.de)  
This project is licensed under the MIT License - see the LICENSE file for details
