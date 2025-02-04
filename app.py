#imports 
from flask import Flask

#create instance of app; __name__ is default param
app = Flask(__name__)

# define root route and the function who will be executed
@app.route('/')
# how to use a function
def hello_world():
    return 'Hello World'


if __name__ == "__main__":
    app.run(debug=True)