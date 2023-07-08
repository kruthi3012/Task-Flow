import json
from flask import Flask
from flask import *
from flask import request, jsonify
import datetime
from flask_cors import CORS, cross_origin
import csv
import pandas as pd


app = Flask(__name__)
cors = CORS(app)


@app.route('/', methods = ['GET'])
def home():
  return json.dumps({'message': 'This is the Flask API setup'})

@app.route('/authenticate/', methods = ['POST'])
def authenticate():
  data = request.json
  email = data['email']
  password = data['password']
  
  res={}
  try:
    df = pd.read_csv("auth.csv")
    print(df)
    try:
      val = df[df['email'] == email].values
      print(val)
      
      if(len(val)!=0):
        val = val[0]
        if(password ==str(val[2])):
          res['message'] = "Authenticated"
          res['name'] = val[0]
          res['status'] = 1
      else:
        res['message'] = "User not found" 
        res['status'] = 3
        
    except Exception as e:
      print("Error: ", e)
      
  except Exception as e:
    print("No file named auth.csv; ", e)
    res['message'] = "No file named auth.csv"
    res['status'] = 4
    
  return json.dumps(res)
    
  
             
        
        
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=4000)
        
# app.run(host="0.0.0.0", port=4000)