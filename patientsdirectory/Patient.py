import itertools
import patientsdirectory.PatientState as pstate
class Patient:
    _id_iter = itertools.count()
    def __init__(self, name, age, gender, priority, arrival_date):
        self._id = next(Patient._id_iter)
        self._name = name
        self._age = age
        self._gender = gender
        self._priority = priority
        self._state = pstate.PatientState.Awaiting
        self._arrival_date = arrival_date