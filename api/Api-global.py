from flask import Flask, request, jsonify

from patientsdirectory.Patient import Patient
from patientsdirectory.PatientsManager import PatientsManager as pm
from patientsdirectory.PatientState import PatientState as pstate
from doctorsdirectory.Doctor import Doctor
from doctorsdirectory.DoctorsManager import DoctorsManager

app = Flask(__name__)

@app.route('/add-doctor', methods=['POST'])
def add_doctor():
    # Récupère les données du docteur à partir de la requête
    doctor_data = request.get_json()

    # Crée un nouveau docteur avec un ID, un nom, une spécialité et une date d'embauche
    doctor = Doctor(doctor_data['name'], doctor_data['specialty'])

    # Ajoute le nouveau docteur à la liste des docteurs
    DoctorsManager.add_doctor(doctor)

    # Renvoie le nouveau docteur au format JSON
    return jsonify("Status : Done"), 201



@app.route('/get-patient/<int:patient_id>', methods=['GET'])
def get_patient(patient_id):
    # Finds the patient in the list of patients
    patient = pm.read_patient("_id",patient_id)[0]
    # If the patient is not found, returns an error message
    if patient is None:
        return jsonify({'message': 'Patient not found'}), 40
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

    data = request.get_json()
    DoctorsManager.update_busy_by_id(data['doctor_id'])
    pm.update_doctor_with(most_urgent_patient._id, data['doctor_id'])

    # Returns the most urgent patient in JSON format
    return jsonify({
        '_id_patient': most_urgent_patient._id,
        '_name': most_urgent_patient._name,
        '_age': most_urgent_patient._age,
        '_gender': most_urgent_patient._gender,
        '_arrival_date': most_urgent_patient._arrival_date,
        '_state': most_urgent_patient._state.value,
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
                #DoctorsManager.update_busy_by_id(patient.current_doctor_id)
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
