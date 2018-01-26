from sanic import Sanic
from sanic.response import stream

app = Sanic(__name__)


@app.route("/")
async def test(request):
    async def sample_streaming(response):
        response.write("foo")
        response.write("bar")

    return stream(sample_streaming, content_type="text/csv")


@app.route("/")
async def index(request):
    async def stream_from_db(response):
        conn = await asyncpg.connect(database='test')
        async with conn.transaction():
            async for record in conn.cursor("select generate_series(0,10)"):
                response.write(record[0])

    return stream(stream_from_db)


from sanic.response import json


@app.route("/json")
def post_json(request):
    return json({"received": True, "Message": request.json}, status=200)


from sanic.response import json


@app.route("/query_string")
def query_string(request):
    return json({"parsed": True, "args": request.args, "url": request.url, "query_string": request.query_string})


