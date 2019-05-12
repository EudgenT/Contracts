from sanic import Sanic
from Contracts.service_api.resource.views import ContractsResource, ContractCreateResource, \
    ContractUpdateResource, ContractDeleteResource, ContractResource, ContractJsonResource
from Contracts.service_api.resource.registration import SmokeResource, registration

app = Sanic()

app.add_route(SmokeResource.as_view(), '/smoke')
app.add_route(ContractsResource.as_view(), '/contracts')
app.add_route(ContractResource.as_view(), '/contract/<pk>')
app.add_route(ContractCreateResource.as_view(), '/contract/insert')
app.add_route(ContractUpdateResource.as_view(), '/contract/update/<pk>')
app.add_route(ContractDeleteResource.as_view(), '/contract/delete/<pk>')
app.add_route(ContractJsonResource.as_view(), '/contract_by_json')

app.add_task(registration)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8007)
