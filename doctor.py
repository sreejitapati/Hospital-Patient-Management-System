class Doctor:
    def __init__(self, doc_id, d_name, d_spec, d_phone, d_avail=True):
        self.doc_id = doc_id
        self.d_name = d_name
        self.d_spec = d_spec
        self.d_phone = d_phone
        self.d_avail = d_avail

    def display_info(self):
        status_str = "Available"
        if not self.d_avail:
            status_str = "Not Available"
        print("Doctor ID: " + str(self.doc_id))
        print("Name: " + str(self.d_name))
        print("Specialization: " + str(self.d_spec))
        print("Phone: " + str(self.d_phone))
        print("Status: " + status_str)
        print("------------------------------")

    def set_availability(self, new_status):
        self.d_avail = new_status
