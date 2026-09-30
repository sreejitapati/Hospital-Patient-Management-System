import sys
sys.path.insert(0, ".")

from hospital import Hospital
from patient import Patient
from doctor import Doctor


def test_hospital_init():
    hosp = Hospital("City Care Hospital, Bengaluru")
    assert hosp.hosp_name == "City Care Hospital, Bengaluru"
    assert len(hosp.patients_data) == 0
    assert len(hosp.doctors_data) == 0
    assert len(hosp.occupied_rooms) == 0
    assert len(hosp.patient_ids_list) == 0
    assert "A+" in hosp.all_blood_groups
    assert "Cardiology" in hosp.departments


def test_add_and_get_patient():
    hosp = Hospital("City Care Hospital, Bengaluru")
    p = Patient("P101", "Aarav Sharma", 29, "Male", "9876543210", "12 MG Road, Indiranagar, Bengaluru", "O+", "Viral Fever", "Rest and Hydration", 101)

    assert hosp.add_patient(p) is True
    assert "P101" in hosp.patients_data
    assert "P101" in hosp.patient_ids_list
    assert 101 in hosp.occupied_rooms

    # verify fetching the registered patient
    found = hosp.get_patient("P101")
    assert found is not None
    assert found.p_name == "Aarav Sharma"

    # querying an unknown ID should return None
    assert hosp.get_patient("P999") is None


def test_duplicate_patient_id():
    hosp = Hospital("City Care Hospital, Bengaluru")
    p1 = Patient("P101", "Aarav Sharma", 29, "Male", "9876543210", "12 MG Road, Indiranagar, Bengaluru", "O+", "Viral Fever", "Rest", 101)
    p2 = Patient("P101", "Rohan Verma", 45, "Male", "9845012345", "45 Brigade Road, Bengaluru", "A-", "Cough", "Syrup", 102)

    assert hosp.add_patient(p1) is True
    # duplicate ID must be rejected
    assert hosp.add_patient(p2) is False
    assert len(hosp.patients_data) == 1
    assert hosp.patients_data["P101"].p_name == "Aarav Sharma"


def test_outpatient_room_zero():
    hosp = Hospital("City Care Hospital, Bengaluru")
    # room = 0 represents OPD consultation without bed admission
    p = Patient("P102", "Priya Nair", 34, "Female", "9741234567", "88 Koramangala 4th Block, Bengaluru", "B+", "Routine Checkup", "None", 0)

    assert hosp.add_patient(p) is True
    assert 0 not in hosp.occupied_rooms
    assert len(hosp.occupied_rooms) == 0


def test_remove_patient():
    hosp = Hospital("City Care Hospital, Bengaluru")
    p = Patient("P103", "Sunita Deshmukh", 52, "Female", "9123456780", "104 FC Road, Shivaji Nagar, Pune", "AB+", "Joint Pain", "Physiotherapy", 204)
    hosp.add_patient(p)

    assert 204 in hosp.occupied_rooms
    assert "P103" in hosp.patients_data

    # discharge patient and verify room is released
    assert hosp.remove_patient("P103") is True
    assert "P103" not in hosp.patients_data
    assert "P103" not in hosp.patient_ids_list
    assert 204 not in hosp.occupied_rooms

    # trying to remove again should safely return False
    assert hosp.remove_patient("P103") is False
    assert hosp.remove_patient("INVALID_ID") is False


def test_doctor_management():
    hosp = Hospital("City Care Hospital, Bengaluru")
    doc1 = Doctor("D201", "Dr. Suresh Kulkarni", "General", "9822011223", True)
    doc_dup = Doctor("D201", "Dr. Ramesh Gupta", "Pediatrics", "9822099887", True)

    assert hosp.add_doctor(doc1) is True
    assert hosp.add_doctor(doc_dup) is False
    assert len(hosp.doctors_data) == 1

    fetched = hosp.get_doctor("D201")
    assert fetched is not None
    assert fetched.d_name == "Dr. Suresh Kulkarni"
    assert hosp.get_doctor("D999") is None


def test_assign_doctor():
    hosp = Hospital("City Care Hospital, Bengaluru")
    p = Patient("P104", "Vikram Malhotra", 38, "Male", "9811223344", "22 Connaught Place, New Delhi", "A+", "Chest Pain", "ECG Monitoring", 105)
    doc = Doctor("D202", "Dr. Meenakshi Sundaram", "Cardiology", "9844055667", True)

    hosp.add_patient(p)
    hosp.add_doctor(doc)

    assert p.assigned_doc is None

    # successful doctor assignment
    assert hosp.assign_doctor_to_patient("P104", "D202") is True
    assert p.assigned_doc is not None
    assert p.assigned_doc.doc_id == "D202"
    assert p.assigned_doc.d_name == "Dr. Meenakshi Sundaram"

    # invalid IDs should be rejected
    assert hosp.assign_doctor_to_patient("NON_EXISTENT", "D202") is False
    assert hosp.assign_doctor_to_patient("P104", "NON_EXISTENT") is False


def test_display_helpers():
    hosp = Hospital("City Care Hospital, Bengaluru")

    # verify empty rosters don't raise errors
    hosp.show_all_patients()
    hosp.show_all_doctors()

    # populate and display again
    p = Patient("P105", "Ananya Iyer", 24, "Female", "9900112233", "15 Anna Salai, Chennai", "O-", "Migraine", "Pain Relief", 301)
    doc = Doctor("D203", "Dr. Rajesh Mukherjee", "General", "9830012345", True)
    hosp.add_patient(p)
    hosp.add_doctor(doc)

    hosp.show_all_patients()
    hosp.show_all_doctors()


if __name__ == "__main__":
    test_hospital_init()
    test_add_and_get_patient()
    test_duplicate_patient_id()
    test_outpatient_room_zero()
    test_remove_patient()
    test_doctor_management()
    test_assign_doctor()
    test_display_helpers()
    print("All hospital tests passed successfully!")