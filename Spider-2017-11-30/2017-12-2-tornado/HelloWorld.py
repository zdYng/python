import tornado.ioloop
import tornado.web

# class MainHandler(tornado.web.RequestHandler):
#     def get(self):
#         self.write("Hello World")
# application = tornado.web.Application([
#     (r"/",MainHandler),
# ])
# if __name__ == "__main__":
#     application.listen(8900)
#     tornado.ioloop.IOLoop.instance().start()

class MainHandler_2(tornado.web.RequestHandler):
    def get(self):
        self.write("You requested the main page")
class StoryHandler(tornado.web.RequestHandler):
    def get(self,story_id):
        self.write("You requested the story " + story_id)
application = tornado.web.Application([
    (r"/",MainHandler_2),
    (r"/story/[0-9]+",StoryHandler),
])

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('<html><body><form action="/" method="post">'
                   '<input type="text" name="message>'
                    '<input type="submit" value="Submit">'
                    '</form></body></html>')
    def post(self):
        self.set_header("Content-Type","text/plain")
        self.write("You wrote " + self.get_argument("message"))