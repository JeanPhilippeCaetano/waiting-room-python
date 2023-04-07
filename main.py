from patientsdirectory.PatientsManager import PatientsManager
from patientsdirectory.Patient import Patient
from patientsdirectory.PatientState import PatientState
from doctorsdirectory.Doctor import Doctor
import time
from datetime import datetime



def fake_activity():
    patient = Patient("test", 19, "M", 4, PatientState.Awaiting, datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
    PatientsManager.create_patient(patient)

    time.sleep(2)

    patient2 = Patient("gabite", 19, "M", 5, PatientState.Awaiting, datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
    PatientsManager.create_patient(patient2)

    time.sleep(2)

    patient3 = Patient("emiliana", 19, "M", 3, PatientState.Awaiting, datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
    PatientsManager.create_patient(patient3)

    time.sleep(2)

    patient4 = Patient("ttcion", 19, "M", 5, PatientState.Awaiting, datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
    PatientsManager.create_patient(patient4)

    for patient in PatientsManager.read_patient():
        print(patient._name, patient._priority)

    time.sleep(2)

    PatientsManager.update_patient(2, "_state", PatientState.Consulted)

    for patient in PatientsManager.read_patient():
        print(patient._name, patient._priority)

    time.sleep(2)

    doc = Doctor("robert", "Uretrologue")

    time.sleep(2)

    doc2 = Doctor("Mr Seguret", "biologie")

def main():
    fake_activity()

if __name__ == '__main__':
    main()