"""
Lancement depuis la racine du projet:
> python -m flask --app api/app.py run

Test:
> curl location --request GET 'localhost:5000/nearest_cars' --header 'Content-Type: application/json' --data-raw '{"lon": 4.82977, "lat": 45.75487}'

"""
from flask import Flask, request

app = Flask(__name__)

# This URL to test that your app is running
# On a navigator: http://localhost:5000/
@app.route("/")
def menu():
    """
    This function display the monitor
    """
    return dict(message="Menu")


# Main URL to get prediction
@app.route("/get-patient", methods=['POST'])
def getPatient():
    """
    Exécute la fonction qui get le dossier d'un patient
    """
    # do the job here
    patient = {
        "Name": "Emile",
        "Gender": "Male" ,
        "Priority": 12,
        "State": "awaiting",
        "arrival_date": "12pm"
    }
    return patient

@app.route("/get-most-urgent-patient", methods=['POST'])
def getNumber1():
    """
    Exécute la fonction qui get le dossier d'un patient
    """
    # do the job here
    patient = {
        "Name": "Emile",
        "Gender": "Male" ,
        "Priority": 120921,
        "State": "awaiting",
        "arrival_date": "12pm"
    }
    return patient


