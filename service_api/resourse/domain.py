from Contracts.models import Contract
from aiopg.sa import create_engine


async def connection():
    engine = await create_engine(user='contracts_user',
                                 database='contracts',
                                 host='127.0.0.1',
                                 port=5432,
                                 password='contracts_user')
    return engine


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
