from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    name = "This is the route."
    return name

@app.route('/hello')
def hello():
    print("Hello world!")

if __name__ == "__main__":
    app.run()
