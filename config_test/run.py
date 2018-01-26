#!/usr/bin/env python
from sanic import Sanic
from sanic.response import text
from config_test import CONFIGS

app = Sanic()
app.config.from_object(CONFIGS)


@app.route("/")
async def test(request):
    return text('Hello World!')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=app.config['DEBUG'])
