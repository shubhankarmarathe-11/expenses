from flask import Flask, request
from flask import render_template
from flask import redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///expenses.sqlite"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

class expenses(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    cost = db.Column(db.Integer, nullable=False)
    Note = db.Column(db.String(10000), nullable=False)
    date_created = db.Column(db.DateTime, default = datetime.now())

    def __repr__(self) -> str:
        return f"{self.cost} - {self.Note}"


@app.route('/')
def home():
    allExpenses = expenses.query.all()
    return render_template("index.html",allExpenses=allExpenses)

@app.route('/AddExpenses', methods=['GET', 'POST'])
def AddExpenses():
    if request.method == 'POST':
        cost = request.form['Amount']
        Note = request.form['note']
        Expenses = expenses(cost=cost,Note=Note)
        db.session.add(Expenses)
        db.session.commit()
        return redirect("/")
    return render_template("add_expen.html")

if __name__ == '__main__':
   app.run()