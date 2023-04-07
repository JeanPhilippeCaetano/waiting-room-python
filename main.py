from patientsdirectory.PatientsManager import PatientsManager
from patientsdirectory.Patient import Patient
from patientsdirectory.PatientState import PatientState

from doctorsdirectory.Doctor import Doctor
from doctorsdirectory.DoctorsManager import DoctorsManager
import time
from datetime import datetime


def fake_activity():
    patient = Patient("Emile", 19, "M", 4, datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
    PatientsManager.create_patient(patient)

    time.sleep(2)

    patient2 = Patient("Gabby", 19, "M", 5, datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
    PatientsManager.create_patient(patient2)

    time.sleep(2)

    patient3 = Patient("JP", 19, "M", 3, datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
    PatientsManager.create_patient(patient3)

    time.sleep(2)

    patient4 = Patient("Wassim", 19, "M", 5, datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
    PatientsManager.create_patient(patient4)

    for patient in PatientsManager.read_patient():
        print(patient._name, patient._priority)

    time.sleep(2)

    PatientsManager.update_patient(2, "_state", PatientState.Consulted)

    for patient in PatientsManager.read_patient():
        print(patient._name, patient._priority)

    time.sleep(2)

    doc = Doctor("Robert", "Ophtalmologue")
    DoctorsManager.add_doctor(doc)

    time.sleep(2)

    doc2 = Doctor("Mr Seguret", "biologie")
    DoctorsManager.add_doctor(doc2)


def main():
    fake_activity()


if __name__ == '__main__':
    main()