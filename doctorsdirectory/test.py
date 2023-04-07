import unittest
from Doctor import Doctor
from DoctorsManager import DoctorsManager


class TestDoctor(unittest.TestCase):
    def test_init(self):
        doctor = Doctor("John Doe", "Pediatrics")
        self.assertEqual(doctor._name, "John Doe")
        self.assertEqual(doctor._speciality, "Pediatrics")
        self.assertFalse(doctor._is_busy)

    def test_update_busy(self):
        doctor = Doctor("John Doe", "Pediatrics")
        doctor.update_busy()
        self.assertTrue(doctor._is_busy)
        doctor.update_busy()
        self.assertFalse(doctor._is_busy)

    def test_get_id(self):
        doctor1 = Doctor("John Doe", "Pediatrics")
        doctor2 = Doctor("Jane Smith", "Cardiology")
        self.assertEqual(doctor1.get_id(), 0)
        self.assertEqual(doctor2.get_id(), 1)


class TestDoctorsManager(unittest.TestCase):
    def setUp(self):
        DoctorsManager._list = []

    def test_get_doctors(self):
        doctor1 = Doctor("John Doe", "Pediatrics")
        doctor2 = Doctor("Jane Smith", "Cardiology")
        DoctorsManager.add_doctor(doctor1)
        DoctorsManager.add_doctor(doctor2)

        # Test with no speciality specified
        doctors = DoctorsManager.get_doctors()
        self.assertEqual(len(doctors), 2)
        self.assertIn(doctor1, doctors)
        self.assertIn(doctor2, doctors)

        # Test with "Pediatrics" speciality specified
        doctors = DoctorsManager.get_doctors(speciality="Pediatrics")
        self.assertEqual(len(doctors), 1)
        self.assertIn(doctor1, doctors)
        self.assertNotIn(doctor2, doctors)

        # Test with "Cardiology" speciality specified
        doctors = DoctorsManager.get_doctors(speciality="Cardiology")
        self.assertEqual(len(doctors), 1)
        self.assertNotIn(doctor1, doctors)
        self.assertIn(doctor2, doctors)

    def test_add_doctor(self):
        doctor = Doctor("John Doe", "Pediatrics")
        DoctorsManager.add_doctor(doctor)
        self.assertIn(doctor, DoctorsManager._list)

    def test_update_busy(self):
        doctor1 = Doctor("John Doe", "Pediatrics")
        doctor2 = Doctor("Jane Smith", "Cardiology")
        DoctorsManager.add_doctor(doctor1)
        DoctorsManager.add_doctor(doctor2)

        # Test updating a doctor who is not busy
        DoctorsManager.update_busy_by_id(7)
        self.assertTrue(doctor1._is_busy)

        # Test updating a doctor who is already busy
        DoctorsManager.update_busy_by_id(7)
        self.assertFalse(doctor1._is_busy)

        # Test updating a doctor who does not exist
        DoctorsManager.update_busy_by_id(3)  # no doctor with id 3


if __name__ == '__main__':
    unittest.main()
