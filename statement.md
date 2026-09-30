# Project Statement: Hospital Patient Management System

Course: Python Essentials
Project Title: Hospital Patient Management System (HPMS)
Level: First-Year Undergraduate Coursework
---

Hence, the problem statement

In small-scale healthcare clinics, nursing homes, and regional community hospitals, patient registration, doctor scheduling, room occupancy allocation, and billing calculations are manually carried out on paper ledgers or disorganized spreadsheets.

This leads to several critical problems:
1. Room allocation mistakes: Beds getting double-booked or failure to deallocate rooms when patients are discharged
2. Billing inconsistencies: Computational errors in calculating daily room charges, physician fees, medicine expenses, and add-on services
3. Information fragmentation: Difficulty for clinic staff to quickly access a patient's complete profile and diagnosis and the attending doctor in one place

There is a need for a lightweight, transparent, and dependable management tool that can automate these routine operations without requiring heavy database servers, web setups, or proprietary software.
---

## Scope of the project

The Hospital Patient Management System is a standalone terminal-based software system built from core Python.

The features marked in-scope are:
• In-memory management of patient demographic and clinical records (ID, name, age, gender, contact, address, blood group, diagnosis, and treatment)
• Doctor management with active duty and availability tracking
• Doctor-to-patient pairing with validation of doctor availability
• Real-time tracking of occupied hospital rooms using a set structure to strictly prevent duplicate room assignments
• Itemized medical billing calculation with support for stay durations, daily rates, pharmacy costs, optional diagnostic service bundles using bitwise flags, and policy discounts
• Maintenance of an itemized financial charges ledger using Python's standard array('d', ...)
• Interactive command-line interface with safe input validation implemented purely without try/except

The features marked out-of-scope / future enhancements include:
• Persistent database storage (SQL/NoSQL, or external like CSV/JSON, as these lie outside the introductory course syllabus)
• Graphical User Interface (GUI) or web-based frontend interfaces
• Multi-user concurrent networking
---

## Target users

1. Hospital front desk / admission clerk:
Personnel responsible for registering new admissions, recording emergency patient details, assign available rooms and direct patients to appropriate doctors.
2. Medical clinic administrator:
Administrative personnel managing doctor duty rosters, update room allocations and check room availability.
3. Billing / discharge officer:
Accounting staff who needs to calculate transparent, itemized invoices, apply approved hospital discounts, and review the patient's billing charges prior to final discharge.