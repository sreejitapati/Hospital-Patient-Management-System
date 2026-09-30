class Hospital:
    def __init__(self, hosp_name):
        self.hosp_name = hosp_name
        self.patients_data = {}
        self.doctors_data = {}
        self.occupied_rooms = set()
        self.patient_ids_list = []
        self.all_blood_groups = ('A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-')
        self.departments = frozenset(['Cardiology', 'Neurology', 'Orthopedics', 'General', 'Pediatrics'])

    def add_patient(self, pat_obj):
        if pat_obj.pat_id in self.patients_data:
            return False
        self.patients_data[pat_obj.pat_id] = pat_obj
        self.patient_ids_list.append(pat_obj.pat_id)
        if pat_obj.p_room > 0:
            self.occupied_rooms.add(pat_obj.p_room)
        return True

    def get_patient(self, p_id):
        if p_id in self.patients_data:
            return self.patients_data[p_id]
        return None

    def show_all_patients(self):
        if len(self.patient_ids_list) == 0:
            print("No patients registered currently.")
            return
        print("===== REGISTERED PATIENTS LIST (" + str(len(self.patient_ids_list)) + ") =====")
        for cur_id in self.patient_ids_list:
            self.patients_data[cur_id].display_info()

    def remove_patient(self, p_id):
        if p_id not in self.patients_data:
            return False
        curr_pat = self.patients_data[p_id]
        if curr_pat.p_room in self.occupied_rooms:
            self.occupied_rooms.remove(curr_pat.p_room)
        del self.patients_data[p_id]
        self.patient_ids_list.remove(p_id)
        return True

    def add_doctor(self, doc_obj):
        if doc_obj.doc_id in self.doctors_data:
            return False
        self.doctors_data[doc_obj.doc_id] = doc_obj
        return True

    def get_doctor(self, d_id):
        if d_id in self.doctors_data:
            return self.doctors_data[d_id]
        return None

    def show_all_doctors(self):
        if len(self.doctors_data) == 0:
            print("No doctors registered currently.")
            return
        print("===== DOCTOR ROSTER (" + str(len(self.doctors_data)) + ") =====")
        for doc_key in self.doctors_data:
            self.doctors_data[doc_key].display_info()

    def assign_doctor_to_patient(self, p_id, d_id):
        if p_id not in self.patients_data or d_id not in self.doctors_data:
            return False
        pat_ref = self.patients_data[p_id]
        doc_ref = self.doctors_data[d_id]
        pat_ref.assigned_doc = doc_ref
        return True
