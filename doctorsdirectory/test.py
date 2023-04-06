import unittest
import Doctor
import DoctorsManager


class MyTestCase(unittest.TestCase):
    def test_doctor_properties(self):
        doc = Doctor("John Smith", "Cardiology")
        self.assertEqual(doc._name, "John Smith")
        self.assertEqual(doc._speciality, "Cardiology")
        self.assertFalse(doc._is_busy)

    def test_doctor_update_busy(self):
        doc = Doctor("John Smith", "Cardiology")
        self.assertFalse(doc._is_busy)
        doc.update_busy()
        self.assertTrue(doc._is_busy)
        doc.update_busy()
        self.assertFalse(doc._is_busy)

    def test_doctor_get_id(self):
        doc1 = Doctor("John Smith", "Cardiology")
        doc2 = Doctor("Jane Doe", "Neurology")
        self.assertNotEqual(doc1.get_id(), doc2.get_id())

    def setUp(self):
        self.doc1 = Doctor("John Smith", "Cardiology")
        self.doc2 = Doctor("Jane Doe", "Neurology")
        self.doc3 = Doctor("Bob Johnson", "Cardiology")
        DoctorsManager.add_doctor(self.doc1)
        DoctorsManager.add_doctor(self.doc2)
        DoctorsManager.add_doctor(self.doc3)

    def tearDown(self):
        DoctorsManager._list = None

    def test_get_doctors_with_speciality(self):
        cardiology_doctors = DoctorsManager.get_doctors("Cardiology")
        neurology_doctors = DoctorsManager.get_doctors("Neurology")
        self.assertEqual(len(cardiology_doctors), 2)
        self.assertEqual(len(neurology_doctors), 1)

    def test_get_all_doctors(self):
        all_doctors = DoctorsManager.get_doctors()
        self.assertEqual(len(all_doctors), 3)

    def test_update_busy(self):
        self.assertFalse(self.doc1._is_busy)
        DoctorsManager.update_busy(self.doc1.get_id())
        self.assertTrue(self.doc1._is_busy)
        DoctorsManager.update_busy(self.doc1.get_id())
        self.assertFalse(self.doc1._is_busy)


if __name__ == '__main__':
    unittest.main()

# Doc1 = Doctor("Jean Gontrand", "Cardiologue")
# Doc2 = Doctor("Eric Zoo", "Uretrologue")
# print(Doc1)
# test_list = [Doc1, Doc2]
# print(next((x for x in test_list if x.get_id() == 1), None))
