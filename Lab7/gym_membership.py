
def parse_plan(code):
    if not isinstance(code, str):
        raise ValueError("Plan code must be a string")

    if code.count('-') != 1:
        raise ValueError("Plan code must contain exactly one '-'")

    plan, months = code.split('-')

    if not plan.strip() or not months.strip():
        raise ValueError("Plan and months cannot be empty")

    try:
        months = int(months)
    except ValueError:
        raise ValueError("Months must be a valid integer")

    if months <= 0:
        raise ValueError("Months must be positive")

    return plan.upper(), months


def calculate_bmi(data):
    if not isinstance(data, str):
        raise ValueError("BMI data must be a string")

    if data.count(',') != 1:
        raise ValueError("Enter weight and height separated by one comma")

    weight, height = data.split(',')

    try:
        weight = float(weight)
        height = float(height)
    except ValueError:
        raise ValueError("Weight and height must be valid numbers")

    if weight <= 0 or height <= 0:
        raise ValueError("Weight and height must be positive")

    return round(weight / (height ** 2), 1)


def average_workout(minutes):
    if not isinstance(minutes, str):
        raise ValueError("Workout minutes must be a string")

    if not minutes.strip():
        raise ValueError("Workout minutes cannot be empty")

    try:
        values = [int(m) for m in minutes.split()]
    except ValueError:
        raise ValueError("Workout minutes must contain valid integers")

    if any(value < 0 for value in values):
        raise ValueError("Workout minutes cannot be negative")

    return sum(values) // len(values)


def main():
    print("==== Running parse_plan ====")
    user_input = input("Enter a plan code (e.g. GOLD-12): ")
    result = parse_plan(user_input)
    print("Plan and Months:", result)

    print("\n==== Running calculate_bmi ====")
    user_input = input("Enter weight and height (e.g. 70,1.75): ")
    result = calculate_bmi(user_input)
    print("BMI:", result)

    print("\n==== Running average_workout ====")
    user_input = input("Enter workout minutes separated by spaces (e.g. 45 60 30): ")
    result = average_workout(user_input)
    print("Average Minutes:", result)


if __name__ == "__main__":
    main()
