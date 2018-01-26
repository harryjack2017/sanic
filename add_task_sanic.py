from sanic import Sanic
import asyncio
from sanic.response import text
app = Sanic()


async def notify_server_after_file_sec():
    await asyncio.sleep(5)
    print("server successfully started")

app.add_task(notify_server_after_file_sec())


@app.route("/")
def index(request):
    return text("index")


if __name__ == "__main__":
    app.run(host="0.0.0.0",port=8000)