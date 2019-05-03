from sqlalchemy import *

metadata = MetaData()

Contract = Table(
                 'Contract', metadata,
                 Column('id', String(32), primary_key=True),
                 Column('title', String(50), nullable=False),
                 Column('start_date', Date),
                 Column('end_date', Date),
                 Column('customer', Integer, ForeignKey("Contractor.id")),
                 Column('executor', Integer, ForeignKey("Contractor.id"))
            )

Contractor = Table(
                   'Contractor', metadata,
                   Column('id', String(32), primary_key=True),
                   Column('title', String(50), nullable=False),
                   Column('checking_account', Integer)
            )
