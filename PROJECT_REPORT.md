Academic Project Report: Hospital Patient Management System

Course: “Python Essentials”
Project Title: “Hospital Patient Management System”

---

1. Introduction
The Hospital Patient Management System is a console-based application written in Python that automates hospital management operations: patient admittance, doctor’s records, physician allocation, medical record update and viewing and itemized billing calculation. The project is confined within the first-year Python’s Essentials syllabus: it uses basic data structures and object-oriented programming.
---

2. Problem Statement
Small healthcare clinics and community pharmacies have traditionally used paper logbooks to record patient admission data and doctor allocations. Such analog systems incur high overheads in terms of administrative work and record-keeping. There are frequent errors in assigning hospital rooms due to double-booking. Calculating itemized bills and insurance discounts is also error-prone. Doctor’s and admitted patient’s records are siloed: there is no unified source of truth for patient admittance information.

An automated, light-weight, in-memory terminal management system would address all of the above without requiring a heavy database engine and external software.
---

3. Objectives
• To design a modular line-edited command-line interface for hospital record keeping.
• To employ Object-Oriented Programming paradigm to define classes and objects for Patient, Doctor and Hospital.
• To demonstrate utilization of built-in string methods (e.g. .isdigit( )) for input validation instead of try-except blocks.
• To showcase Python’s built-in data structures: dictionary, list, tuple, set and frozenset.
• To implement numerical billing calculation using array module and bitwise flagging.
• To verify the implementation’s correctness with assert statements instead of external testing frameworks.
---

4. Proposed Solution
The proposed solution involves developing a modular command-line application organized in Python modules. The application will utilize in-memory dictionaries for fast $O(1)$ lookups. Sets will be employed to hold room allocations to avoid duplication. Tuples will be used to hold constants such as valid blood groups and itemized billing receipt. Billing calculations will use arrays for storing charge items and perform bitwise AND to compute discounts.
---

5. Features
1. Patient registration: patient’s details such as age, gender, diagnosis, room number and admittance flags are stored.
2. Doctor roster management: doctors’ specialty, phone numbers and availability are updated.
3. Physician allocation: available doctors are assigned to patients on a first-come basis using object references.
4. Diagnostic and treatment update: patient’s diagnosis and treatment plan are updated.
5. Itemized billing calculation: itemized billing receipts are generated. The total amount due is calculated as a combination of consultation fee, room charge and medicine charges. Consultation fee and medicine charges are hard-coded. Room charge depends on length of stay and is calculated as daily rate x number of days. Discounts are granted if the patient is covered by insurance: they amount to 15% of the subtotal. Net due is calculated as subtotal less discounts. The average daily cost is calculated as total amount due divided by length of stay.
6. Patient search and detail view: a patient’s details can be viewed given their ID.
7. Patient discharge and room reclamation: discharged patients are removed from the in-memory database. Their room number is deallocated from the room set.
---

6. Technologies and Concepts Used

| Syllabus Topic | Utilization |
| :--- | :--- |
| Python Fundamentals | Adherence to PEP8 standards is observed by using descriptive identifiers, proper indenting, dynamic typing and following standard program flow conventions. |
| Membership Operators (`in`, `not in`) | Used extensively to check for duplicate patient admission IDs, room occupancy and valid blood groups. |
| Assignment Operators (`=`, `+=`, `-=`) | Billing subtotals are accumulated using += operator; object attributes are updated. |
| Bitwise Operators (`&`, `\|`) | Admission flags are set: `FLAG_INSURANCE = 1` ($01_2$) and `FLAG_EMERGENCY = 2` ($10_2$). |
| `type()` Function | Used extensively to verify that only numeric values are stored in billing arrays. Example: `type(val) == int or type(val) == float`. |
| Identity Operators (`is`, `is not`) | Used to determine if a patient has no assigned physician: `pat.assigned_doc is None`. |
| Arithmetic Operators (`+`, `-`, ``, `/`) | Used in billing calculations such as subtotal, multi-day room charges, discounts and average daily cost. |
| Logical Operators (`and`, `or`, `not`) | Used in enforcing input constraints: e.g. `age >= 0 and age <= 120`. |
| Relational Operators (`==`, `!=`, `<`, `>`) | Used in implementing command-line menu options and general comparisons. |
| Type Casting (`int()`, `float()`, `str()`) | Terminal inputs are converted from strings to integers and floats where applicable. Strings are cast to terminals for display. |
| Core Collections | Dictionaries are used as key-value stores; lists as sequences; tuples as immutable sequences; sets for room allocations; frozensets for valid departments. |
| Control Flow | `while` loops are used for implementing continuous menu; `if-elif-else` for routing; `for` loops for iterating through sequences; `break` and `continue`. |
| Functions | Used extensively in modularizing the code: billing logic, menu rendering, validation checks. |
| Modules & Packages | The code is split into modules for better maintainability: `patient.py`, `doctor.py`, `billing.py`, `hospital.py` and `main.py`. |
| Array Data Structure | `from array import array`: creates double-precision arrays for storing billing charge items. Example: `array('d', [...])`. |
| OOP Fundamentals | Classes and objects are used without magic methods: attributes and instance methods are defined. |
## Non-Functional Requirements

