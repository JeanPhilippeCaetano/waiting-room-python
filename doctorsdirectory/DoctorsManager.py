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

    @classmethod
    def update_busy_by_id(cls, doc_id):
        for doctor in cls._list:
            if doctor.get_id() == doc_id:
                doctor.update_busy()
                print(f"Doctor with id {doc_id} found.")
                print(f"Before update: {doctor._is_busy}")
                break

