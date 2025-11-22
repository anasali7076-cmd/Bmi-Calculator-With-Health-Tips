# Project Statement: BMI Calculator with Health Tips

## 1. Problem Statement
Body Mass Index (BMI) is a widely recognized screening tool for identifying potential weight-related health issues in adults. However, a raw BMI number is often abstract and insufficient for users to understand their actual health status. Without interpretation, users may not know if their weight falls within a healthy range or what steps they should take next.

There is a need for a simple, accessible tool that not only performs the mathematical calculation but also translates the data into meaningful categories and provides immediate, context-aware health advice to guide the user toward better well-being.

## 2. Scope of the Project
The scope of this project is limited to a text-based (Command Line Interface) utility that focuses on immediate assessment and advice.

* **In-Scope:**
    * **User Input:** Accepting weight (kg) and height (cm) from the user.
    * **Validation:** Ensuring data integrity by handling non-numeric or non-positive values to prevent runtime errors.
    * **Calculation:** computing BMI using the standard metric formula: $BMI = \text{weight} / (\text{height}/100)^2$.
    * **Categorization:** Mapping the calculated BMI into WHO standard ranges (Underweight, Normal, Overweight, Obese).
    * **Advisory:** Displaying curated, category-specific health tips to the user.

* **Out-of-Scope:**
    * Persistent data storage (database integration).
    * Graphical User Interface (GUI).
    * Medical diagnosis or professional treatment plans.
    * Support for Imperial units (lbs/inches).

## 3. Target Users
This application is designed for:
* **Health-Conscious Individuals:** People actively monitoring their fitness who need quick, self-service assessments.
* **General Public:** Individuals curious about their weight status who require a simple, no-frills tool without complex setups.
* **Healthcare Assistants & Students:** Users needing a reliable, quick method to double-check BMI calculations and recall standard lifestyle advice during basic screenings.

## 4. High-level Features
The application delivers four core functionalities designed to address the problem statement efficiently:

### 4.1. Robust Data Processing
To ensure reliability, the system includes an input validation layer.
* **Feature:** The `get_user_data()` function captures input and manages exceptions.
* **Mechanism:** It validates that inputs are numeric and positive, raising a `ValueError` for invalid data (e.g., weight $\le 0$), ensuring the application fails gracefully rather than crashing.

### 4.2. Precision Calculation
The core logic computes BMI with high precision using the metric system.
* **Feature:** The `BMI` class encapsulates the calculation logic.
* **Mechanism:** It automatically converts height from centimeters to meters and rounds the final result to two decimal places for readability.

### 4.3. Intelligent Categorization
The application automatically maps numerical results to health categories using standard thresholds:

| BMI Range ($kg/m^2$) | Category |
| :--- | :--- |
| **< 18.5** | Underweight |
| **18.5 – 24.9** | Normal weight |
| **25.0 – 29.9** | Overweight |
| **≥ 30.0** | Obese |

### 4.4. Context-Aware Health Guidance
Unlike simple calculators that only output a number, this system provides actionable logic via the `HealthTips` class.
* **Feature:** Dynamic tip generation based on the determined category.
* **Mechanism:** The system retrieves specific text blocks tailored to the user's status (e.g., suggesting nutrient-rich meals for underweight users versus cardiovascular exercise for overweight users), providing the user with immediate "next steps."