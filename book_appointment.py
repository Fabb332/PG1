from datetime import datetime, timedelta

def book_appointment():
    """
    Handles appointment booking with input validation for department selection
    and date checking (must be > 7 days from current date).
    """
    current_date = datetime.now().date()
    # Calculate threshold date (must be strictly greater than current_date + 7 days)
    min_date = current_date + timedelta(days=7)

    print("\n=== BOOK APPOINTMENT ===")

    # 1. Input and validate Department
    while True:
        print("Select Department:")
        print("1. GP")
        print("2. Specialist")
        dept_choice = input("Enter choice (1 or 2): ").strip()

        if dept_choice == "1":
            department = "GP"
            break
        elif dept_choice == "2":
            department = "Specialist"
            break
        else:
            print("[Error] Invalid choice. Please enter 1 for GP or 2 for Specialist.\n")

    # 2. Input and validate Appointment Date
    while True:
        date_str = input("\nEnter preferred date (YYYY-MM-DD): ").strip()
        try:
            chosen_date = datetime.strptime(date_str, "%Y-%m-%d").date()
            
            # Date must be MORE than 7 days from today
            if chosen_date > min_date:
                break
            else:
                print(f"[Error] Date must be strictly more than 7 days from today (After {min_date}).")
        except ValueError:
            print("[Error] Invalid date format or non-existent date. Use YYYY-MM-DD.")

    # 3. Output Confirmation
    print("\n--- Booking Confirmation ---")
    print(f"Department   : {department}")
    print(f"Date         : {chosen_date}")
    print("Status       : Appointment successfully booked!")
    print("-----------------------------\n")


# Allows you to test your function directly
#####
if __name__ == "__main__":
    book_appointment()
