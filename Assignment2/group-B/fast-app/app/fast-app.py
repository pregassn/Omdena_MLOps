"""
Spyder Editor

This is a script file for getting request from fast api, evaluate, and return result.
"""
from BMICalculation import BMICompute
import uvicorn
from fastapi import FastAPI, Request

#instantiate flask object
app = FastAPI()

@app.get('/')
async def get_input(request:Request):
    packet = await request.json()
    weight = packet['weight']
    height = packet['height']
    bmi = BMICompute(weight, height)
    return bmi

#driver function
if __name__ == '__main__':
    uvicorn.run()