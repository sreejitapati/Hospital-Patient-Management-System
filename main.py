from patient import Patient
from doctor import Doctor
from hospital import Hospital
from billing import calculate_bill, display_bill_slip, FLAG_INSURANCE, FLAG_EMERGENCY

def check_is_float_str(str_val):
    if str_val == "":
        return False
    dot_count = 0
    for ch in str_val:
        if ch == ".":
            dot_count += 1
            if dot_count > 1:
                return False
        elif ch not in "0123456789":
            return False
    return True

def read_int_input(prompt_msg):
    while True:
        raw_val = input(prompt_msg).strip()
        if raw_val.isdigit():
            return int(raw_val)
        print("Invalid input. Please enter a valid whole number.")

def read_float_input(prompt_msg):
    while True:
        raw_val = input(prompt_msg).strip()
        if check_is_float_str(raw_val):
            return float(raw_val)
        print("Invalid input. Please enter a valid numeric value.")

def read_non_empty_str(prompt_msg):
    while True:
        raw_val = input(prompt_msg).strip()
        if raw_val != "":
            return raw_val
        print("Input cannot be empty. Please try again.")

def populate_initial_data(hosp):
    doc1 = Doctor("D101", "Dr. Robert Smith", "Cardiology", "555-0101", True)
    doc2 = Doctor("D102", "Dr. Sarah Adams", "Neurology", "555-0102", True)
    hosp.add_doctor(doc1)
    hosp.add_doctor(doc2)

    pat1 = Patient("P201", "Alice Johnson", 32, "Female", "555-1111", "12 Maple St", "O+", "Hypertension", "Medication and rest", 101, FLAG_INSURANCE)
    pat2 = Patient("P202", "David Miller", 45, "Male", "555-2222", "84 Oak Ave", "A+", "Migraine", "Therapy", 102, FLAG_EMERGENCY)
    hosp.add_patient(pat1)
    hosp.add_patient(pat2)
    hosp.assign_doctor_to_patient("P201", "D101")

def display_menu():
    print("\n========================================")
    print("   HOSPITAL PATIENT MANAGEMENT SYSTEM   ")
    print("========================================")
    print("1.  Add New Patient")
    print("2.  Display All Patients")
    print("3.  Search Patient by ID")
    print("4.  View Specific Patient Details")
    print("5.  Update Patient Information")
    print("6.  Delete Patient")
    print("7.  Add Doctor Information")
    print("8.  Display Doctors")
    print("9.  Assign Doctor to Patient")
    print("10. Record Diagnosis and Treatment")
    print("11. Calculate Patient Bill")
    print("12. Exit Program")
    print("========================================")

def handle_add_patient(hosp):
    print("\n--- ADD NEW PATIENT ---")
    p_id = read_non_empty_str("Enter Patient ID (e.g. P301): ")
    if p_id in hosp.patients_data:
        print("Error: Patient ID already exists.")
        return

    p_name = read_non_empty_str("Enter Patient Name: ")
    p_age = read_int_input("Enter Patient Age: ")
    p_gender = read_non_empty_str("Enter Gender (Male/Female/Other): ")
    p_phone = read_non_empty_str("Enter Phone Number: ")
    p_addr = read_non_empty_str("Enter Address: ")

    print("Valid Blood Groups: " + str(hosp.all_blood_groups))
    p_blood = read_non_empty_str("Enter Blood Group: ")
    if p_blood not in hosp.all_blood_groups:
        print("Notice: Non-standard blood group recorded.")

    p_disease = read_non_empty_str("Enter Initial Diagnosis/Reason: ")
    p_treat = read_non_empty_str("Enter Treatment Plan: ")

    p_room = read_int_input("Enter Room Number: ")
    if p_room in hosp.occupied_rooms:
        print("Warning: Room " + str(p_room) + " is already occupied. Setting room to 0.")
        p_room = 0

    print("Is patient covered by insurance? (1 for Yes, 0 for No): ")
    ins_choice = read_int_input("Choice: ")
    print("Is this an emergency admission? (1 for Yes, 0 for No): ")
    emerg_choice = read_int_input("Choice: ")

    s_flags = 0
    if ins_choice == 1:
        s_flags = s_flags | FLAG_INSURANCE
    if emerg_choice == 1:
        s_flags = s_flags | FLAG_EMERGENCY

    new_pat = Patient(p_id, p_name, p_age, p_gender, p_phone, p_addr, p_blood, p_disease, p_treat, p_room, s_flags)
    hosp.add_patient(new_pat)
    print("Patient " + p_name + " added successfully.")

def handle_search_patient(hosp):
    print("\n--- SEARCH PATIENT ---")
    p_id = read_non_empty_str("Enter Patient ID: ")
    pat = hosp.get_patient(p_id)
    if pat is None:
        print("No patient found with ID: " + p_id)
    else:
        print("Patient record found:")
        pat.display_info()

