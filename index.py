from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello World!"

@app.route('/contacts')
def home():
    return "Fale comigo!"

if __name__ == '__main__':
    app.run(debug=True)