class BMI:
    def __init__(self, weight_kg, height_cm):
        if weight_kg <= 0 or height_cm <= 0:
            raise ValueError("Weight and height must be positive numbers.")
        self.weight = weight_kg
        self.height_m = height_cm / 100  # convert cm to meters
        self.bmi = None
    
    def calculate(self):
        self.bmi = round(self.weight / (self.height_m ** 2), 2)
        return self.bmi

class HealthTips:
    def __init__(self, bmi):
        self.bmi = bmi
        self.category = None
        self.tips = None
    
    def categorize(self):
        if self.bmi < 18.5:
            self.category = "Underweight"
        elif 18.5 <= self.bmi < 24.9:
            self.category = "Normal weight"
        elif 25.0 <= self.bmi < 29.9:
            self.category = "Overweight"
        else:
            self.category = "Obese"
        return self.category
    
    def get_tips(self):
        if self.category == "Underweight":
            self.tips = (
                "Consider nutrient-rich meals to gain healthy weight.\n"
                "Include protein-rich foods like lean meats, legumes, and dairy.\n"
                "Increase healthy fats in your diet such as avocados, nuts, and olive oil.\n"
                "Eat frequent small meals throughout the day.\n"
                "Avoid empty calories from sugary drinks and junk food.\n"
                "Engage in strength training to build muscle mass.\n"
                "Consult a healthcare professional for personalized guidance.\n"
                "Ensure adequate hydration and sleep."
            )
        elif self.category == "Normal weight":
            self.tips = (
                "Maintain your weight through a balanced diet and regular exercise.\n"
                "Consume plenty of fruits, vegetables, whole grains, and lean proteins.\n"
                "Stay hydrated by drinking enough water daily.\n"
                "Make time for at least 150 minutes of moderate aerobic activity per week.\n"
                "Incorporate strength training exercises twice a week.\n"
                "Avoid smoking and limit alcohol consumption.\n"
                "Manage stress through mindfulness or relaxation techniques.\n"
                "Get regular health check-ups to monitor wellbeing."
            )
        elif self.category == "Overweight":
            self.tips = (
                "Increase physical activity; aim for at least 150-300 minutes of moderate exercise each week.\n"
                "Focus on a balanced diet rich in whole foods—vegetables, fruits, lean proteins, and whole grains.\n"
                "Limit processed foods, sugary drinks, and high-fat snacks.\n"
                "Practice mindful eating and portion control.\n"
                "Track your food intake and physical activity to stay motivated.\n"
                "Drink plenty of water and reduce intake of high-calorie beverages.\n"
                "Consider consulting a registered dietitian or nutritionist for tailored advice.\n"
                "Ensure sufficient sleep and reduce stress which can impact weight."
            )
        else:  # Obese
            self.tips = (
                "Seek professional medical advice for comprehensive weight management.\n"
                "Adopt a low-calorie, nutrient-dense diet focusing on whole foods.\n"
                "Gradually increase physical activity, working up to at least 150 minutes per week.\n"
                "Join support groups or counseling programs to stay motivated.\n"
                "Avoid fad diets or extreme weight loss methods.\n"
                "Monitor blood pressure, blood sugar, and cholesterol regularly.\n"
                "Consider behavioral therapy to help with lifestyle changes.\n"
                "Prioritize mental health, sleep quality, and stress management.\n"
                "Work with healthcare providers to address any related health conditions."
            )
        return self.tips

def get_user_data():
    try:
        weight = float(input("Enter your weight in kilograms: "))
        height = float(input("Enter your height in centimeters: "))
        return weight, height
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return None, None

def display_results(bmi, category, tips):
    print(f"\nYour BMI is: {bmi}")
    print(f"Category: {category}")
    print("\nHealth Tips:")
    print(tips)

def main():
    print("Welcome to the BMI Calculator with Health Tips")

    weight, height = get_user_data()
    if weight is None or height is None:
        print("Exiting due to invalid input.")
        return

    try:
        bmi_calculator = BMI(weight, height)
        bmi_value = bmi_calculator.calculate()

        tips_provider = HealthTips(bmi_value)
        category = tips_provider.categorize()
        tips = tips_provider.get_tips()

        display_results(bmi_value, category, tips)

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
