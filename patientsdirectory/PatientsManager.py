import patientsdirectory.PatientState as pstate

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
        return [patient for patient in patients_sorted if patient._state is pstate.PatientState.Awaiting]

    @classmethod
    def update_patient(self, patient_id, attribute_type=None, attribute_value=None):
        if attribute_type is not None and attribute_value is not None:
            setattr(self._patients[patient_id], attribute_type, attribute_value)
            if getattr(self._patients[patient_id], attribute_type) == pstate.PatientState.Consulted:
                for patient in self._patients:
                    if patient_id is not patient._id:
                        patient._priority += 1

    @classmethod
    def delete_patient(self, patient_id):
        self._patients.pop(patient_id)

