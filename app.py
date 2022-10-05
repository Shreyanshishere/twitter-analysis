import numpy as np
from flask import Flask , render_template, request
from backend import *
lis=['non hate tweet','hate tweet']
app=Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')
    
@app.route("/predict1",methods=['POST'])
def predict1():
    st=request.form['tweet']
    res=predict(st)[0]
    # return f"your result is the "+str(lis[res]) 
    res= "your tweet is analyzed as a "+str(lis[res])
    return render_template('index.html',result=res)
if __name__=="__main__":
    app.run(debug=True)
