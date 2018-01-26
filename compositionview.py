from sanic import Sanic
from sanic.views import CompositionView
from sanic.response import text

app=Sanic(__name__)

def get_handler(request):
    return text(" i am get ")

view = CompositionView()

view.add(["GET"],get_handler)

view.add(["POST","PUT"], lambda request: text(" i am a post/put method"))

app.add_route(view, "/")