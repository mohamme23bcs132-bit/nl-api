from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import joblib
import numpy as np

model=joblib.load("model.joblib")   

class_names = ['setosa', 'versicolor', 'virginica'] 
app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

@app.get("/")
def read_root():
    return {'message':'Iris model API'}

@app.post('/predict')
def predict(data:dict):
    features=np.array(data['features']).reshape(1,-1)
    prediction=model.predict(features)[0]
    class_name=class_names[prediction]
    return {'prediction':class_name}
