from sanic import Sanic
from sanic import response

app=Sanic(__name__)

@app.route("/")
def handle_request(requst):
    return Sanic.response.redirect("/redirect")

@app.route("/redirect")
async def test(request):
    return response.json({"redirected":True})

app.run(host="0.0.0.0" , port = 8000)