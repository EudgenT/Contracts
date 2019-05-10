from Contracts.models import Contract
from Contracts.database import connection


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
        async for row in conn.execute(Contract.select().where(Contract.c.id == pk)):
            data.append(row)
    return data


async def create_contract(json):
    engine = await connection()
    async with engine.acquire() as conn:
        await conn.execute(Contract.insert().values(title=json['title'],
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
        await conn.execute(Contract.update().
                           where(Contract.c.id == pk).values(title=json['title'],
                                                             amount=json['amount'],
                                                             start_date=json['start_date'],
                                                             end_date=json['end_date'],
                                                             customer=json['customer'],
                                                             executor=json['executor']
                                                             )
                           )


async def delete_contract(pk):
    engine = await connection()
    async with engine.acquire() as conn:
        await conn.execute(Contract.delete().where(Contract.c.id == pk))
