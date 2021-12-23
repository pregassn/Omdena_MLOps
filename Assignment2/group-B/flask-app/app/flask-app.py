"""
Spyder Editor

This is a script file for getting request from flask, evaluate, and return result.
"""
from BMICalculation import BMICompute
from flask import Flask, jsonify, request

#instantiate flask object
app = Flask('__name__')

@app.route('/', methods=['GET', 'POST'])
def get_input():
    packet = request.get_json(force=True)
    weight = packet['weight']
    height = packet['height']
    bmi = BMICompute(weight, height)
    return jsonify(packet, bmi)

#driver function
if __name__ == '__main__':
    app.run()