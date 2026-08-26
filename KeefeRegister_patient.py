def register_patient():

    while True:
        name = input("Enter Patient Name: ")

        if name.strip() != "":
            break

        print("Error: Name cannot be blank.")

    while True:
        try:
            age = int(input("Enter Patient Age: "))

            if age > 0:
                break

            print("Error: Age must be positive.")

        except ValueError:
            print("Error: Please enter a valid number.")

    while True:
        patient_id = input("Enter Patient ID: ")

        if patient_id.strip() != "":
            break

        print("Error: ID cannot be blank.")

    print("\n===== PATIENT DETAILS =====")
    print("Name:", name)
    print("Age:", age)
    print("ID:", patient_id)

    print("\nPatient Successfully Registered!")


# Call the function
register_patient()
