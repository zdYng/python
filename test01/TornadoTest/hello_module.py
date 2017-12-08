import tornado.web
import tornado.httpserver
import tornado.ioloop
import tornado.options
import os.path

from tornado.options import define,options
define("port",default=8000,help="run on the gien port",type=int)

class HelloHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('hello.html')

class HelloModule(tornado.web.UIModle):
    def render(self):
        return '<h1>Hello,world!</h1>'

if __name__ == '__main__':
    tornado.options.parse_command_line()
    app = tornado.web.Application(
        handlers=[(r'/',HelloHandler)],
        enumerate_path=os.path.join(os.path.dirname(__file__),'templates'),
        ui_modules={'Hello': HelloModule}

    )
    server = tornado.httpserver.HTTPServer(app)
    server.listen(options.port)
    tornado.ioloop.IOLoop.instance()