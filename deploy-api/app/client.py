import requests

def get_loan_prediction(age, gender, experience, income, family, ccavg, education, mortgage, home_ownership):
    url = "http://100.26.211.76:80/predict"  # URL to the FastAPI endpoint
    # 100.26.211.76
    # Create the payload
    payload = {
        "Age": age,
        "Gender": gender,
        "Experience": experience,
        "Income": income,
        "Family": family,
        "CCAvg": ccavg,
        "Education": education,
        "Mortgage": mortgage,
        "HomeOwnership": home_ownership
    }
    
    # Send a POST request to the API
    response = requests.post(url, json=payload)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Print the prediction result
        print("Prediction:", response.json()['prediction'])
    else:
        print("Failed to get a response:", response.status_code)

if __name__ == "__main__":
    # Pass the parameters to the function
    get_loan_prediction(
        age=30,
        gender="M",
        experience=5,
        income=6,
        family=3,
        ccavg=2.5,
        education="a",
        mortgage=0,
        home_ownership="Rent"
    )
