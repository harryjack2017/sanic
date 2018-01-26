#! /usr/env python3

from sanic.response import text
from sanic import Blueprint

blueprint_v1=Blueprint("v1", url_prefix="/v1")
blueprint_v2= Blueprint("v2", url_prefix="/v2")

@blueprint_v1.route("/bp1")
async def api_v1_root(request):
    return text("version1")

@blueprint_v2.route("/bp2")
async def api_v2_root(request):
    return text("verson2")

##访问方法：http://0.0.0.0:8000/v1/bp1