The Hospital Patient Management System satisfies the following non-functional requirements.

1. Usability

The application uses a simple menu-driven text-based interface that allows hospital staff to easily register patients, manage doctors, assign doctors, update medical details, and prepare hospital bills.

2. Reliability

The application validates important user inputs to avoid the following: registering the same patient twice, registering the same doctor twice, entering invalid numeric data, and removing non-existent patients.

3. Maintainability

The application is designed with separate Python modules for patients, doctors, billing, managers, and the main application. This modularity improves the readability, testability, and maintainability of the source code.

4. Error Handling

The application validates user input data and reports errors to the user in a friendly manner.

5. Performance

The application uses efficient data structures such as dictionaries and sets to store and retrieve patient records, doctor records, and occupied hospital beds. It is designed for smaller applications and clinics.

6. Resource Efficiency

The application does not require any external framework or database because Python has built-in data structures such as dictionaries and sets. This project stores patient and doctor records temporarily (in the memory) during the execution of the program.

7. Security / Data Protection

This application is a local application and therefore, does not store or share patient medical information in a network or over the internet. However, future versions should implement strong security measures, such as authentication and authorization, before deploying this application in a production environment.
---
7.## 7. System Design & Architecture

```
                  +--------------------------------+
                  |         main.py (CLI)          |
                  +---------------+----------------+
                                  |
         +------------------------+------------------------+
         |                        |                        |
         v                        v                        v
+-----------------+      +-----------------+      +-----------------+
|   patient.py    |      |    doctor.py    |      |   billing.py    |
|  Class Patient  |<-----+  Class Doctor   |      |  Array & Flags  |
+--------+--------+      +--------+--------+      +--------+--------+
         |                        |                        |
         +------------------------+------------------------+
                                  |
                                  v
                       +--------------------+
                       |    hospital.py     |
                       |   Class Hospital   |
                       | (In-Memory Store)  |
                       +--------------------+
```

---


##Use Case Diagram

Actors:

Hospital Staff
Front Desk / Admission Clerk
Billing/Discharge Officer

Use cases:

Register Patient
Search Patient
Update Patient
Delete Patient
Add Doctor
View Doctors
Assign Doctor
Update Diagnosis/Treatment
Generate Bill
Discharge Patient
## work Flow
Start
  ↓
Display Main Menu
  ↓
Select Operation
  ↓
Register / Search / Update / Doctor / Billing
  ↓
Validate Input
  ↓
Perform Operation
  ↓
Display Result
  ↓
Return to Menu
  ↓
Exit?
 ├── No → Main Menu
 └── Yes → End
 ## class Diagram
 Patient
 ├── patient_id
 ├── name
 ├── age
 ├── gender
 ├── contact
 ├── blood_group
 ├── room_no
 ├── diagnosis
 └── treatment

Doctor
 ├── doctor_id
 ├── name
 ├── specialization
 └── availability

Hospital
 ├── patients
 ├── doctors
 ├── occupied_rooms
 ├── add_patient()
 ├── remove_patient()
 ├── add_doctor()
 └── assign_doctor_to_patient()

Billing
 └── calculate_bill()
 ##Sequence Diagram
 Patient Registration

User → Main
Main → Hospital: add_patient()
Hospital → Patient: create Patient
Patient → Hospital: patient object
Hospital → Main: success/failure
Main → User: display result
##ER Diagram

