from flask import Flask
app = Flask(__name__)

@app.route('/')
def Home():
    return 'Welcome to Home Page! To view the message use /hello in the URL'

@app.route('/hello')
def hello_world():
    return 'Hello World!'
    
if __name__ == "__main__":
    app.run(debug=True)
