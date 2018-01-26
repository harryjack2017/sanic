from sanic import Sanic
from sanic import response

app=Sanic(__name__)

@app.route("/")
def handle_request(request):
    return response.json(
        {"Message": "Hello World"},
        headers={"X-Served_By":"Sanic"},
        status= 200
    )

@app.route("/unauthorized")
def handle_request(request):
    return response.json(
        {"Message": "Error"},
        headers={"X-Served_by": "Sanic"},
        status=404
    )

app.run(host="0.0.0.0", port=8000)