from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)



@app.route('/')
def Index():

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)