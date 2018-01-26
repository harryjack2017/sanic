from sanic import Sanic
from sanic.views import HTTPMethodView
from sanic.response import text

app=Sanic("some_name")

class SimpleView(HTTPMethodView):

    def get(self,request):
        return text("I am get")

    def post(self,request):
        return text("I am post")

    def put(self,request):
        return text("i am put")

    def patch(self,request):
        return text(" i ma patch")

    def delete(self,request):
        return text("i am delete")

app.add_route( SimpleView.as_view(),"/")