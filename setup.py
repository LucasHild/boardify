from setuptools import setup

long_description = """
boardify
========

A web-based dashboard to analyzing your data with Python

|image0| |PyPI| |Requires|

.. figure:: https://raw.githubusercontent.com/Lanseuo/boardify/master/screenshot.png
   :alt: Screenshot

   Screenshot

Installation
------------

.. code:: bash

    pip3 install boardify

Usage
-----

.. code:: python

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
            return \"""<ul>
    <li>Apple</li>
    <li>Orange</li>
    <li>Banana</li>
    <li>Kiwifruit</li>
    <li>Blueberry</li>
    <li>Grapes</li>
    </ul>\"""


    # Block renders a bar chart
    class NicestFruit(BasicBlock):
        def config(self):
            self.name = "Nicest Fruit"
            self.description = "A survey of 145 people asked them " \
                "\"Which is the nicest fruit?\""

        def data(self):
            # Define the data for the chart
            data = {
                "datasets": {
                    "Survey One": [35, 20, 45, 10, 30, 5],
                    "Survey Two": [30, 25, 60, 5, 35, 0],
                },
                "labels": ["Apple",
                           "Orange",
                           "Banana",
                           "Kiwifruit",
                           "Blueberry",
                           "Grapes"],
                "background_color": ["rgb(128, 18, 2)",
                                     "rgb(244, 132, 0)",
                                     "rgb(246, 221, 0)",
                                     "rgba(83, 65, 25, 0.97)",
                                     "rgb(35, 123, 214)",
                                     "rgb(99, 74, 161)"]
            }

            # Generate the bar chart
            return BarChart(data).generate()


    # Run the server
    dashboard = FruitDashboard()
    dashboard.run()


Open the dashboard at http://localhost:7000

Made with
---------

-  `Flask`_ - web framework
-  `Chart.js`_ - charts made with JavaScript

Meta
----

| Lucas Hild - `https://lucas-hild.de`_
| This project is licensed under the MIT License - see the LICENSE file
  for details

.. _Flask: http://flask.pocoo.org
.. _Chart.js: http://www.chartjs.org/
.. _`https://lucas-hild.de`: https://lucas.hild.de

.. |image0| image:: https://img.shields.io/badge/license-MIT-blue.svg?style=flat-square
.. |PyPI| image:: https://img.shields.io/pypi/v/boardify.svg?style=flat-square&colorB=dfb317
   :target: https://pypi.python.org/pypi/boardify
.. |Requires| image:: https://requires.io/github/Lanseuo/boardify/requirements.svg?branch=master
   :target: https://requires.io/github/Lanseuo/boardify/requirements/?branch=master)
"""

setup(
    name="boardify",
    version="0.3.0",
    description=" A web-based dashboard to analyzing your data with Python ",
    long_description=long_description,
    license="MIT",
    author="Lucas Hild",
    author_email="contact@lucas-hild.de",
    url="https://github.com/Lanseuo/boardify",
    packages=["boardify"],
    install_requires=[
        "flask"
    ],
)
