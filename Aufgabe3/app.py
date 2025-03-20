from http.server import SimpleHTTPRequestHandler, HTTPServer

class MyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"<h1>Hello from  inside the container!</h1>")

if __name__ == "__main__":
    server_address = ("", 8080)  # Listen on all available interfaces, port 8080
    httpd = HTTPServer(server_address, MyHandler)
    print("Serving on posdfljdsfjrt 8080..")
    httpd.serve_forever()

