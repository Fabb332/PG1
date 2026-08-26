def calculate_bill():
    # Define constants
    BASE_CONSULTATION_FEE = 100[cite: 1]
    LAB_TEST_RATE = 10[cite: 1]

    # Input and validate Patient Type
    while True:
        patient_type = (
            input("Enter patient type (Subsidised/Private): ").strip().capitalize()
        )
        if patient_type in ["Subsidised", "Private"]:[cite: 1]
            break
        print(
            "Error: Invalid patient type. Please enter 'Subsidised' or 'Private'."
        )[cite: 1]

    # Input and validate Number of Lab Tests
    while True:
        lab_input = input("Enter the number of lab tests completed: ").strip()[cite: 1]
        if lab_input.isdigit():[cite: 1]
            lab_tests = int(lab_input)
            break
        print(
            "Error: Number of lab tests must be a non-negative whole number."
        )[cite: 1]

    # Calculate Subtotal
    subtotal = BASE_CONSULTATION_FEE + (lab_tests * LAB_TEST_RATE)[cite: 1]

    # Apply discount based on patient type
    if patient_type == "Subsidised":[cite: 1]
        total = subtotal * 0.70[cite: 1]
    else:
        total = float(subtotal)[cite: 1]

    # Display results
    print("\n--- Bill Summary ---")
    print(f"Patient Type: {patient_type}")[cite: 1]
    print(f"Total Amount to Pay: ${total:.2f}")[cite: 1]


# Example usage:
if __name__ == "__main__":
    calculate_bill()