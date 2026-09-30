# Hospital Patient Management System

Python beginner-friendly menu-driven command-line hospital patient management, doctor allocation and itemized billing application

## 1. Project Description

The Hospital Patient Management System is an academic terminal based application for an introductory "Python Essentials" course. The application is used for an hospital administrative staff to register patients, maintain doctor rosters, assign medical specialties to patients, log diagnostic updates and generate itemized billing calculations.

The project makes use of foundational Python concepts without the use of external packages, frameworks or database engines. The application stores all data in memory using Python data structures.

## 2. Objectives

- Provide a reliable menu-driven terminal based interface for an hospital record keeping.
- Demonstrate the use of Object-Oriented Programming (OOP), classes, objects and encapsulation.
- Naturally use the Python fundamental data structures such as lists, tuples, sets, dictionaries, frozen sets.
- Implement realistic mathematical and billing logic using arithmetic and bitwise operations.
- Use input handling without external libraries or advanced exception handling.

## 3. Features

1. Add Patient: Add a patient to the database with Patient ID, Name, Age, Gender, Phone, Blood group, Diagnosis, Room number, Admission details etc.
2. Display All Patients: Display all patients in a formatted manner.

3. Search Patient: Search a patient in the database by Patient ID.
4. View Specific Details: View a specific patients medical, assigned physician and billing details.
5. Update Patient: Update a patients contact numbers and address.
6. Delete Patient: Delete discharged patients and free up hospital rooms.
7. Add Doctor: Add a medical specialist to the database with their ID, Name, Department, Phone number etc.
8. Display Doctors: Display all the doctors and their availability status.
9. Assign Doctor: Assign an available doctor to a patient record.
10. Record Diagnosis and Treatment: Record a patients clinical observations and treatment.
11. Calculate Bill: Calculate consultation fees, room stay charges, medicine fees and insurance discounts using arrays and bitwise flags.
12. Data Validation: Enforces duplicate ID checks, numeric validation and room collision prevention without exception handling.
## 4. Python Concepts Used
| Topic | Where & How is it used |
| :--- | :--- |
| Python Fundamentals | Clean program execution, standard variables and dynamic typing |
| Membership Operators (`in`, `not in`) | Used for checking for duplicate IDs, room availability and blood group validation |
| Assignment Operators (`=`, `+=`, `-=`) | Used for accumulation of charges in running totals and setting attributes |
| Bitwise Operators (`&`, `\|`) | Used for patient admission flags: `FLAG_INSURANCE = 1` ($01_2$) and `FLAG_EMERGENCY = 2` ($10_2$) |
| `type()` Function | Used for type checking of charge values to be numeric (`int` or `float`) before billing |
| Identity Operators (`is`, `is not`) | Used for checking if a doctor is assigned (`pat.assigned_doc is None` / `pat.assigned_doc is not None`) |
| Arithmetic Operators (`+`, `-`, ``, `/`) | Used for computing room charges, discounts, subtotal and average daily cost |
| Logical Operators (`and`, `or`, `not`) | Used for compound input verification and string presence checks |
| Relational Operators (`==`, `!=`, `<`, `>`) | Used for processing menu options, numeric comparisons and search matches |
| Type Conversion (`int()`, `float()`, `str()`) | Used for parsing terminal inputs into integers and floating point values |
| Lists | Used for maintaining an ordered registry of patient IDs (`patient_ids_list`) |

