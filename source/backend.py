def metric_input():
    weight = float(input("What's your weight (kg)? "))
    height = float(input("What's your height (cm)? "))
    return [weight, height]


def bmi_calculation(metric_input):
    weight = metric_input[0]
    height = metric_input[1] / 100
    bmi = weight / height ** 2
    return bmi


def bmi_evaluation(index):
    if index < 18.5:
        index_class = "Underweight"
    elif index < 25:
        index_class = "Normal weight"
    elif index < 30:
        index_class = "Overweight"
    elif index < 35:
        index_class = "Class I Obesity"
    elif index < 40:
        index_class = "Class II Obesity"
    else:
        index_class = "Class III Obesity"
    return index_class


def run():
    bmi = bmi_calculation(metric_input())
    index_class = bmi_evaluation(bmi)
    print(f"Your BMI is {bmi:.2f} and your classification is {index_class}")


run()