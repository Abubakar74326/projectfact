#from typing import Optional
#from fastapi import FastAPI

from flask import Flask
import factorial

app = Flask(__name__)

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.route('/factorial/<int:num>/')
def read_item(num: int):
    fact = factorial.factorial(num)
    return {"factorial": fact}

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8081, debug=True)