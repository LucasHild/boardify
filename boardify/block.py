class BasicBlock:
    def __init__(self):
        self.name = None
        self.description = None
        self.config()

    def config(self):
        pass

    def data(self):
        return ""

    def generate(self):
        html = ""

        if self.name:
            html += "<div class=\"block-title\"><h3>" + self.name + "</h3></div>\n"
        else:
            html += "<div class=\"block-title\"><h3>Untitled</h3></div>\n"

        html += "<div class=\"block-content\">"

        if self.description:
            html += "<p>" + self.description + "</p>\n"

        html += self.data()

        html += "</div>"

        return html