import sys
import signal
import time
from threading import Thread
from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
from controller import SpotifyController
from urlparse import urlparse, parse_qs
from view import AppView


appView = None

class GETHandler(BaseHTTPRequestHandler):
    controller = SpotifyController()

    def do_GET(self):
        print(self.path)
        if self.path == "/next":
            GETHandler.controller.next()
        if self.path == "/play":
            GETHandler.controller.play()
        if self.path == "/back":
            GETHandler.controller.back()
        if self.path == "/star":
            GETHandler.controller.star()
        if self.path == "/radio":
            GETHandler.controller.radio()
        if self.path.startswith("/progress"):
            GETHandler.controller.progress(self.getParamValue(self.path))
        if self.path.startswith("/volume"):
            GETHandler.controller.volume(self.getParamValue(self.path))
        self.showView()

    def getParamValue(self, path):
        parsed = parse_qs(urlparse(path).query)
        return int(parsed.get('v')[0])

    def showView(self):
        page = appView.create()
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(page)

class GETServer:
    def __init__(self, address, port):
        self.port = port
        self.address = address

    def start(self):
        print("Starting a http server on port %i" % self.port)
        server_address = (self.address, self.port)
        self.httpd = HTTPServer(server_address, GETHandler)
        self.httpd.serve_forever()

if __name__ == "__main__":
    ports = [int(arg) for arg in sys.argv[1:]]
    for port_number in ports:
        address = "192.168.1.15"
        appView = AppView(address + ":" + str(port_number))
        serv = GETServer(address, port_number)
        serv.start()

