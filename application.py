from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

# our example data model
class Drinks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(120))

    def __repr__(self):
        return f"{self.name} - {self.description}"

# our assignment book model
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String(100), unique=True, nullable=False)
    author = db.Column(db.String(100), unique=True, nullable=False)
    publisher = db.Column(db.String(100), unique=True, nullable=False)

    def __repr__(self):
        return f"{self.book_name} - {self.author} - {self.publisher}"



@app.route('/')
def index():
    return 'Hello!'

@app.route('/drinks')
def get_drinks():
    drinks = Drinks.query.all()
    output = []
    for drink in drinks:
        drink_data = {'name':drink.name, 'description':drink.description}
        output.append(drink_data)

    return {"drinks": output}

@app.route('/drinks/<id>')
def get_drink(id):
    drink = Drinks.query.get_or_404(id)
    return {"name":drink.name, "description":drink.description}

@app.route('/drinks', methods=['POST'])
def add_drink():
    drink = Drinks(name=request.json['name'], description=request.json['decription'])
    db.session.add(drink)
    db.session.commit()
    return {'id':drink.id}


#route for /book
@app.route('/books')
def get_books():
    books = Book.query.all()
    output = []
    for book in books:
        book_data = {'book_name':book.book_name, 'author':book.author, 'publisher':book.publisher}
        output.append(book_data)
    
    return{"books":output}

# id route for /books
@app.route('/books/<id>')
def get_book(id):
    book = Book.query.get_or_404(id)
    return {"book_name":book.book_name, "author":book.author, "publisher":book.publisher}