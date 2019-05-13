from sanic.views import HTTPMethodView
from sanic import response
import aiohttp
import logging


async def registration():
    sda = "http://0.0.0.0:30000/"
    parameters = '?name=Contracts&host=0.0.0.0&port: 8007'
    # data = {
    #     "service": "Contracts",
    #     "host": "0.0.0.0",
    #     "port": 8007,
    # }
    try:
        async with aiohttp.ClientSession() as session:
            await session.post(sda, data=parameters)

    except Exception as exc:
        logging.error(exc)


class SmokeResource(HTTPMethodView):
    def get(self, request):
        return response.json(
                             {'message': 'Service enabled'},
                             headers={'Service': 'Contracts'},
                             status=200
                              )
