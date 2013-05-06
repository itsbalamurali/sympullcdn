#!/usr/bin/env python
import webapp2


class MainPage(webapp2.RequestHandler):

    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('echo-reply')


app = webapp2.WSGIApplication([('/ping', MainPage)],
                              debug=True)
