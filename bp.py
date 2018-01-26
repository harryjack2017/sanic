from sanic import Sanic
from sanic.response import json
from sanic import Blueprint

app = Sanic(__name__)

blueprint1 = Blueprint("name1", url_prefix="/my_blueprint1")
blueprint2 = Blueprint("name2", url_prefix = "/my_blueprint2")
blueprint3 = Blueprint("name3", url_prefix = "/my_blueprint3")

@blueprint1.route("/foo")
async def foo1(request):
    return json({"msg": " from blueprint1"})

@blueprint2.route("/foo")
async def foo2(request):
    return json({"msg": "from blueprint2"})

@blueprint3.websocket("/foo")
async def foo3(request, ws):
    while True:
        data = "hello"
        print("Sending Data:"+data)
        await ws.send(data)
        data= await ws.recv()
        print("Received:"+data)


app.blueprint(blueprint1)
app.blueprint(blueprint2)
app.blueprint(blueprint3)

app.run(host="0.0.0.0",port=8000, debug=True)
