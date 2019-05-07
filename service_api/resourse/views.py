from sanic import response
from sanic.response import text
from sanic.views import HTTPMethodView
from .domain import *
from .forms import ContractSchema


class SmokeView(HTTPMethodView):
    @staticmethod
    def get(request):
        return response.json({'message': 'Service enabled'}, headers={'Service': 'Contracts'}, status=200)


class ContractsView(HTTPMethodView):
    @staticmethod
    async def get(request):
        contracts = await get_all_contracts()
        data = ContractSchema().dump(contracts, many=True)
        return response.json(data)


class ContractView(HTTPMethodView):
    @staticmethod
    async def get(request, pk):
        contract = await get_contract(pk)
        data = ContractSchema().dump(contract, many=True)
        return response.json(data)


class ContractCreateView(HTTPMethodView):
    @staticmethod
    async def post(request):
        await create_contract(request.json)
        return text('Created')


class ContractUpdateView(HTTPMethodView):
    @staticmethod
    async def put(request, pk):
        await update_contract(request.json, pk)
        return text('Updated')


class ContractDeleteView(HTTPMethodView):
    @staticmethod
    async def delete(request, pk):
        await delete_contract(pk)
        return text('Deleted')
