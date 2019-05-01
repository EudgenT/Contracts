from sqlalchemy import *

metadata = MetaData()

Contract = Table('Contract', metadata,
                 Column('id', String(32), primary_key=True),
                 Column('title', String(50), nullable=False),
                 Column('contract_start_date', Date),
                 Column('contract_end_date', Date),
                 Column('customer', Integer, ForeignKey("contractor.contractor_id")),
                 Column('executor', Integer, ForeignKey("contractor.contractor_id"))
                 )

Contractor = Table('contractor', metadata,
                   Column('contractor_id', Integer, primary_key=True),
                   Column('title', String(50), nullable=False),
                   Column('checking_account', Integer),
                   Column('contract_end_date', Date)
                   )
