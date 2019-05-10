from sanic import response
from sanic.response import text
from sanic.views import HTTPMethodView
from .domain import *
from .forms import ContractSchema


class SmokeResource(HTTPMethodView):
    def get(self, request):
        return response.json({'message': 'Service enabled'}, headers={'Service': 'Contracts'}, status=200)


class ContractsResource(HTTPMethodView):
    async def get(self, request):
        contracts = await get_all_contracts()
        result = ContractSchema().dump(contracts, many=True)
        return response.json(result.data)


class ContractResource(HTTPMethodView):
    async def get(self, request, pk):
        contract = await get_contract(pk)
        result = ContractSchema().dump(contract, many=True)
        return response.json(result.data)


class ContractCreateResource(HTTPMethodView):
    async def post(self, request):
        await create_contract(request.json)
        return text('Created')


class ContractUpdateResource(HTTPMethodView):
    async def put(self, request, pk):
        await update_contract(request.json, pk)
        return text('Updated')


class ContractDeleteResource(HTTPMethodView):
    async def delete(self, request, contact_id):
        await delete_contract(contact_id)
        return text('Deleted')
