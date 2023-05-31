from flask import Flask, render_template, request
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

app = Flask(__name__)

Base = declarative_base()
class Data(Base):
    """
    The Data class has four class variables namely:
        __tablename__: Tells sqlalchemy that the rows must be mapped to this class
        id:Identifies that this is the primary key of the type integer.
        email:Property indicates that the column has the same name as the property and that it is type string.
        height:Property indicates that the column has the same name as the property and that it is type Integer.
    """
    __tablename__ = 'data'
    id=Column(Integer, primary_key=True)
    email=Column("email",String(200))
    height=Column("height",Integer)

    def __init__(self,email_,height_):
        self.email = email_
        self.height = height_

# Create an engine
engine = create_engine('mysql://root:k16s/21810/2014@localhost:3306/height_collector', echo=True)

Base.metadata.create_all(bind=engine)

# Create a configured "session" Class
Session = sessionmaker(bind=engine)
session = Session()



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/success', methods=['POST'])
def success():
    if request.method == 'POST':
        email=request.form["email_name"]
        height=request.form["height"]

        # Add the user input into the database
        data=Data(email,height)
        session.add(data)
        session.commit()
        return render_template('success.html')


if __name__ == '__main__':
    app.run(debug=True)
