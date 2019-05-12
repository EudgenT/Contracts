from sanic.views import HTTPMethodView
from sanic import response
import requests


async def registration():
    sda = "http://0.0.0.0:31502/"
    data = {
            "service": "Contracts",
            "host": "0.0.0.0",
            "port": 8007,
            }
    headers = {"Content-type": "application/json"}
    requests.post(sda, json=data, headers=headers)


class SmokeResource(HTTPMethodView):
    def get(self, request):
        return response.json(
                             {'message': 'Service enabled'},
                             headers={'Service': 'Contracts'},
                             status=200
                              )
