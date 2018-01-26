from sanic import response
from sanic import Sanic
from sanic.exceptions import ServerError
from sanic.exceptions import abort

app = Sanic(__name__)


@app.route("/raw")
def handler_request(request):
    return response.raw("raw data")


@app.route("/json")
def handler_request(request):
    return response.json({"message": "hello world"}, status=200)


# ----
@app.route("/killme")
def handler_except(request):
    raise ServerError("something bad happend", status_code=500)


@app.route("/abort")
def handler_abort(request):
    abort(401)
    response.text("ok")

app.run(host="0.0.0.0", port=8000)
