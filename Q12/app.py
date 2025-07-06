from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1>Hello, World from a Flask app in Docker!</h1>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
# Qualuqer host pode acessar