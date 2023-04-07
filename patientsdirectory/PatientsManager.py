from patientsdirectory.PatientState import PatientState
import datetime as dt
import logging

logging.basicConfig(filename="logfilehospital.log", level=logging.DEBUG)

now = dt.datetime.now()
# Convert the datetime.datetime object to a string in the format 'YYYY-MM-DD HH:MM:SS'
date_string = now.strftime('%Y-%m-%d %H:%M:%S')


class PatientsManager:
    _patients = []

    @classmethod
    def create_patient(self, patient):
        self._patients.append(patient)
        logging.info("\nPATIENT CREATED IN REGISTER: " + date_string + \
                     patient.__str__() + \
                     "\n-------------------------\n")

    @classmethod
    def read_patient(cls, attribute_type=None, attribute_value=None):
        patients_copy = cls._patients.copy()
        patients_sorted = sorted(patients_copy, key=(lambda b: b._priority), reverse=True)
        if attribute_type is not None and attribute_value is not None:
            return [patient for patient in patients_sorted if getattr(patient, attribute_type) == attribute_value]
        return [patient for patient in patients_sorted if patient._state is PatientState.Awaiting]

    @classmethod
    def update_patient(cls, patient_id, attribute_type=None, attribute_value=None):
        if attribute_type is not None and attribute_value is not None:
            setattr(cls._patients[patient_id], attribute_type, attribute_value)
            if getattr(cls._patients[patient_id], attribute_type) == PatientState.Consulted:
                for patient in cls._patients:
                    if patient_id is not patient._id:
                        old_priority = patient._priority
                        patient._priority += 1
                        logging.info("\nPATIENT PRIORITY CHANGED: " + date_string + \
                                     "\nName: " + patient._name + \
                                     "\nOld priority: " + str(old_priority) + \
                                     "\nPriority: " + str(patient._priority) + \
                                     "\n-------------------------\n")

    @classmethod
    def update_doctor_with(cls,patient_id, doc_id):
        for patient in cls._patients:
            if patient._id == patient_id:
                patient.current_doctor_id = doc_id


    @classmethod
    def delete_patient(self, patient_id):
        patient = self.read_patient("_id", patient_id)
        self._patients.pop(patient_id)
        logging.info("\nPATIENT DELETED: " + date_string + \
                     "\nName: " + patient._name + \
                     "\nPriority: " + str(patient._priority) + \
                     "\n-------------------------\n")
