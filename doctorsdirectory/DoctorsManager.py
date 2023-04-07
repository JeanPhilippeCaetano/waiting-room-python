import logging
import datetime as dt

logging.basicConfig(filename="logfilehospital.log", level=logging.DEBUG)

now = dt.datetime.now()
# Convert the datetime.datetime object to a string in the format 'YYYY-MM-DD HH:MM:SS'
date_string = now.strftime('%Y-%m-%d %H:%M:%S')

class DoctorsManager:
    _list = []

    @classmethod
    def get_doctors(cls, speciality=None):
        #        if cls._list is None:
        #            cls._list = []
        return cls._list if speciality is None else [doc for doc in cls._list if doc.get_speciality() == speciality]

    @classmethod
    def add_doctor(cls, doctor):
        cls._list.append(doctor)
        logging.info("\nDoctor created in register:" + date_string + \
                     doctor.__str__() + \
                     "\n-------------------------\n")

    @classmethod
    def update_busy_by_id(cls, doc_id):
        for doctor in cls._list:
            if doctor.get_id() == doc_id:
                doctor.update_busy()
                logging.info("\nDoctor changed state:" + date_string + \
                             "\nName: " + doctor._name + \
                             "\nIs busy: " + doctor._is_busy + \
                             "\n-------------------------\n")
                break