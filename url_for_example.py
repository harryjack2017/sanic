from sanic import Sanic
from sanic import response

app = Sanic(__name__)


@app.route("/")
async def index(request):
    url = app.url_for("post_handler", post_id=5)
    return response.redirect(url)


@app.route("/posts/<post_id>")
async def post_handler(request, post_id):
    return response.text("Post - {}".format(post_id))


app.run(host="0.0.0.0", port=8000, debug=True)
