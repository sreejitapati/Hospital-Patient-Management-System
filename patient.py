class Patient:
    def __init__(self, pat_id, p_name, p_age, p_gender, p_phone, p_address, p_blood, p_disease="Under Observation", p_treatment="None", p_room=0, service_flags=0):
        self.pat_id = pat_id
        self.p_name = p_name
        self.p_age = p_age
        self.p_gender = p_gender
        self.p_phone = p_phone
        self.p_address = p_address
        self.p_blood = p_blood
        self.p_disease = p_disease
        self.assigned_doc = None
        self.p_treatment = p_treatment
        self.p_room = p_room
        self.service_flags = service_flags
        self.bill_summary = None

    def display_info(self):
        doc_info = "Unassigned"
        if self.assigned_doc is not None:
            doc_info = str(self.assigned_doc.d_name) + " (" + str(self.assigned_doc.d_spec) + ")"

        ins_status = "No"
        if (self.service_flags & 1) != 0:
            ins_status = "Yes"

        emerg_status = "Standard"
        if (self.service_flags & 2) != 0:
            emerg_status = "Emergency"

        print("Patient ID: " + str(self.pat_id))
        print("Name: " + str(self.p_name))
        print("Age: " + str(self.p_age))
        print("Gender: " + str(self.p_gender))
        print("Phone: " + str(self.p_phone))
        print("Address: " + str(self.p_address))
        print("Blood Group: " + str(self.p_blood))
        print("Diagnosis: " + str(self.p_disease))
        print("Assigned Doctor: " + doc_info)
        print("Treatment: " + str(self.p_treatment))
        print("Room Number: " + str(self.p_room))
        print("Insurance Covered: " + ins_status)
        print("Admission Type: " + emerg_status)
        if self.bill_summary is not None:
            print("Total Billed: $" + str(self.bill_summary[2]))
        else:
            print("Total Billed: Not Generated")
        print("------------------------------")

    def update_contact(self, new_phone, new_addr):
        if new_phone != "":
            self.p_phone = new_phone
        if new_addr != "":
            self.p_address = new_addr

    def set_diagnosis(self, new_disease, new_treatment):
        if new_disease != "":
            self.p_disease = new_disease
        if new_treatment != "":
            self.p_treatment = new_treatment

