from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == "POST":

        name = request.form["patient_name"]
        age = request.form["patient_age"]
        patient_id = request.form["patient_id"]

        # Validation
        if name.strip() == "":
            return "Error: Name cannot be blank."

        if patient_id.strip() == "":
            return "Error: Patient ID cannot be blank."

        try:
            age = int(age)

            if age <= 0:
                return "Error: Age must be positive."

        except ValueError:
            return "Error: Please enter a valid age."

        return f"""
        Patient Successfully Registered!<br><br>

        Name: {name}<br>
        Age: {age}<br>
        ID: {patient_id}
        """

    return render_template("register_patient.html")


if __name__ == "__main__":
    app.run(debug=True)
