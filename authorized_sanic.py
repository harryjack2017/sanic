# -*- coding :utf-8 -*-
from sanic import Sanic
from sanic.response import json
from functools import wraps


app = Sanic()

def check_request_for_authorization(request):
    return False

def authorized(f):
    # def decorator(f):
        @wraps(f)
        async def decorated_function(request, *args, **kwargs):
            is_authorized = check_request_for_authorization(request)

            if is_authorized:
                response = await f(request, *args, **kwargs)
                return response

            else:
                return json({"status":"no_authorized"},403)

        return decorated_function
    # return decorator


@app.route("/")
@authorized
async def test(request):
    return json({"status":"authorized"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)