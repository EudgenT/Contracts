from Contracts.service_api.domain.models import Contract
from Contracts.database import connection
from sqlalchemy import or_


async def get_all_contracts():
    engine = await connection()
    data = []
    async with engine.acquire() as conn:
        async for row in conn.execute(Contract.select()):
            data.append(row)
    return data


async def get_contract(pk):
    engine = await connection()
    data = []
    async with engine.acquire() as conn:
        async for row in conn.execute(
                Contract.select().where(Contract.c.id == pk)
                                      ):
            data.append(row)
    return data


async def create_contract(json):
    engine = await connection()
    async with engine.acquire() as conn:
        await conn.execute(
            Contract.insert().values(title=json['title'],
                                     amount=json['amount'],
                                     start_date=json['start_date'],
                                     end_date=json['end_date'],
                                     customer=json['customer'],
                                     executor=json['executor']
                                     )
                           )


async def update_contract(json, pk):
    engine = await connection()
    async with engine.acquire() as conn:
        query = Contract.update().where(
            Contract.c.id == pk).values(title=json['title'],
                                        amount=json['amount'],
                                        start_date=json['start_date'],
                                        end_date=json['end_date'],
                                        customer=json['customer'],
                                        executor=json['executor']
                                        )
        await conn.execute(query)


async def delete_contract(pk):
    engine = await connection()
    async with engine.acquire() as conn:
        await conn.execute(Contract.delete().where(Contract.c.id == pk))


async def get_contracts(json):
    engine = await connection()
    async with engine.acquire() as conn:
        queryset = []
        query = Contract.select().where(
            or_(Contract.c.executor.in_(json.get("executor", ['None'])),
                Contract.c.id.in_(
                    json.get("id", ['00000000-0000-0000-0000-000000000000'])
                                  ),
                Contract.c.customer.in_(json.get("customer", ['None'])),
                Contract.c.start_date.in_(
                    json.get("start_date", ['2000-01-01'])
                                          ),
                Contract.c.end_date.in_(json.get("end_date", ['1000-01-01'])),
                Contract.c.title.in_(json.get("title", ['None'])),
                Contract.c.amount.in_(json.get("amount", [0]))
                )
                                        )
        async for item in conn.execute(query):
            queryset.append(item)
    return queryset
