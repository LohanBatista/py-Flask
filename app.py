#imports 
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

#create instance of app; __name__ is default param
app = Flask(__name__)
#database config
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecommerce.db'

#database use
db = SQLAlchemy(app)   

#Model
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.Text, nullable=True)

@app.route('/api/products/add', methods=["POST"])
def add_product():
    data = request.json
    if 'name' in data and 'price' in data:
    #when use data=['key'] if the value was not received he acuses error, when we use data.get('key', "") if the value was not received he pass the second value
        product = Product(name=data['name'], price=data['price'], description=data['description'])
        db.session.add(product)
        db.session.commit()
        return jsonify({'message': 'Product added successfully!'})
    return jsonify({'message': 'Invalid product data'}), 400

@app.route('/api/products/delete/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    #pick the product in database
    #verify if exists
    #if exists, delete from database
    #if not exists, return 404 not found
    product = Product.query.get(product_id)
    if product: 
        db.session.delete(product)
        db.session.commit()
        return jsonify({"message": 'Product deleted successfully!'})
    return jsonify({"message": "Product not fount" }), 404


# define root route and the function who will be executed
@app.route('/')
# how to use a function
def hello_world():
    return 'Hello World'


if __name__ == "__main__":
    app.run(debug=True)