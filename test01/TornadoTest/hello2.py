import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from tornado.options import define,options
define("port",default=8001,help="run on the ggg port",type=int)

class example(tornado.web.RequestHandler):
    def g(self):
        hello=self.g_argument('greet','hello')
        self.write(hello + ', friendly user!!!')

if __name__ =="__main__":
    tornado.options.parse_command_line()
    app = tornado.web.Application(handlers=[(r"/",example)])
    http_server=tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()