def handle_update_patient(hosp):
    print("\n--- UPDATE PATIENT INFORMATION ---")
    p_id = read_non_empty_str("Enter Patient ID to update: ")
    pat = hosp.get_patient(p_id)
    if pat is None:
        print("Patient not found.")
        return

    print("Leave field blank and press Enter to keep current value.")
    new_phone = input("Enter new phone (" + str(pat.p_phone) + "): ").strip()
    new_addr = input("Enter new address (" + str(pat.p_address) + "): ").strip()
    pat.update_contact(new_phone, new_addr)
    print("Contact details updated successfully.")

def handle_delete_patient(hosp):
    print("\n--- DELETE PATIENT ---")
    p_id = read_non_empty_str("Enter Patient ID to delete: ")
    success = hosp.remove_patient(p_id)
    if success:
        print("Patient " + p_id + " deleted successfully.")
    else:
        print("Error: Patient ID not found.")

def handle_add_doctor(hosp):
    print("\n--- ADD DOCTOR ---")
    d_id = read_non_empty_str("Enter Doctor ID (e.g. D103): ")
    if d_id in hosp.doctors_data:
        print("Error: Doctor ID already exists.")
        return

    d_name = read_non_empty_str("Enter Doctor Name: ")
    print("Standard Departments: " + str(sorted(list(hosp.departments))))
    d_spec = read_non_empty_str("Enter Specialization: ")
    d_phone = read_non_empty_str("Enter Phone Number: ")

    new_doc = Doctor(d_id, d_name, d_spec, d_phone, True)
    hosp.add_doctor(new_doc)
    print("Doctor " + d_name + " added successfully.")

def handle_assign_doctor(hosp):
    print("\n--- ASSIGN DOCTOR TO PATIENT ---")
    p_id = read_non_empty_str("Enter Patient ID: ")
    pat = hosp.get_patient(p_id)
    if pat is None:
        print("Patient not found.")
        return

    d_id = read_non_empty_str("Enter Doctor ID: ")
    doc = hosp.get_doctor(d_id)
    if doc is None:
        print("Doctor not found.")
        return

    hosp.assign_doctor_to_patient(p_id, d_id)
    print("Doctor " + doc.d_name + " assigned to Patient " + pat.p_name + ".")

def handle_record_diagnosis(hosp):
    print("\n--- RECORD DIAGNOSIS AND TREATMENT ---")
    p_id = read_non_empty_str("Enter Patient ID: ")
    pat = hosp.get_patient(p_id)
    if pat is None:
        print("Patient not found.")
        return

    new_dis = read_non_empty_str("Enter Updated Diagnosis: ")
    new_treat = read_non_empty_str("Enter Updated Treatment: ")
    pat.set_diagnosis(new_dis, new_treat)
    print("Diagnosis and treatment updated successfully.")

def handle_billing(hosp):
    print("\n--- CALCULATE PATIENT BILL ---")
    p_id = read_non_empty_str("Enter Patient ID: ")
    pat = hosp.get_patient(p_id)
    if pat is None:
        print("Patient not found.")
        return

    consult_fee = read_float_input("Enter Doctor Consultation Fee ($): ")
    stay_days = read_int_input("Enter Number of Room Days: ")
    room_rate = read_float_input("Enter Daily Room Rate ($): ")
    medicine_cost = read_float_input("Enter Medicine and Lab Charges ($): ")

    bill_tuple = calculate_bill(consult_fee, stay_days, room_rate, medicine_cost, pat.service_flags)
    if bill_tuple is not None:
        pat.bill_summary = bill_tuple
        display_bill_slip(pat, bill_tuple)
    else:
        print("Failed to calculate bill due to invalid numeric input.")

def main():
    hosp_inst = Hospital("City Care Community Hospital")
    populate_initial_data(hosp_inst)

    while True:
        display_menu()
        choice_str = input("Enter your choice (1-12): ").strip()
        if not choice_str.isdigit():
            print("Please enter a number between 1 and 12.")
            continue

        choice = int(choice_str)

        if choice == 1:
            handle_add_patient(hosp_inst)
        elif choice == 2:
            hosp_inst.show_all_patients()
        elif choice == 3:
            handle_search_patient(hosp_inst)
        elif choice == 4:
            handle_search_patient(hosp_inst)
        elif choice == 5:
            handle_update_patient(hosp_inst)
        elif choice == 6:
            handle_delete_patient(hosp_inst)
        elif choice == 7:
            handle_add_doctor(hosp_inst)
        elif choice == 8:
            hosp_inst.show_all_doctors()
        elif choice == 9:
            handle_assign_doctor(hosp_inst)
        elif choice == 10:
            handle_record_diagnosis(hosp_inst)
        elif choice == 11:
            handle_billing(hosp_inst)
        elif choice == 12:
            print("\nThank you for using the Hospital Patient Management System. Exiting...")
            break
        else:
            print("Invalid choice. Please select an option from 1 to 12.")

if __name__ == "__main__":
    main()
