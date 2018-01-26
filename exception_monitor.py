"""
author:***
"""

from sanic import Sanic
from sanic.handlers import ErrorHandler
from sanic.exceptions import SanicException
app=Sanic(__name__)

class CustomHandler(ErrorHandler):
    def default(self,request,exception):
        if not isinstance(exception,SanicException):
            print(exception)

        return super().default(request,exception)



handler=CustomHandler()
app.error_handler = handler

@app.route("/")
async def test(request):
    raise SanicException("You broke it")

app.run(host="0.0.0.0",port = 8000, debug = True)