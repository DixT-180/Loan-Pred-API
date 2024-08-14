import requests
from flask import Flask, request, render_template, redirect, url_for

application = Flask(__name__)
app = application

# Route for the home page
@app.route('/')
def index():
    return render_template('index.html')

# Route for the prediction page
@app.route('/data_inlet', methods=['GET', 'POST'])
def data_inlet():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        # Collecting form data
        data = {
            "Age": request.form.get('Age'),
            "Gender": request.form.get('Gender'),
            "Experience": request.form.get('Experience'),
            "Income": request.form.get('Income'),
            "Family": request.form.get('Family'),
            "CCAvg": request.form.get('CCAvg'),
            "Education": request.form.get('Education'),
            "Mortgage": request.form.get('Mortgage'),
            "HomeOwnership": request.form.get('HomeOwnership')
        }

        # API URL
        url = "http://100.26.211.76:80/predict"
        
        # Sending data to FastAPI endpoint
        response = requests.post(url, json=data)
        if response.status_code == 200:
        # Print the prediction result
            print("Prediction:", response.json()['prediction'])
            return render_template('index.html', results=response.json()['prediction'])
        else:
            print("Failed to get a response:", response.status_code)

# Running the Flask app
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
