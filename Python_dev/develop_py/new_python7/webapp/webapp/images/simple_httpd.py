
import BaseHTTPServer, CGIHTTPServer  
  
port = 8080  
  
httpd = BaseHTTPServer.HTTPServer(('', port), CGIHTTPServer.CGIHTTPRequestHandler)  
print ('starting simple_httpd on port :' + str(httpd.server_port))  
httpd.serve_forever()  

