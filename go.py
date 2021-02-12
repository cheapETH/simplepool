#from http.server import HTTPServer, BaseHTTPRequestHandler
from jsonrpcserver import method, dispatch
from jsonrpcclient import request as jsonrequest
import json
import time


@method
def eth_getWork():
  response = jsonrequest("http://127.0.0.1:8545", "eth_getWork")
  return response.data.result

import socketserver

class MyTCPHandler(socketserver.StreamRequestHandler):
  def handle(self):
    cl = 0
    while 1:
      hh = self.rfile.readline().strip()
      print(hh)
      if b'Content-Length: ' in hh:
        cl = int(hh.split(b'Content-Length: ')[1])
      if hh == b"":
        print("done")
        break
    idat = self.rfile.read(cl).decode('utf-8')
    dat = dispatch(idat)
    print(dat)
    #dat = b'{"jsonrpc":"2.0","id":1,"result":["0xcba3f3e17e543de49b69d0227f4e6afb1ad58528ea8c247ee24d3f2f8e53970d","0x13f58a9760184da06e3feff2e1ccada4ebfaea50a2cca46f7aac6165d81d5fd4","0x000000002dddb2699b111fb60cb7e872dca7cbe2af0fee5762a5a1c50610a15a","0xb4ee8d"]}'
    self.wfile.write(b'HTTP/1.0 200 OK\r\n\r\n'+str(dat).encode('utf-8'))

if __name__ == "__main__":
  HOST, PORT = "localhost", 8080

  socketserver.TCPServer.allow_reuse_address = True
  with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
    server.serve_forever()

