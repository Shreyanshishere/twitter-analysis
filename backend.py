from cgitb import text
import pickle
model=pickle.load(open("model.pkl",'rb'))
cvt=pickle.load(open("cvt.pkl",'rb'))
def predict(string):
    
    string=cvt.transform([string])
    return model.predict(string)  
