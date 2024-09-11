from http.server import HTTPServer, BaseHTTPRequestHandler

class HelloWorldHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b'Hello World')

def run_server(port=8000):
    server_address = ('0.0.0.0', port)  # Changed from '' to '0.0.0.0'
    httpd = HTTPServer(server_address, HelloWorldHandler)
    print(f'Server running on port {port}')
    httpd.serve_forever()

if __name__ == '__main__':
    run_server()