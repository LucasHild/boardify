from .block import BaseBlock


class Table(BaseBlock):
    def generate(self):
        data = self.data()

        table = "  <table>\n"

        # Add table header
        table_header = data.pop(0)
        table += "    <tr>\n"
        table += "      <th>" + "</th><th>".join(table_header) + "</th>\n"
        table += "    </tr>\n"

        # Add rows
        for row in data:
            table += "    <tr>\n"
            table += "      <td>" + "</td><td>".join(row) + "</td>\n"
            table += "    </tr>\n"

        table += "  </table>\n"

        return table
