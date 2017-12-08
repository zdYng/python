# coding:utf-8
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

authorizer = DummyAuthorizer()
authorizer.add_user("qian","123456","F:/",perm="elr")
authorizer.add_anonymous("F:/")

handler =FTPHandler
handler.authorizer = authorizer

server = FTPServer(("127.0.0.1",21),handler)
server.serve_forever()