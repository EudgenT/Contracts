from sanic import Sanic
from Contracts.service_api.resource.views import Contracts
from Contracts.service_api.resource.registration import SmokeResource, registration

app = Sanic()

app.add_route(SmokeResource.as_view(), '/smoke')
app.add_route(Contracts.as_view(), '/contracts')

app.add_task(registration)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8007)
