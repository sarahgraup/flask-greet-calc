from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.get("/add/<int:num_a>/<int::num_b>")
def get_num(a, b):
    num_a = request.args.get("a")
    num_b = request.args.get("b")
    sum = add(num_a, num_b)
    return sum


@app.get("/sub/<int:num_a>/<int::num_b>")
def get_num(a, b):
    num_a = request.args.get("a")
    num_b = request.args.get("b")
    sum = sub(num_a, num_b)
    return sum

@app.get("/mult/<int:num_a>/<int::num_b>")
def get_num(a, b):
    num_a = request.args.get("a")
    num_b = request.args.get("b")
    sum = mult(num_a, num_b)
    return sum

@app.get("/div/<int:num_a>/<int::num_b>")
def get_num(a, b):
    num_a = request.args.get("a")
    num_b = request.args.get("b")
    sum = div(num_a, num_b)
    return sum

