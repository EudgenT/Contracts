from sanic import Sanic
from Contracts.service_api.resourse.views import SmokeView, ContractsView, ContractCreateView, \
    ContractUpdateView, ContractDeleteView, ContractView

app = Sanic()

app.add_route(SmokeView.as_view(), '/smoke')
app.add_route(ContractsView.as_view(), '/contracts')
app.add_route(ContractView.as_view(), '/contract/<pk>')
app.add_route(ContractCreateView.as_view(), '/contract/insert')
app.add_route(ContractUpdateView.as_view(), '/contract/update/<pk>')
app.add_route(ContractDeleteView.as_view(), '/contract/delete/<pk>')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8001)
