from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.secret_key = "Secret"

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:chadthepro123@localhost/booklist'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)
 
 

class Data(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    rate = db.Column(db.String(100))
    rtype = db.Column(db.String(100))
    arrival = db.Column(db.String(100))
    departure = db.Column(db.String(100))
 
 
    def __init__(self, name, email, rate, rtype, arrival, departure):
 
        self.name = name
        self.email = email
        self.rate = rate
        self.rtype = rtype
        self.arrival = arrival
        self.departure = departure
 
 
 
 
 

@app.route('/')
def Index():
    all_data = Data.query.all()
 
    return render_template("index.html", list = all_data)
 
 
 

@app.route('/insert', methods = ['POST'])
def insert():
 
    if request.method == 'POST':
 
        name = request.form['name']
        email = request.form['email']
        rate = request.form['rate']
        rtype = request.form['rtype']
        arrival = request.form['arrival']
        departure = request.form['departure']
 
 
        my_data = Data(name, email, rate, rtype, arrival, departure)
        db.session.add(my_data)
        db.session.commit()
 
        flash("List Inserted Successfully")
 
        return redirect(url_for('Index'))
 
 

@app.route('/update', methods = ['GET', 'POST'])
def update():
 
    if request.method == 'POST':
        my_data = Data.query.get(request.form.get('id'))
 
        my_data.name = request.form['name']
        my_data.email = request.form['email']
        my_data.rate = request.form['rate']
        my_data.rtype = request.form['rtype']
        my_data.arrival = request.form['rate']
        my_data.departure = request.form['departure']
 
        db.session.commit()
        flash("List Updated Successfully")
 
        return redirect(url_for('Index'))
 
 
 
 
#deleting list
@app.route('/delete/<id>/', methods = ['GET', 'POST'])
def delete(id):
    my_data = Data.query.get(id)
    db.session.delete(my_data)
    db.session.commit()
    flash("list Deleted Successfully")
 
    return redirect(url_for('Index'))
 
 
 
 
 
 
if __name__ == "__main__":
    app.run(debug=True)