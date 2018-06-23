import random
import string


class BaseBlock:
    def __init__(self):
        self.name = None
        self.description = None
        self.config()

        # Generate random id for element
        self.id = "".join(random.choice(string.ascii_lowercase)
                          for _ in range(12))

    def config(self):
        raise AttributeError(
            self.__class__.__name__ + " needs config() method"
        )

    def data(self):
        print()
        raise AttributeError(
            self.__class__.__name__ + " needs data() method"
        )

    def generate(self):
        raise AttributeError(
            self.__class__.__name__ + " needs generate() method"
        )

    def generate_block(self):
        name = self.name or "Untitled"

        html = ""
        html += "<div class=\"block-title\"><h3>" + name + "</h3></div>\n"
        html += "<div class=\"block-content\">"

        if self.description:
            html += "<p>" + self.description + "</p>\n"

        html += self.generate()

        html += "</div>"

        return html
