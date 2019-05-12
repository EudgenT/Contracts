from sanic import response
from sanic.response import text
from sanic.views import HTTPMethodView
from Contracts.service_api.domain.domain import get_all_contracts, \
    get_contract, create_contract, update_contract, delete_contract, \
    get_contracts
from .forms import ContractSchema


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


class ContractJsonResource(HTTPMethodView):
    async def get(self, request):
        contracts = await get_contracts(request.json)
        result = ContractSchema().dump(contracts, many=True)
        return response.json(result.data)
