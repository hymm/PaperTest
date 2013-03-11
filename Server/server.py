from twisted.web import server, resource
from twisted.web.static import File
from twisted.internet import reactor
import datetime

class TimeJson(resource.Resource):
    def render_GET(self, request):
        return datetime.datetime.now().ctime()

class FormPage(resource.Resource):
    def render_GET(self, request):
        return ''

    def render_POST(self, request):
        newdata = request.content.getvalue()
        print newdata
        return ''

if __name__ == '__main__':
    root = File('.')
    root.putChild('test', FormPage())
    root.putChild('time', TimeJson())
    site = server.Site(root)
    reactor.listenTCP(8080, site)
    reactor.run()