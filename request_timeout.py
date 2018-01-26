import asyncio
from sanic import Sanic
from sanic import response
from sanic.config import Config
from sanic.exceptions import RequestTimeout

Config.REQUEST_TIMEOUT = 1
app = Sanic(__name__)


@app.route('/')
async def hello(request):
    hell
    await asyncio.sleep(3)
    print("hello again")


@app.exception(RequestTimeout)
def timeout(request, exception):
    return response.text('RequestTimeout from error_handler.', 408)

app.run(host='0.0.0.0', port=8000)