import os

from flask import Flask
from .server import _EndpointAction


class BaseDashboard:
    def __init__(self):
        self.blocks = []
        self.name = None
        self.theme_color = "rgb(35, 76, 94)"
        self.config()

    def config(self):
        raise AttributeError(
            self.__class__.__name__ + " needs config() method"
        )

    def add_block(self, block):
        self.blocks.append(block())

    def generate(self):
        # Open the html template
        with open(os.path.dirname(os.path.abspath(__file__)) + "/index.html", "r") as f:
            file = f.read()

        # Set dashboard title
        if self.name:
            html = file.replace("TITLE", self.name)
        else:
            html = file.replace("TITLE", "Dashboard")

        main_html = ""

        # Calculate how many boxes have to go in the columns
        if len(self.blocks) % 2 == 0:
            # Event number
            first_column_length = int(len(self.blocks) / 2)
            second_column_length = int(len(self.blocks) / 2)
        else:
            # Odd number
            first_column_length = int((len(self.blocks) - 1) / 2 + 1)
            second_column_length = int((len(self.blocks) - 1) / 2)

        # Create arrays for the first and the second column based on the calculated distribution
        first_column = self.blocks[:first_column_length]
        second_column = self.blocks[-second_column_length:] if len(
            self.blocks) > 1 else []

        # For every column
        for column in [first_column, second_column]:
            main_html += "<div class=\"column\">\n"

            # For every block in the column
            for block in column:
                main_html += "<div class=\"block\">\n"
                main_html += block.generate_block() + "\n"
                main_html += "</div>\n"

            main_html += "</div>\n"

        return html.replace("THEME_COLOR", self.theme_color).replace("HTMLCONTENT", main_html)

    def run(self):
        self.app = Flask(__name__)
        self.app.add_url_rule(
            "/", "index", _EndpointAction(response=self.generate()))
        self.app.run(debug=True, port=7000)
