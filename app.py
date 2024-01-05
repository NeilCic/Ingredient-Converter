from flask import Flask
from flask import request

from business_logic import bl_convert, bl_calculate, bl_pinches

app = Flask(__name__)


@app.route("/convert", methods=['POST'])
def q1a():
    """
    Your task is to write a service with two endpoints that receives as a parameter a serving
    amount, serving unit to convert from and the serving unit to convert to.
    Upon startup the service should load the conversion table from a provided input file to the
    services cache
    """
    return bl_convert(request.get_json())
    

@app.route("/calculate", methods=['POST'])
def q1b():
    """
    Calculate sugar amount.
    convert a specific item to the correct number of cups, and then receive how many grams of sugar it has. You can find the converting methods at the file sugar_calculation.json attached
    """
    return bl_calculate(request.get_json())


@app.route("/pinches", methods=['POST'])
def q2():
    """
    Create an endpoint that receives the number of pinch (and only pinch), and another serving amount,
    This endpoint should return the exact number of pinch that are in the serving amount.
    Use the first question functions that you implemented.
    :return: exact number of pinch that are in the serving amount (float)
    """
    return bl_pinches(request.get_json())


@app.route("/", methods=['GET'])
def homepage():
    return "Hello World!"
