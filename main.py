from patientsdirectory.PatientsManager import PatientsManager as pt_manager
from patientsdirectory.Patient import Patient as pt
from patientsdirectory.PatientState import PatientState as pt_state

from doctorsdirectory.Doctor import Doctor as dt
from doctorsdirectory.DoctorsManager import DoctorsManager as dt_manager
import time
from datetime import datetime



def fake_activity():
    patient = pt("test", 19, "M", 4, pt_state.Awaiting, datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
    pt_manager.create_patient(patient)

    time.sleep(2)

    patient2 = pt("gabite", 19, "M", 5, pt_state.Awaiting, datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
    pt_manager.create_patient(patient2)

    time.sleep(2)

    patient3 = pt("emiliana", 19, "M", 3, pt_state.Awaiting, datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
    pt_manager.create_patient(patient3)

    time.sleep(2)

    patient4 = pt("ttcion", 19, "M", 5, pt_state.Awaiting, datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
    pt_manager.create_patient(patient4)

    for patient in pt_manager.read_patient():
        print(patient._name, patient._priority)

    time.sleep(2)

    pt_manager.update_patient(2, "_state", pt_state.Consulted)

    for patient in pt_manager.read_patient():
        print(patient._name, patient._priority)

    time.sleep(2)

    doc = dt("robert", "Uretrologue")
    dt_manager.add_doctor(doc)

    time.sleep(2)

    doc2 = dt("Mr Seguret", "biologie")
    dt_manager.add_doctor(doc2)

def main():
    fake_activity()

if __name__ == '__main__':
    main()