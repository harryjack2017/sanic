import re
from sanic import Sanic
from sanic.response import text
from sanic.testing import PORT as PORT_BASE, SanicTestClient
import pytest


@pytest.fixture(scope="session")
def test_port(worker_id):
    m = re.search(r'[0-9]+', worker_id)
    if m:
        num_id = m.group(0)
    else:
        num_id = 0
    port = PORT_BASE + int(num_id)
    return port


@pytest.fixture(scope="session")
def app():
    app = Sanic()

    @app.route('/')
    async def index(request):
        return text('OK')

    return app


@pytest.fixture(scope="session")
def client(app, test_port):
    return SanicTestClient(app, test_port)


@pytest.mark.parametrize('run_id', range(100))
def test_index(client, run_id):
    request, response = client._sanic_endpoint_test('get', '/')
    assert response.status == 200
    assert response.text == 'OK'