# http://learnpythonthehardway.org/book/ex50.html
# see project - gothonweb

import web

urls = (
    '/', 'index',
    '/search', 'response',
    'inclination', 'share something to me'
)

app = web.application(urls, globals())


class index:
    def GET(self):
        greeting = "Hello World"
        return greeting


class response:
    def GET(self):
        return 'it\'s empty'


if __name__ == "__main__":
    app.run()
