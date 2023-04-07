from flask import Flask, request, jsonify

from patientsdirectory.Patient import Patient
from patientsdirectory.PatientsManager import PatientsManager as pm
from patientsdirectory.PatientState import PatientState as pstate
app = Flask(__name__)

@app.route('/get-patient/<int:patient_id>', methods=['GET'])
def get_patient(patient_id):
    # Finds the patient in the list of patients
    patient = pm.read_patient("_id",patient_id)[0]
    # If the patient is not found, returns an error message
    if patient is None:
        return jsonify({'message': 'Patient not found'}), 404
    # Returns the patient in JSON format
    return jsonify({
        "name":patient._name,
        "age":patient._age,
        "gender":patient._gender,
        "priority":patient._priority,
        "state":patient._state.value,
        "arrival_date":patient._arrival_date
    }), 200


@app.route('/add-patient', methods=['POST'])
def add_patient():
    # Gets patient data from the request
    patient_data = request.get_json()

    # Creates a new patient with an ID, name, gender, arrival date, priority, and state
    patient = Patient(
        patient_data['name'],
        patient_data['age'],
        patient_data['gender'],
        patient_data['priority'],
        patient_data['arrival_date']
    )

    pm.create_patient(patient)
    # Returns the new patient in JSON format
    return jsonify("Status : Done"), 201


@app.route('/get-most-urgent-patient', methods=['GET'])
def get_most_urgent_patient():
    # Initializes the most urgent patient as none
    most_urgent_patient = pm.read_patient()[0]
    # If there is no most urgent patient, return an error message
    if most_urgent_patient is None:
        return jsonify({'message': 'No patient found in the waiting list'}), 404

    # Change the state of the most urgent patient to 'in consultation'
    pm.update_patient(most_urgent_patient._id, "_state", pstate.InConsultation)

    # Returns the most urgent patient in JSON format
    return jsonify({
        '_id_patient': most_urgent_patient._id,
        '_name': most_urgent_patient._name,
        '_age': most_urgent_patient._age,
        '_gender': most_urgent_patient._gender,
        '_arrival_date': most_urgent_patient._arrival_date,
        '_state': pstate.InConsultation.value,
        '_priority': most_urgent_patient._priority
    }), 200


@app.route('/update-patient/<int:patient_id>', methods=['PUT'])
def update_patient(patient_id):
    # Search for the patient by ID in the list of patients
    patient = pm.read_patient("_id",patient_id)[0]
    # If the patient is not found, return an error message and status code 404
    if not patient:
        return jsonify({'message': 'Patient not found'}), 404

    # Get the updated patient data from the request JSON
    data = request.get_json()
    for key in data.keys():
        if key == "_state":
            if data[key] == "Consulted":
                pm.update_patient(patient_id, "_state", pstate.Consulted)
        pm.update_patient(patient_id, key, data[key])
        setattr(patient, key, data[key])
    # Return the updated patient information with status code 200
    return jsonify("Status : Done"), 200


@app.route('/delete-patient/<int:id>', methods=['DELETE'])
def delete_patient(id):
    # Iterate through the list of patients and check if any of them have the given ID
    patient = pm.read_patient("_id", id)[0]
    # If no patient with the given ID is found, return an error message
    if patient is None:
        return jsonify({'message': 'Patient not found'}), 404

    pm.delete_patient(id)
    return jsonify({'message': f'Patient with ID {id} has been deleted'}), 200
