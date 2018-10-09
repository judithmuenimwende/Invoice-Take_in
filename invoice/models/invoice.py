from peewee import (Model, CharField,                          SqliteDatabase,
                    IntegrityError, IntegerField, TextField)

DATABASE = SqliteDatabase("invoice.db")

invoices = [
    {'id': 1, 'user_email': 'john@doe.com', 'design_fee': 20, 'hosting_fee': 100, 'domain_fee': 20,'dev_fee': 100, },
    {'id': 2, 'user_email': 'fatma15@doe.com', 'design_fee': 20, 'hosting_fee': 100, 'domain_fee': 20,'dev_fee': 100, }
    
    
]


class Invoice(Model):
    user_email = CharField(max_length=100)
    design_fee = IntegerField()
    hosting_fee = IntegerField()
    domain_fee = IntegerField()
    dev_fee = IntegerField()


    @classmethod
    def list(cls):
        
        invoices = Invoice.select()
        return invoices


    class Meta:
        database = DATABASE