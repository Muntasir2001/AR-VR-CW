import http.server, ssl, socketserver

PORT=3000

context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)

context.load_cert_chain("cert.pem")
server_address = ("0.0.0.0", PORT)

handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(server_address, handler) as httpd:
    httpd.socket = context.wrap_socket(httpd.socket, server_side=True)
    print(f"Server listening on https://localhost:{PORT}")
    httpd.serve_forever()
