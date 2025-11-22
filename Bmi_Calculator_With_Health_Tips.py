def get_health_tip(bmi):
    if bmi <= 18.4:
        return (
            "You are underweight.\n"
            "Tips:\n"
            "- Increase your calorie intake with nutritious, calorie-dense foods like nuts, dairy, and whole grains.\n"
            "- Eat small, frequent meals to gain weight gradually.\n"
            "- Incorporate strength training exercises to build muscle mass.\n"
            "- Consult a healthcare provider or dietitian to rule out underlying issues."
        )
    elif bmi <= 24.9:
        return (
            "You are in a healthy weight range.\n"
            "Tips:\n"
            "- Maintain a balanced diet with plenty of fruits, vegetables, lean protein, and whole grains.\n"
            "- Stay physically active with at least 150 minutes of moderate aerobic exercise weekly.\n"
            "- Keep hydrated and get regular sleep.\n"
            "- Continue regular health checkups to monitor wellbeing."
        )
    elif bmi <= 29.9:
        return (
            "You are overweight.\n"
            "Tips:\n"
            "- Reduce intake of sugary drinks, processed foods, and high-fat snacks.\n"
            "- Increase cardiovascular exercises like walking, cycling, or swimming.\n"
            "- Control portion sizes and focus on nutrient-dense foods.\n"
            "- Set realistic, gradual weight-loss goals."
        )
    elif bmi <= 34.9:
        return (
            "You are in the obese category (Class I).\n"
            "Tips:\n"
            "- Consult a healthcare professional to develop a weight management plan.\n"
            "- Combine a calorie-controlled diet with regular, supervised physical activity.\n"
            "- Consider behavioral therapy or support groups.\n"
            "- Monitor for obesity-related health issues such as diabetes and hypertension."
        )
    elif bmi <= 39.9:
        return (
            "You are in the obese category (Class II).\n"
            "Tips:\n"
            "- Medical evaluation is important to assess health risks.\n"
            "- A structured diet and exercise program under medical guidance is recommended.\n"
            "- Discuss possible medical treatments or interventions with your doctor.\n"
            "- Mental health support may also be beneficial."
        )
    else:
        return (
            "You are in the severely obese category (Class III).\n"
            "Tips:\n"
            "- Immediate consultation with healthcare providers is crucial.\n"
            "- Intensive lifestyle changes, medical treatment, and possibly surgery may be required.\n"
            "- Regular monitoring of cardiovascular, respiratory, and metabolic health is essential.\n"
            "- Psychological support and counseling can help manage lifestyle adjustments."
        )

def bmi_calculator():
    try:
        weight = float(input("Enter your weight in kg: "))
        height = float(input("Enter your height in cm: "))
        if weight <= 0 or height <= 0:
            print("Weight and height must be positive numbers.")
            return
        bmi = weight / ((height / 100) ** 2)
        print(f"Your BMI is: {bmi:.2f}")
        print(get_health_tip(bmi))
    except ValueError:
        print("Please enter valid numbers for weight and height.")

bmi_calculator()
