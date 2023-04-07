import patientsdirectory.PatientsManager as pdm
import patientsdirectory.Patient as pt
import patientsdirectory.PatientState as pstate
def main():
    p_d_m = pdm.PatientsManager()
    patient = pt.Patient("test",19,"M",4,"19/05/21")
    patient2 = pt.Patient("gabite",19,"M",5,"18/05/21")
    patient3 = pt.Patient("emiliana",19,"M",3,"19/05/21")
    patient4 = pt.Patient("ttcion",19,"M",5,"19/05/21")
    p_d_m.create_patient(patient)
    p_d_m.create_patient(patient2)
    p_d_m.create_patient(patient3)
    p_d_m.create_patient(patient4)
    t = p_d_m.read_patient()
    for x in t:
        print(x._name,x._priority)
    p_d_m.update_patient(2,"_state",pstate.PatientState.Consulted)
    s = p_d_m.read_patient()
    for z in s:
        print(z._name,z._priority)

if __name__ == '__main__':
    main()