| Tuples | Used for standard hospital blood groups and for billing summary outputs |
| Sets | Used for fast tracking of currently occupied room numbers (`occupied_rooms`) |
| Dictionaries | Used for key-value storage of patients (`pat_id -> Patient`) and doctors (`doc_id -> Doctor`) |
| Frozen Sets | Used for for an immutable set of standard hospital departments (`valid_departments`) |
| Control Flow (`if-elif-else`, `while`, `for`) | Used for menu loops, option routing and record iterations |
| Functions | Used for modular procedures of billing, receipt display and input reading |
| Modules & Packages | Used for separation of code into `patient.py`, `doctor.py`, `hospital.py`, `billing.py` and `main.py` |
| Array Module (`array`) | Storing double-precision charge components (`array('d', [...])`) in `billing.py` |
| Object-Oriented Programming (OOP) | Classes (`Patient`, `Doctor`, `Hospital`) with constructors and instance methods |
## 5. Project Structure
```
hospital_management/
│
├── main.py      # Entry point with interactive CLI menu and input validation
├── patient.py     # Patient class handling individual patient records
├── doctor.py     # Doctor class storing physician profiles
├── hospital.py    # Hospital class managing in memory collections and relationships
├── billing.py     # Financial calculations, array processing and bitwise flags
├── test_project.py  # Test suite verifying core logic using plain assert statements
├── requirements.txt  # Dependency specifications (standard library only)
└── README.md     # Comprehensive project documentation
```
## 6. Requirements
- Python 3.6 or higher
- Standard Python library only (no external pip dependencies)
## 7. Installation and Setup Instructions
1. Clone or download the repository to your local computer
2. Open a terminal (macOS/Linux) or Command Prompt/PowerShell (Windows)
3. Navigate to the project directory:
```bash
cd /path/to/hospital_management
```
## 8. How to run the project from the terminal
Run the main application file using Python:
```bash
python3 main.py
```
(On Windows systems may use `python main.py`)
To run the verification test suite:
```bash
python3 test_project.py
```
## 9. How to use the menu
On launch the system displays a 12-item menu:
```
========================================
HOSPITAL PATIENT MANAGEMENT SYSTEM
========================================
1. Add New Patient
2. Display All Patients

3. Search Patient by ID
4. View Specific Patient Details
5. Update Patient Information
6. Delete Patient

7. Add Doctor Information
8. Display Doctors
9. Assign Doctor to Patient
10. Record Diagnosis and Treatment
11. Calculate Patient Bill
12. Exit Program
========================================
```
- Type a number between `1` and `12` and press Enter
- Enter requested data fields as prompted
- To cancel or skip optional fields during updates leave the prompt blank and press Enter
## 10. Example Usage
### Adding a Patient
1. Select option `1`
2. Input Patient ID: `P301`
3. Input Name: `Sarah Jenkins`
4. Input Age: `28`
5. Input Gender: `Female`
6. Input Phone: `555-4321`
7. Input Address: `100 River Road`
8. Input Blood Group: `B+`
9. Input Initial Diagnosis: `Acute Appendicitis`
10. Input Treatment: `Post-surgery recovery`
11. Input Room Number: `105`
12. Select Insurance (`1` for Yes, `0` for No)
13. Select Emergency (`1` for Yes, `0` for No)
### Generating a Bill
1. Select option `11`
2. Enter Patient ID: `P301`
3. Enter Consultation Fee: `150.0`
4. Enter Number of Room Days: `3`
5. Enter Daily Room Rate: `200.0`
6. Enter Medicine/Lab Charges: `250.0`
7. The system outputs an itemized receipt and attaches the billing summary to the patient record.
## 11. Sample input and output
### Sample Bill Output:
```
========================================
PATIENT BILL RECEIPT
========================================
Patient ID: P201
Patient Name: Alice Johnson
Doctor: Dr. Robert Smith
----------------------------------------
Consultation Fee: $150.0
Room Charges:   $600.0
Medicine Charges: $250.0
----------------------------------------
Subtotal:     $1000.0
Discount (Ins): -$150.0
Net Amount Due:  $850.0
Avg Daily Cost:  $283.33
========================================
```
## 12. Limitations
- Volatile Storage: All records are in memory. Terminating the program clears all newly added data
- Single Terminal Session: Designed for single operator in a single terminal session
- Basic Search: Searches are performed by exact match of Patient ID or Doctor ID
## 13. Future Improvements
- Integrate file storage (text or structured) once learned in future units
- Implement name searching and advanced record sorting algorithms