ER Diagram: Not Applicable
The current project uses in-memory Python data structures instead of a persistent relational database. Therefore, a traditional ER diagram is not required for the current implementation. Future versions using SQLite/MySQL/PostgreSQL would require an ER diagram

8. Module Descriptions

### `patient.py`
This module stores the `Patient` class. Class methods perform core duties such as adding personal details, updating phone/address, recording diagnosis/treatment, updating bitwise admission flags, tracking assigned physician’s reference and displaying information.

### `doctor.py`
This module stores the `Doctor` class. Class methods perform core duties such as doctor specialization, phone number and availability update and information display.

### `hospital.py`
This module coordinates the in-memory data structures. It defines:
• `patients_data`: a dictionary keyed on `pat_id` with patient objects as values.
• `doctors_data`: a dictionary keyed on `doc_id` with doctor objects as values.
• `occupied_rooms`: a set that tracks room numbers that are currently occupied.

• `patient_ids_list`: a list that stores patient admission sequence.

• `all_blood_groups`: a tuple that stores valid blood groups.
• `departments`: a frozenset that stores valid departments.

### `billing.py`
This module contains billing logic, bitwise constants, validation checks and receipt display. It declares `FLAG_INSURANCE` and `FLAG_EMERGENCY`. It uses `type( )` to check that the value stored in an array is a float. The bill subtotals are stored in a double array (`array('d', [...])`). It displays the final billing receipt as a tuple: `(subtotal, discount, net_total, avg_day, charges_array)`.
### `main.py`
This is the entry point module. It contains robust input handling routines that use `.isdigit( )` to verify that the user is entering numbers. It also creates sample records for testing purposes. It displays the 12-item command-line menu and routes requests.
---
9. OOP Classes & Responsibilities
### Class `Patient`
The `__init__()` method defines the object’s attributes such as `pat_id`, p_name`, `p_age`, `p_gender`, `p_phone`, `p_address`, `p_blood`, admission flags, assigned physician reference and treatment plan.
The `display_info()` method displays the personal details, assigned doctor details (if any) and admits/discharge status.
The `update_contact(new_phone, new_addr)` updates the phone number and address.
The `set_diagnosis(new_disease, new_treatment)` method updates the diagnosis and treatment plan.
### Class `Doctor`
The `__init__()` method defines the object’s attributes such as `doc_id`, `d_name`, `d_spec`, `d_phone`, and `d_avail`.
The `display_info()` method displays the personal details, specialization and availability.
The `set_availability(new_status)` updates the physician’s availability status.

### Class `Hospital`
The `__init__(hosp_name)` method instantiates the dictionary, lists, sets, tuples and frozensets.
The `add_patient(pat_obj)` adds a patient and allocates a room from the room set.
The `get_patient(p_id)` gets a patient from the `patients_data` dictionary.
The `show_all_patients()` displays all patients.
The `remove_patient(p_id)` removes a patient from the `patients_data` dictionary. It also deallocates the room.
The `add_doctor(doc_obj)` adds a doctor to the `doctors_data` dictionary.
The `get_doctor(d_id)` gets a doctor from the `doctors_data` dictionary.
The `show_all_doctors()` displays all doctors.
The `assign_doctor_to_patient(p_id, d_id)` sets the doctor reference on the selected patient.
---
10. Data Structures Used
1. Dictionary (`dict`): This is the primary data structure used for storing patients and doctors since it provides constant time $O(1)$
| Lookup and Update | Example |
| :--- | :--- |
| `patients_data[pat_id] = pat_obj` | Adds a new patient record |
| `doc = doctors_data.get(d_id)` | Gets a doctor by ID |
2. List (`list`): A list is used to store the patient admission sequence.
| Purpose | Example |
| :--- | :--- |
| Iterating through elements in order | `for p_id in patient_ids_list:` |
| Maintaining order | `patient_ids_list.append(p_id)` |
3. Tuple (`tuple`): Tuples are used to store constants such as blood groups and generate itemized billing receipts.
| Purpose | Example |
| :--- | :--- |
| `all_blood_groups = ('A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-')` | Store valid blood groups |
| Returning values from functions/methods | `return (subtotal, discount, net_total)` |
4. Set (`set`): The set data structure is used to store the room numbers that are currently occupied.
| Purpose | Example |
| :--- | :--- |
| Fast lookups to determine room availability | `room_num in occupied_rooms` |
| Removing a room from the set | `occupied_rooms.remove(room_num)` |
5. Frozen Set (`frozenset`): This data structure is used to store valid departments.
6. Array (`array`): Arrays are used to store the billing charge items. The array of type `double` is instantiated using `from array import array` and `array('d', [...])`.
---
11. Control Flow Used
| Statement | Utilization |
| :--- | :--- |
| `while True`: | This loop is used to implement the command-line interface. It terminates on the option 12. |
| `if / elif / else`: | This statement is used to route requests based on the selected menu option. |
| `for`: | This loop is used iterate through sequences such as the patient ID list. |
| `break`: | This statement terminates the while loop and exits the application. It is triggered when the user selects option 12. |
| `continue`: | This statement skips to the next iteration of the loop. It is used when the user enters invalid menu options. |
---
12.
Sample Execution

### Adding a Patient
```text
--- ADD NEW PATIENT ---
Enter Patient ID (e.g. P301): P301
Enter Patient Name: Eleanor Vance
Enter Patient Age: 29
Enter Gender (Male/Female/Other): Female
Enter Phone Number: 555-7788
Enter Address: 42 Crestview Rd
Valid Blood Groups: ('A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-')
Enter Blood Group: A+
Enter Initial Diagnosis/Reason: Bronchitis
Enter Treatment Plan: Antibiotics and inhaler
Enter Room Number: 105
Is patient covered by insurance? (1 for Yes, 0 for No): 
Choice: 1
Is this an emergency admission? (1 for Yes, 0 for No): 
Choice: 0
Patient Eleanor Vance added successfully.
```

### Itemized Billing Receipt
```text
========================================
          PATIENT BILL RECEIPT          
