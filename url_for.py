from sanic import Sanic
from sanic import response
from sanic.response import text
from sanic.exceptions import ServerError
from sanic.exceptions import NotFound

from my_blueprint import bp
from blueprints import blueprint_v1,blueprint_v2
app = Sanic(__name__)

#注册蓝图
app.blueprint(bp)
app.blueprint(blueprint_v1, url_prefix="/v1")
app.blueprint(blueprint_v2, url_prefix="/v2")

@app.route("/")
async def test(request):
    return response.json({"test": True})

@app.route("/number/<integer_arg:int>")
async def integer_handler(request,integer_arg):
    return text("integer - {}".format(integer_arg))

@app.route("person/<name:[A-Z]>")
async def person_handler(request,name):
    return text("person - {}".format(name))


@app.route("/person/post",methods=["GET"])
async def person_post_handler(request):
    return text("POST - request -{}".format(request.args))

async def person_work_handler(request,name):
    print(app.url_for("person_post_handler",post_id=4,arg_one="one",arg_two="two"))
    print(app.url_for("person_post_handler",post_id=4,arg_one=["one","two"],_anchor="anchor"))
    print(app.url_for("person_post_handler",post_id=4,arg_one=["one","two"],arg_two="three",_anchor="anchor",_scheme="http",_external=True,_server="another_server:8080"))
    return text("GET - request - {}".format(name))


@app.websocket("/feed")
async def feed(request,ws):
    data="HEllo"
    print("sending:"+data)
    await ws.send(data)
    data=await ws.recv()
    print("received:"+data)

app.add_route(person_work_handler,"person/work/<name:[a-z]>",methods=["GET"])

@app.route("/query_string")
def query_string(request):
    return text({"parsed":True,"args":request.args,"url":request.url,"query_string":request.query_string})


@app.route("/files")
def post_json(request):
    test_file=request.files.get("test")

    file_parameters={
        "body":test_file.body,
        "name":test_file.name,
        "type":test_file.type
    }
    return text({"file_names":request.files.keys(),"test_file_parameters":file_parameters})



from sanic.request import RequestParameters
args=RequestParameters()
args["titles"]=["post1","post2"]

print(args.get("titles"))
print(args.getlist("titles"))


@app.route("/redirect")
def handle_request(request):
    return response.redirect("/json")


@app.route("/raw")
def handle_raw(request):
    return response.raw("raw data")


@app.route("/killme")
def i_am_ready_to_die(request):
    #raise ServerError("Something bad happend",status_code=500)
    return ignore_404s(request)

@app.exception(NotFound)
def ignore_404s(request,* exception):
    return text("yep,I totally found the page :{}".format(request.url))


@app.middleware("response")
async def custom_banner(request, response):
    response.headers["Server"]="Fake-Server"

@app.middleware("response")
async def prevent_xss(request, response):
    response.headers["x-xss-protection"]="1;mode=block"

# @app.middleware("request")
# def halt_request(request):
#     return text("I halt the request")
#
# @app.middleware("response")
# def halt_response(request,response):
#     return text("I halt the response")


# @app.listener("before_server_start")
# async def setup_db(app,loop):
#     app.db=await db_setup()
#
# @app.listener("after_server_start")
# async def notify_server_started(app,loop):
#     print("Server successfully started")
#
# @app.listener("before_server_stop")
# async def notify_server_stopping(app, loop):
#     print("Server shutting down")
#
# @app.listener("after_server_stop")
# async def close_db(app, loop):
#     await app.db.close()

@app.route("/cookie")
async def test(request):
    test_cookie=request.cookies.get("test")
    return text("test cookie set to:{}".format(test_cookie))



@app.route("/setcookie")
async def setcookie(request):
    response=text("there is a cookie in response")
    response.cookies["test"]="it workd"
    return response



if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000)
