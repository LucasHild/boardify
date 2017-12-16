import random
import string

from .chart import BasicChart


class Table(BasicChart):
    def __init__(self, data):
        """
        :param data: list with lists [["row 1 column 1", "row 1 column 2", "row 1 column 3"], ["row 2 column 1", "row 2 column 2", "row 2 column 3"]]
        :return:
        """

        self.data = data

        # Generate random id for element
        self.id = "".join(random.choice(string.ascii_lowercase) for _ in range(12))

    def generate(self):
        table = "  <table>\n"

        # Add table header
        table_header = self.data.pop(0)
        table += "    <tr>\n"
        table += "      <th>" + "</th><th>".join(table_header) + "</th>\n"
        table += "    </tr>\n"

        # Add rows
        for i in self.data:
            table += "    <tr>\n"
            table += "      <td>" + "</td><td>".join(i) + "</td>\n"
            table += "    </tr>\n"

        table += "  </table>\n"

        return table