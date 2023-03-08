from flask import Flask, request

app = Flask(__name__)

@app.get('/welcome')
def say_welcome():
    """Return simple "Welcome" greeting"""

    html = "<html><body><h1>Welcome</h1></body></html>"
    return html

@app.get('/welcome/home')
def say_welcome_home():
    """Return simple "Welcome home" greeting"""

    html = "<html><body><h1>Welcome Home</h1></body></html>"
    return html

@app.get('/welcome/back')
def say_welcome_back():
    """Return simple "Welcome back" greeting"""

    html = "<html><body><h1>Welcome back</h1></body></html>"
    return html