========================================
Patient ID: P201
Patient Name: Alice Johnson
Doctor: Dr. Robert Smith (Cardiology)
----------------------------------------
Consultation Fee: $100.0
Room Charges:     $200.0
Medicine Charges: $100.0
----------------------------------------
Subtotal:         $400.0
Discount (Ins):  -$60.0
Net Amount Due:   $340.0
Avg Daily Cost:   $85.0
========================================
```

---
---
13. Testing Cases (`tests/test_project.py`)
The test suite is executed by simply running the script:
```bash
python3 tests/test_project.py
```
### Test Case Matrix:
1. `test_patient_and_doctor_init()`: Verifies that attributes are properly assigned including default values and status updates.
2. `test_doctor_assignment()`: Confirms that `is None` and `is not None` work as expected.
3. `test_bitwise_and_billing()`:
- Confirms that bitwise AND combination works as expected: `FLAG_INSURANCE | FLAG_EMERGENCY == 3`.
- Confirms that `check_numeric_val()` works as expected using `type( )`.
- Confirms that the array is correctly instantiated (`array('d')`). The loop correctly sums all charge items. The code correctly applies a 15% discount on the subtotal for insured patients. The net due is calculated and compared to an expected value.
4. `test_hospital_collections()`:
- Confirms that `in` and `not in` work on tuples and frozensets.
- Confirms that a patient can be added and that the dictionary correctly stores the values. The list is correctly updated. The set is correctly updated to indicate an occupied room. The `get_patient()` method correctly returns the expected patient.
- Confirms that a patient can be deleted and that the room set is correctly updated.
---
14. Limitations
• No Long Term Persistence: The records are only held in memory. Quitting the program kills all data.
• Single Terminal Session: There is no support for concurrent users.
• Strict Key Search: The search is performed on exact match of Patient or Doctor ID only.
---
15. Future Scope
• File I/O: We could persist the data to files (text or binary) after we learn about file handling modules.
• Search by Name and Doctor Specialization: It would be more intuitive to search by patient name. There should also be a way to filter doctors by specialization.
• Multi-Doctor Consultations and Appointments: Patients should be able to consult multiple doctors. The system should support scheduling.
---

16. Conclusion
The Hospital Patient Management System satisfies all requirements of the “Python Essentials” course. It uses object-oriented programming to model a real-life use case. Python’s built-in data structures such as dictionaries, lists, tuples, sets and frozensets are utilized. Bitwise operators are used for admissions flags. The array module is used for storing billing charge items. Input validation is achieved using string methods and without using exception handling.