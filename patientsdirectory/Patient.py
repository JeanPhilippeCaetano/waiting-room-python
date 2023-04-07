import itertools
from patientsdirectory.PatientState import PatientState

class Patient:
    _id_iter = itertools.count()
    def __init__(self, name, age, gender, priority, state, arrival_date):
        self._id = next(Patient._id_iter)
        self._name = name
        self._age = age
        self._gender = gender
        self._priority = priority
        self._state = state
        self._arrival_date = arrival_date

    def __str__(self):
        return (
            "\nPriority: " + str(self._priority) +
            "\nName: " + self._name +
            "\nGender: " + str(self._gender) +
            "\nState: " + str(PatientState(self._state).name) +
            "\nArrival Date: " + self._arrival_date
            )