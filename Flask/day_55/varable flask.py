# use variable in route using <variable_name>

from flask import Flask
app = Flask(__name__)

@app.route('/username/<name>')
def greet(name):
    return f"hellow{ name}!"

@app.route('/<name>')
def greet(name):
    return f"hellow{ name}!"


if __name__ == "__main__":
    app.run()
    