from marshmallow import Schema, fields, ValidationError, validates


def must_not_be_blank(data):
    if not data:
        raise ValidationError('Data not provided.')


class ContractSchema(Schema):
    id = fields.UUID(required=True, validate=must_not_be_blank)
    title = fields.String(validate=must_not_be_blank)
    amount = fields.Decimal(validate=must_not_be_blank)
    start_date = fields.Date(validate=must_not_be_blank)
    end_date = fields.Date(validate=must_not_be_blank)
    customer = fields.String(validate=must_not_be_blank)
    executor = fields.String(validate=must_not_be_blank)

    @validates('amount')
    def validate_amount(self, amount):
        if amount < 0:
            raise ValidationError("Only positive numbers")
