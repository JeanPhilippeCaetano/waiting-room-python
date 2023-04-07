import itertools
import logging

logging.basicConfig(filename="logfilehospital.log", level=logging.DEBUG)

class Doctor:
    _id_iter = itertools.count()

    def __init__(self, name, speciality):
        self._name = name
        self._id = next(Doctor._id_iter)
        self._is_busy = False
        self._speciality = speciality
        logging.info("---------------------- \nDoctor created in register:\nid: " + str(
            self._id) + "\nname: " + self._name + "\nis busy: " + str(self._is_busy) + "\nspeciality: " + \
                     self.get_speciality() + "\n-------------------------")

    def __str__(self):
        return "id: " + str(
            self._id) + "\nname: " + self._name + "\nis busy: " + str(
            self._is_busy) + "\nspeciality: " + self.get_speciality() + "\n"

    def update_busy(self):
        self._is_busy = not self._is_busy

    def get_id(self):
        return self._id

    def get_speciality(self):
        return self._speciality