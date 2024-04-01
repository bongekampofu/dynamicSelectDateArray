from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import SelectField


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:\\Users\\Bongeka.Mpofu\\DB Browser for SQLite\\tickets.db'
app.config['SECRET_KEY'] = 'this is a secret key '
db = SQLAlchemy(app)

class Ticket(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    #tickets = db.session.query(Ticket).all()
    return render_template('index.html')


@app.route('/available/<cdate>')
def available(cdate):
    print(cdate)
    cdate = datetime.strptime(cdate, '%Y-%m-%d').date()
    print(cdate)
    print(type(cdate))
    tickets = Ticket.query.filter_by(date=cdate).all()
    print(tickets)
    ticketArray=[]
    for ticket in tickets:
        ticketObj={}
        #ticketObj['id']=ticket.id
        ticketObj['quantity']=ticket.quantity
        ticketArray.append(ticketObj)
        print(ticketArray)
    return jsonify({'tickets' : ticketArray})

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)

