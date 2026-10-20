# -----------------------------------------------------------
# Staff Salary Management System
# -----------------------------------------------------------

import sys

# Global list to store staff records
staff_list = []

# Fixed National Insurance (NI) deduction per month
FIXED_NI = 200
TAX_THRESHOLD = 12570
TAX_RATE = 0.20


# -----------------------------
# Additional Features
# -----------------------------

def calculate_net_salary(gross_pay):
    """Calculate net salary after tax and NI."""
    if gross_pay > TAX_THRESHOLD:
        taxable_income = gross_pay - TAX_THRESHOLD
        tax = taxable_income * TAX_RATE
    else:
        tax = 0

    total_deductions = tax + FIXED_NI
    net_salary = gross_pay - total_deductions
    return gross_pay, tax, FIXED_NI, net_salary


def display_payslip(staff):
    """Display formatted payslip for a staff member."""
    gross, tax, ni, net = calculate_net_salary(staff['hours'] * staff['rate'])
    print("\n------ PAYSLIP ------")
    print(f"Name: {staff['name']}")
    print(f"Hours Worked: {staff['hours']}")
    print(f"Hourly Rate: £{staff['rate']:.2f}")
    print(f"Gross Pay: £{gross:.2f}")
    print(f"Tax Deducted: £{tax:.2f}")
    print(f"NI Deduction: £{ni:.2f}")
    print(f"Net Pay: £{net:.2f}")
    print("----------------------\n")


# -----------------------------
# Main Features
# -----------------------------

#------------------------------
# 1. Add new staff
#------------------------------
def add_staff():
    """Add a new staff record."""
    name = input("Enter staff name: ").strip()
    try:
        rate = float(input("Enter hourly rate (£): "))
        hours = float(input("Enter hours worked: "))
    except ValueError:
        print("Invalid input. Please enter numeric values for rate and hours.")
        return

    staff = {'name': name, 'rate': rate, 'hours': hours}
    staff_list.append(staff)
    print(f"Staff '{name}' added successfully.\n")

#-------------------------
# 2. Show all the staffs
#-------------------------

def view_staff():
    """Display list of all staff members."""
    if not staff_list:
        print("No staff records found.\n")
        return

    print("\n--- Staff List ---")
    for i, s in enumerate(staff_list, start=1):
        print(f"{i}. {s['name']} - £{s['rate']:.2f}/hr, {s['hours']} hrs")
    print("------------------\n")

#------------------------------------------
# 3. Search staff and view their payslip
#------------------------------------------

def search_staff():
    """Search staff by name."""
    name = input("Enter staff name to search: ").strip().lower()
    found = False
    for s in staff_list:
        if s['name'].lower() == name:
            display_payslip(s)
            found = True
            break
    if not found:
        print("No matching staff found.\n")

#---------------------------------
# 4. Delete a staff
#---------------------------------

def delete_staff():
    """Delete a staff record by name."""
    name = input("Enter staff name to delete: ").strip().lower()
    for s in staff_list:
        if s['name'].lower() == name:
            staff_list.remove(s)
            print(f"Staff '{name}' removed successfully.\n")
            return
    print("No matching staff found.\n")

#-----------------------------------
# 5. Compare salaries of two staffs
#-----------------------------------

def compare_salaries():
    """Compare salaries between two staff members."""
    if len(staff_list) < 2:
        print("At least two staff records are required for comparison.\n")
        return

    name1 = input("Enter first staff name: ").strip().lower()
    name2 = input("Enter second staff name: ").strip().lower()

    staff1 = next((s for s in staff_list if s['name'].lower() == name1), None)
    staff2 = next((s for s in staff_list if s['name'].lower() == name2), None)

    if not staff1 or not staff2:
        print("One or both staff members not found.\n")
        return

    net1 = calculate_net_salary(staff1['hours'] * staff1['rate'])[3]
    net2 = calculate_net_salary(staff2['hours'] * staff2['rate'])[3]

    print("\n--- Salary Comparison ---")
    print(f"{staff1['name']}: £{net1:.2f}")
    print(f"{staff2['name']}: £{net2:.2f}")

    if net1 > net2:
        print(f"{staff1['name']} earns more than {staff2['name']}.")
    elif net2 > net1:
        print(f"{staff2['name']} earns more than {staff1['name']}.")
    else:
        print("Both have the same net pay.")
    print("--------------------------\n")


# -----------------------------
# Main Menu
# -----------------------------

def menu():
    """Display menu and handle user selection."""
    while True:
        print("===== STAFF SALARY SYSTEM =====")
        print("1. Add Staff")
        print("2. View Staff List")
        print("3. Search Staff & View Payslip")
        print("4. Delete Staff")
        print("5. Compare Salaries")
        print("6. Exit")
        choice = input("Select an option (1-6): ")

        if choice == '1':
            add_staff()
        elif choice == '2':
            view_staff()
        elif choice == '3':
            search_staff()
        elif choice == '4':
            delete_staff()
        elif choice == '5':
            compare_salaries()
        elif choice == '6':
            print("Exiting the system. Goodbye!")
            sys.exit()
        else:
            print("Invalid choice. Please try again.\n")


# -----------------------------
# Run Program
# -----------------------------
if __name__ == "__main__":
    menu()
