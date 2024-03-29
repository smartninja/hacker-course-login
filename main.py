#!/usr/bin/env python
import os
import jinja2
import webapp2


template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=False)


class BaseHandler(webapp2.RequestHandler):

    def write(self, *a, **kw):
        return self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        return self.write(self.render_str(template, **kw))

    def render_template(self, view_filename, params=None):
        if not params:
            params = {}
        template = jinja_env.get_template(view_filename)
        return self.response.out.write(template.render(params))


class MainHandler(BaseHandler):
    def get(self):
        return self.render_template("main.html")


class LoginHandler(BaseHandler):
    def get(self):
        return self.render_template("google-login.html")


class InsecureLoginHandler(BaseHandler):
    def get(self):
        return self.render_template("non-secure-login.html")

    def post(self):
        email = self.request.get("email")
        password = self.request.get("password")
        # don't do anything with it

        return self.render_template("non-secure-thanks.html")


class InsecureLoginThanksHandler(BaseHandler):
    def get(self):
        return self.render_template("non-secure-thanks.html")

app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
    webapp2.Route('/login', LoginHandler),
    webapp2.Route('/login2', InsecureLoginHandler),
    webapp2.Route('/login2/thanks', InsecureLoginThanksHandler),
], debug=True)
