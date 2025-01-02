from flask import Flask

app = Flask("hello")
@app.route('/hello/<name>')
def hello_world(name):
    return f'Hello, {name}!'