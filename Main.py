from flask import Flask, render_template, request, flash, redirect, url_for
from wtforms import Form, StringField, TextAreaField, RadioField, SelectField,validators

app = Flask(__name__)
class FormData(Form):
    bank_number = StringField("Enter bank account number:", [validators.Length(min=1, max=9), validators.DataRequired()])
    amount_payable = StringField("Enter amount payable:", [validators.Length(min=1, max=999), validators.DataRequired()])
    bank_payto = StringField("Enter bank account number(pay to):", [validators.Length(min=1, max=9), validators.DataRequired()])
    specify = StringField("Specify:", [validators.Length(min=1, max=20), validators.DataRequired()])
    date = StringField("Enter date:", [validators.Length(min=1, max=9), validators.DataRequired()])
    category = SelectField("Category:", [validators.DataRequired()], choices=[("A", "all"), ('U', "utility"), ("O", 'others'), ("S", "standardtransfer")])

@app.route('/')
def root():
    return render_template('login.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/accounts')
def accounts():
    return render_template('accounts.html')

@app.route('/giro')
def giro():
    return render_template('giro.html')

@app.route('/spendinganalytics')
def spendinganalytics():
    return render_template('spendinganalytics.html')

@app.route("/transaction")
def transaction():
    return render_template("transaction.html")

@app.route('/rewards')
def rewards():
    return render_template('rewards.html')

@app.route('/faqs')
def faqs():
    return render_template('faqs.html')

@app.route('/logout')
def logout():
    return render_template('logout.html')

if __name__ == '__main__':
    app.run()
