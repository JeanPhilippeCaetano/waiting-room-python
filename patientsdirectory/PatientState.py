from enum import Enum


class PatientState(Enum):
    Awaiting = "Awaiting"
    InConsultation = "In Consultation"
    Consulted = "Consulted"
