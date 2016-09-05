import BaseHTTPServer
from os import curdir , sep

class MyHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        
        if self.path == "/":
            self.path="/test.html"
        try:
            f = open(curdir+sep+self.path)
            self.wfile.write(f.read())
            f.close()
            return 
        except IOError:
            self.send_error(404, "File Not Found : %s" %self.path)
    
print "Listen 8080"
server = BaseHTTPServer.HTTPServer(("",8080),MyHandler)
server.serve_forever()
