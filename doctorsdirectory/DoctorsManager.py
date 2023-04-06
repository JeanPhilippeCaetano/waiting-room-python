class DoctorsManager:
    _list = None

    @classmethod
    def get_doctors(cls, speciality=None):
        if cls._list is None:
            cls._list = []

        return cls._list if speciality is not None else [doc for doc in cls._list if doc.speciality == speciality]

    @classmethod
    def add_doctor(cls, doctor):
        cls._list.append(doctor)

    @classmethod
    def update_busy(cls, doc_id):
        next((doc for doc in cls._list if doc.get_id == doc_id), None)


