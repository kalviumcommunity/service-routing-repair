import os,urllib.request
from http.server import HTTPServer,BaseHTTPRequestHandler
class Handler(BaseHTTPRequestHandler):
 def do_GET(self):
  try:
   with urllib.request.urlopen(os.environ['API_URL']+'/health',timeout=2) as r: body=r.read()
   self.send_response(200);self.end_headers();self.wfile.write(b'Dashboard API: '+body)
  except Exception as e:
   print('API route failed:',e,flush=True);self.send_response(502);self.end_headers();self.wfile.write(b'API unavailable')
HTTPServer(('0.0.0.0',9000),Handler).serve_forever()
