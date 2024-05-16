# Command-line BMI Calculator

def calculate_bmi(weight, height):
    
    # Calculates BMI based on weight (kg) and height (m).
    
    bmi = weight / (height ** 2)
    if bmi < 18.5:
        return bmi, "Underweight"
    elif 18.5 <= bmi < 25:
        return bmi, "Normal Weight"
    else:
        return bmi, "Overweight"

def main():
    try:
        weight = float(input("Enter your weight in kilograms: "))
        height = float(input("Enter your height in meters: "))
        bmi_value, bmi_category = calculate_bmi(weight, height)
        print(f"Your BMI is: {bmi_value:.2f}")
        print(f"Category: {bmi_category}")
    except ValueError:
        print("Invalid input. Please enter valid numeric values.")

if __name__ == "__main__":
    main()
