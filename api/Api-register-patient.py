from flask import Flask, request, jsonify

app = Flask(__name__)

patients = [
    {
        '_id_patient': 1,
        '_name': 'John Doe',
        '_gender': 'Male',
        '_arrival_date': '2022-03-14 10:30:00',
        '_priority': 1,
        '_state': 'waiting'
    },
    {
        '_id_patient': 2,
        '_name': 'Jane Doe',
        '_gender': 'Female',
        '_arrival_date': '2022-03-15 08:45:00',
        '_priority': 2,
        '_state': 'waiting'
    }
]


@app.route('/get-patient/int:patient_id', methods=['GET'])
def get_patient(patient_id):
    
    # Finds the patient in the list of patients
    patient = next((p for p in patients if p['_id_patient'] == patient_id), None)
    
    # If the patient is not found, returns an error message
    if not patient:
        return jsonify({'message': 'Patient not found'}), 404
    
    # Returns the patient in JSON format
    return jsonify(patient), 200


    
@app.route('/add-patient', methods=['POST'])
def add_patient():
    
    # Gets patient data from the request
    patient_data = request.get_json()
    
    # Creates a new patient with an ID, name, gender, arrival date, priority, and state
    patient = {
        '_id_patient': len(patients) + 1,
        '_name': patient_data['_name'],
        '_gender': patient_data['_gender'],
        '_arrival_date': patient_data['_arrival_date'],
        '_priority': patient_data['_priority'],
        '_state': 'waiting'
    }
    
    # Adds the new patient to the list of patients
    patients.append(patient)
    
    # Returns the new patient in JSON format
    return jsonify({
        '_id_patient': patient['_id_patient'],
        '_name': patient['_name'],
        '_gender': patient['_gender'],
        '_arrival_date': patient['_arrival_date'],
        '_priority': patient['_priority'],
        '_state': patient['_state']
    }), 201     
    
    
    
@app.route('/get-most-urgent-patient', methods=['GET'])
def get_most_urgent_patient():
# Initializes the most urgent patient as none
    most_urgent_patient = None
    # Loops through the list of patients
    for patient in patients:
        # If the patient is waiting
        if patient['_state'] == 'waiting':
            # If the patient is more urgent than the current most urgent patient, update the most urgent patient
            if most_urgent_patient is None or patient['_priority'] > most_urgent_patient['_priority']:
                most_urgent_patient = patient
                
    # If there is no most urgent patient, return an error message
    if most_urgent_patient is None:
        return jsonify({'message': 'No patient found in the waiting list'}), 404
    
    # Change the state of the most urgent patient to 'in consultation'
    most_urgent_patient['_state'] = 'in consultation'
    
    # Returns the most urgent patient in JSON format
    return jsonify({
        '_id_patient': most_urgent_patient['_id_patient'],
        '_name': most_urgent_patient['_name'],
        '_gender': most_urgent_patient['_gender'],
        '_arrival_date': most_urgent_patient['_arrival_date'],
        '_priority': most_urgent_patient['_priority']
    }), 200    



@app.route('/update-patient/int:patient_id', methods=['PUT'])
def update_patient(patient_id):
    
    # Search for the patient by ID in the list of patients
    patient = next((p for p in patients if p['_id_patient'] == patient_id), None)
    
    # If the patient is not found, return an error message and status code 404
    if not patient:
        return jsonify({'message': 'Patient not found'}), 404
    
    # Get the updated patient data from the request JSON
    data = request.get_json()
    # Update the patient's state if included in the request JSON, or keep the existing state
    patient['_state'] = data.get('_state', patient['_state'])
    # Update the patient's priority if included in the request JSON, or keep the existing priority
    patient['_priority'] = data.get('_priority', patient['_priority'])

    # Return the updated patient information with status code 200
    return jsonify(patient), 200



@app.route('/delete-patient/int:id', methods=['DELETE'])
def delete_patient(id):
    
    # Iterate through the list of patients and check if any of them have the given ID
    for patient in patients:
        if patient['_id_patient'] == id:
            
        # If a patient with the given ID is found, remove it from the list and return a success message
            patients.remove(patient)
            return jsonify({'message': f'Patient with ID {id} has been deleted'}), 200
        
    # If no patient with the given ID is found, return an error message
    return jsonify({'message': 'Patient not found'}), 404