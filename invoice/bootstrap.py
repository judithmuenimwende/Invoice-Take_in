from models.user import User
from models.invoice import Invoice
from peewee import SqliteDatabase, IntegrityError, OperationalError

DATABASE = SqliteDatabase("invoice.db")


invoices = [
    {'id': 1, 'user_email': 'john@doe.com', 'design_fee': 20, 'hosting_fee': 100, 'domain_fee': 20,'dev_fee': 100, },
    {'id': 2, 'user_email': 'Judith15@Mueni.com', 'design_fee': 220, 'hosting_fee': 500, 'domain_fee': 50,'dev_fee': 600, }
    
    
]

def initialize():
    DATABASE.connect()
    DATABASE.create_tables([User, Invoice], safe=True)
    try:
        User.create(
            first_name='first_name',
            last_name='last_name',
            email='john@doe.com',
            company='Acme'
        )
    except  IntegrityError:
        pass
    for invoice in invoices:
      try:
        Invoice.create(
                user_email=invoice.get('user_email'),
                design_fee=invoice.get('design_fee'),
                hosting_fee=invoice.get('hosting_fee'),
                domain_fee=invoice.get('domain_fee'),
                dev_fee = invoice.get('dev_fee'),
        )
      except IntegrityError:
        pass
    DATABASE.close()