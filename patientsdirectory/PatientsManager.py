from copy import copy


class PatientsManager:
    _patients = []

    @classmethod
    def create_patient(self, patient):
        self._patients.append(patient)

    @classmethod
    def read_patient(self, attribute_type=None, attribute_value=None):
        patients_copy = self._patients.copy()
        patients_sorted = sorted(patients_copy, key=(lambda b: b._priority), reverse=True)
        if attribute_type is not None and attribute_value is not None:
            return [patient for patient in patients_sorted if getattr(patient, attribute_type) == attribute_value]
        return patients_sorted

    @classmethod
    def update_patient(self, patient_id, attribute_type=None, attribute_value=None):
        if attribute_type is not None and attribute_value is not None:
            setattr(self._patients[patient_id], attribute_type, attribute_value)

    @classmethod
    def delete_patient(self, patient_id):
        self._patients.pop(patient_id)
