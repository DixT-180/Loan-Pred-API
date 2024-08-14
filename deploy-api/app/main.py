import uvicorn
from fastapi import FastAPI
import pickle
import pandas as pd
from pydantic import BaseModel

# Create the app object
app = FastAPI()

# Load the model and preprocessor
model_path = "app/model.pkl"
preprocessor_path = "app/preprocessor.pkl"

with open(model_path, 'rb') as file:
    predictor = pickle.load(file)

with open(preprocessor_path, 'rb') as file:
    preprocessor = pickle.load(file)

# Define the Pydantic model for input data
class Loan(BaseModel):
    Age: int
    Gender: str
    Experience: int
    Income: float
    Family: int
    CCAvg: float 
    Education: str
    Mortgage: int
    HomeOwnership: str

@app.get('/')
def index():
    return {'message': 'Hello, World'}

@app.post('/predict')
def predict_loan(data: Loan):
    print(data,'data')
    print(data.dict(),'data.dict()')
    # Convert the incoming data into a DataFrame
    data_df = pd.DataFrame([data.dict()])
    
    # Apply the preprocessor
    data_scaled = preprocessor.transform(data_df)
    
    # Make the prediction
    prediction = predictor.predict(data_scaled)
    
    # Map the prediction to a readable format
    if prediction == 1:
        prediction_text = "LOAN ACCEPT"
    else:
        prediction_text = "NOT ACCEPT"
    
    return {'prediction': prediction_text}

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
