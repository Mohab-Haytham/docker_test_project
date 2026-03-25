from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello from Alexandria! My Flask App is running in a container."


if __name__== '__main__':
    app.run(host='0.0.0.0', port=5000)
