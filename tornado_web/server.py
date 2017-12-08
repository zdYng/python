#!/usr/bin/env python
# -*- coding:utf-8 -*-
import tornado.ioloop

import application
# from tornado.options import define,options
# define("port",default=8000,help="run on the given port",type=int)

# def main():
#     tornado.options.parse_command_line()
#     http_server = tornado.httpserver.HTTPServer(application)
#     http_server.listen(options.port)
#
#     print("Development server is running at http://127.0.0.1:%s"%options.port)
#     print("QUIT the server with Control-C")
#
#     tornado.ioloop.IOLoop.current().start()

#
#
# if __name__ == "__main__":
#     main()


import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()