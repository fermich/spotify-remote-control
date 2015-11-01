class AppView:
    def __init__(self, address):
        self.address = address

    def create(self):
        return self.page(
            self.nl(self.action("index", "INDEX")) +
            self.menu() + 
            self.nl(self.action("star", "STAR")) +
            self.nl(self.action("radio", "RADIO")) +
            self.nl(self.bar("Progress", "progress", 10)) + 
            self.nl(self.bar("Volume", "volume", 11))
        )

    def page(self, body):
        return "<html><head><title>Spotify Remote Control</title></head><body>" + body + "</body></html>"

    def menu(self):
        return self.table(self.row(
            self.cell(self.action("back", "BACK")) +
            self.cell(self.action("play", "PLAY")) +
            self.cell(self.action("next", "NEXT"))))

    def bar(self, name, action, upTo):
        title = "<h1>" + name + ":</h1>"
        cells = ""
        for p in range(0, upTo):
            cells = cells + self.cell(self.action(action + "?v=" + str(p), str(p * 10) + "% "))
        return title + self.table(self.row(cells))

    def action(self, cmd, name):
        return "<h1><a href=http://" + self.address + "/" + cmd + ">| " + name + " |</a></h1>"

    def nl(self, content):
        return str(content) + "<br /><br />"

    def table(self, content):
        return "<table>" + str(content) + "</table>"

    def row(self, content):
        return "<tr>" + str(content) + "</tr>"

    def cell(self, content):
        return "<td>" + str(content) + "</td>"

