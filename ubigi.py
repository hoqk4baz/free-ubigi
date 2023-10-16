import http.server
import socketserver
import threading
import requests

class ThreadedHTTPServer(socketserver.ThreadingMixIn, http.server.HTTPServer):
    pass

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = '/index.html'  # Kök URL'yi index.html dosyasına yönlendir
        elif self.path == '/values':
            head = {
                "Pragma": "no-cache",
                "Origin": "ionic://ubigi.me",
                "Cache-Control": "no-cache",
                "X-Authorization-Timestamp": "1697453980036",
                "Content-Length": "0",
                "Authorization": "HMAC E591rrXWZPWRunValdVLVPc7C9Me1Zlilr3tqh+kJfY=",
                "Connection": "keep-alive",
                "Accept-Encoding": "gzip, deflate, br",
                "Accept": "application/json",
                "Accept-Language": "tr-TR,tr;q=0.9",
                "Expires": "-1",
                "Host": "ubigi.me",
                "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148"
            }
            url = "https://ubigi.me/scapi/sims/reservation"
            a = requests.post(url, headers=head)
            b = a.json()
            smdp_address = b["smdpAddress"]
            matching_id = b["matchingId"]
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            response_text = f'{{"smdp": "{smdp_address}", "matching": "{matching_id}"}}'
            self.wfile.write(response_text.encode())
            return

        super().do_GET()

if __name__ == '__main__':
    port = 1055
    with ThreadedHTTPServer(("", port), MyHandler) as httpd:
        print(f"Serving at port {port}")
        server_thread = threading.Thread(target=httpd.serve_forever)
        server_thread.daemon = True
        server_thread.start()
        server_thread.join()
