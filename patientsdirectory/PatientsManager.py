from copy import copy

import Patient

class PatientsManager:
    def __init__(self):
        self._patients = []

    def create_patient(self, patient):
        self._patients.append(patient)

    def read_patient(self, attribute_type=None, attribute_value=None):
        patients_sorted = sorted(copy(self._patients),"priority",reverse=True)
        if attribute_type is not None and attribute_value is not None:
            return [patient for patient in patients_sorted if patient[attribute_type] == attribute_value]
        return patients_sorted

    def update_patient(self, patient_id, attribute_type=None, attribute_value=None):
        if attribute_type is not None and attribute_value is not None:
            self._patients[patient_id][attribute_type] = attribute_value

    def delete_patient(self, patient_id):
        self._patients.pop(patient_id)

    