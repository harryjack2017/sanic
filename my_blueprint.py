#! usr/env python3

from sanic.response import json
from sanic.response import text
from sanic import Blueprint
from sanic.exceptions import NotFound
bp=Blueprint("my_blueprint")

@bp.route("/bp")
async def bp_root(request):
    return json({"my":"blueprint"})


@bp.middleware
async def print_on_request(request):
    print("I am a spy")

# @bp.middleware("request")
# async def halt_request(request):
#     return json("I halt the request")
#
# @bp.middleware("response")
# async def halt_response(request, response):
#     return json(" bp halt the response ")


#只利用蓝图来应用全局异常
@bp.exception(NotFound)
def ignore_404s(request,response):
    return text({"found the page:{}".format(request.url)})