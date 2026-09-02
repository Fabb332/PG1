def assign_triage_room():
    """
    Handles triage room assignment with input validation.
    Severity must be a whole number from 1 to 10.
    1-4 = Waiting Room
    5-7 = Room 1
    8-10 = Room 2
    """

    print("\n=== ASSIGN TRIAGE ROOM ===")

    # 1. Input and validate Severity
    while True:
        severity_str = input("Enter severity level (1-10): ").strip()

        try:
            severity = int(severity_str)

            # Check if severity is within the valid range
            if 1 <= severity <= 10:
                break
            else:
                print("[Error] Severity must be a whole number from 1 to 10.\n")

        except ValueError:
            print("[Error] Invalid input. Please enter a whole number from 1 to 10.\n")

    # 2. Assign Triage Room
    if 1 <= severity <= 4:
        room = "Waiting Room"
    elif 5 <= severity <= 7:
        room = "Room 1"
    else:
        room = "Room 2"

    # 3. Output Triage Summary
    print("\n--- Triage Summary ---")
    print(f"Severity Level : {severity}")
    print(f"Assigned Room  : {room}")
    print("Status         : Triage room successfully assigned!")
    print("----------------------\n")


# Allows you to test your function directly
if __name__ == "__main__":
    assign_triage_room()
