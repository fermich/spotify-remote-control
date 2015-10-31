class AppView:
    def __init__(self, address):
        self.address = address

    def create(self):
        return self.page(
            self.nl(self.action("index", "INDEX")) + 
            self.nl(self.action("play", "PLAY")) + 
            self.nl(self.action("next", "NEXT")) + 
            self.nl(self.action("back", "BACK")) +
            self.nl(self.action("star", "STAR")) +
            self.nl(self.progressBar())
        )

    def page(self, body):
        return "<html><head><title>Spotify Remote Control</title></head><body>" + body + "</body></html>"

    def action(self, cmd, name):
        return "<h1><a href=http://" + self.address + "/" + cmd + ">" + name + "</a></h1>"

    def nl(self, content):
        return str(content) + "<br /><br />"

    def progressBar(self):
        bar = ""
        for p in range(1, 10):
            bar = bar + self.action("progress?v=" + str(p), str(p * 10) + "% ")
        return bar

