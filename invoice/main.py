

from flask import (Flask, render_template, request)
from models.user import User
from models.invoice import Invoice
import bootstrap
app_start_config = {'debug': True, 'port': 8080, 'host': '0.0.0.0'}
app = Flask(__name__)


@app.route('/')
def index():
    bootstrap.initialize()
    user = User.select().where(
        User.email == "john@doe.com"
    ).get()
    invoice = Invoice.select().where(
        Invoice.user_email == user.email
    ).get()
    total = invoice.design_fee + invoice.hosting_fee + invoice.domain_fee + invoice.dev_fee
    return render_template('invoice.html', user=user, invoice=invoice, total=total)

@app.route('/invoice/generate', methods=['POST', 'GET'])
def generate():
  invoice = dict(request.form.items())
  total = ( int(invoice.get('design_fee', 10))+
  int(invoice.get('hosting_fee', 90)) + 
  int(invoice.get('domain_fee', 4)) + 
  int(invoice.get('dev_fee', 8))
  )
  return render_template('user_generated_invoice.html', invoice=invoice, total=total)
@app.route('/invoice/new', methods=['POST', 'GET'])
def new_template():
  return render_template('invoice_form.html')
  
@app.route('/invoice/list', methods=['POST','GET'])
def invoice():
   invoices = Invoice.select()

   return render_template("list.html", invoices = invoices)
@app.route('/invoice/save')
def all_invoice():
    invoices = Invoice.list()
    return render_template('list.html', invoices=invoices)

if __name__ == '__main__':
    app.run(**app_start_config)