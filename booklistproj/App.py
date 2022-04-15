from flask import Flask, render_template
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

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)