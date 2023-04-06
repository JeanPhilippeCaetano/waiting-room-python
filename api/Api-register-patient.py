from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///patients.db'
db = SQLAlchemy(app)


class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    gender = db.Column(db.String(10))
    condition = db.Column(db.String(100))
    priority = db.Column(db.Integer)
    status = db.Column(db.String(20), default='waiting')
    

@app.route('/register-patient', methods=['POST'])
def register_patient():
    patient_data = request.get_json()
    patient = Patient(name=patient_data['name'], gender=patient_data['gender'],
                      condition=patient_data['condition'], priority=patient_data['priority'])
    db.session.add(patient)
    db.session.commit()
    return 'Patient registered successfully'


@app.route('/get-next-patient', methods=['GET'])
def get_next_patient():
    next_patient = Patient.query.filter_by(status='waiting').order_by(Patient.priority.desc()).first()
    if not next_patient:
        return jsonify({'message': 'No patient found in the waiting list'}), 404
    
    next_patient.status = 'in consultation'
    db.session.commit()
    
    return jsonify({
        'id': next_patient.id,
        'name': next_patient.name,
        'gender': next_patient.gender,
        'condition': next_patient.condition,
        'priority': next_patient.priority
    }), 200
    
@app.route('/refer-patient', methods=['POST'])
def refer_patient():
    patient_data = request.get_json()
    patient_id = patient_data['id']
    new_specialist = patient_data['specialist']
    patient = Patient.query.get(patient_id)
    if not patient:
        return jsonify({'message': 'Patient not found'}), 404
    patient.specialist = new_specialist
    db.session.commit()
    return jsonify({'message': 'Patient referred successfully'}), 200

@app.route('/finish-patient-cycle', methods=['POST'])
def finish_patient_cycle():
    patient_data = request.get_json()
    patient_id = patient_data['id']
    patient = Patient.query.get(patient_id)
    if not patient:
        return jsonify({'message': 'Patient not found'}), 404
    patient.status = 'finished'
    db.session.commit()
    return jsonify({'message': 'Patient cycle finished successfully'}), 200