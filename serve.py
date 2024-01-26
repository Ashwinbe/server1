from flask import Flask

serve = Flask(__name__)

@serve.route('/')
def home():
    return 'Hello, World!'

if __name__ == '__main__':
    serve.run(debug=True)
