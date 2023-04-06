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

@app.route('/get-patient/<int:patient_id>', methods=['GET'])
def get_patient(patient_id):
    patient = next((p for p in patients if p['_id_patient'] == patient_id), None)
    if not patient:
        return jsonify({'message': 'Patient not found'}), 404
    
    return jsonify(patient), 200


@app.route('/add-patient', methods=['POST'])
def add_patient():
    patient_data = request.get_json()
    patient = {
        '_id_patient': len(patients) + 1,
        '_name': patient_data['_name'],
        '_gender': patient_data['_gender'],
        '_arrival_date': patient_data['_arrival_date'],
        '_priority': patient_data['_priority'],
        '_state': 'waiting'
    }
    patients.append(patient)
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
    most_urgent_patient = None
    for patient in patients:
        if patient['_state'] == 'waiting':
            if most_urgent_patient is None or patient['_priority'] > most_urgent_patient['_priority']:
                most_urgent_patient = patient

    if most_urgent_patient is None:
        return jsonify({'message': 'No patient found in the waiting list'}), 404
    
    most_urgent_patient['_state'] = 'in consultation'
    
    return jsonify({
        '_id_patient': most_urgent_patient['_id_patient'],
        '_name': most_urgent_patient['_name'],
        '_gender': most_urgent_patient['_gender'],
        '_arrival_date': most_urgent_patient['_arrival_date'],
        '_priority': most_urgent_patient['_priority']
    }), 200

@app.route('/update-patient/<int:patient_id>', methods=['PUT'])
def update_patient(patient_id):
    patient = next((p for p in patients if p['_id_patient'] == patient_id), None)
    if not patient:
        return jsonify({'message': 'Patient not found'}), 404

    data = request.get_json()
    patient['_state'] = data.get('_state', patient['_state'])
    patient['_priority'] = data.get('_priority', patient['_priority'])

    return jsonify(patient), 200
    
@app.route('/delete-patient/<int:id>', methods=['DELETE'])
def delete_patient(id):
    for patient in patients:
        if patient['_id_patient'] == id:
            patients.remove(patient)
            return jsonify({'message': f'Patient with ID {id} has been deleted'}), 200
    
    return jsonify({'message': 'Patient not found'}), 404