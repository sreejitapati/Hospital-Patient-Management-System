from array import array

FLAG_INSURANCE = 1
FLAG_EMERGENCY = 2

def check_numeric_val(chk_val):
    if type(chk_val) == int or type(chk_val) == float:
        return True
    return False

def calculate_bill(consult_fee, room_days, daily_rate, med_charge, s_flags):
    if not (check_numeric_val(consult_fee) and check_numeric_val(daily_rate) and check_numeric_val(med_charge)):
        return None

    rm_charge = room_days * daily_rate
    charges_arr = array('d', [float(consult_fee), float(rm_charge), float(med_charge)])

    sub_tot = 0.0
    for chg in charges_arr:
        sub_tot += chg

    disc_amt = 0.0
    if (s_flags & FLAG_INSURANCE) != 0:
        disc_amt = (sub_tot * 15) / 100

    net_tot = consult_fee + room_days * daily_rate + med_charge - disc_amt

    avg_day_cost = 0.0
    if room_days > 0:
        avg_day_cost = net_tot / room_days

    res_tuple = (sub_tot, disc_amt, net_tot, avg_day_cost, charges_arr)
    return res_tuple

def display_bill_slip(p_obj, b_tuple):
    print("========================================")
    print("          PATIENT BILL RECEIPT          ")
    print("========================================")
    print("Patient ID: " + str(p_obj.pat_id))
    print("Patient Name: " + str(p_obj.p_name))
    print("Doctor: " + ("Unassigned" if p_obj.assigned_doc is None else str(p_obj.assigned_doc.d_name)))
    print("----------------------------------------")
    print("Consultation Fee: $" + str(b_tuple[4][0]))
    print("Room Charges:     $" + str(b_tuple[4][1]))
    print("Medicine Charges: $" + str(b_tuple[4][2]))
    print("----------------------------------------")
    print("Subtotal:         $" + str(b_tuple[0]))
    print("Discount (Ins):  -$" + str(b_tuple[1]))
    print("Net Amount Due:   $" + str(b_tuple[2]))
    print("Avg Daily Cost:   $" + str(round(b_tuple[3], 2)))
    print("========================================")
