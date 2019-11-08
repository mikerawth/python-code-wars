# https://www.codewars.com/kata/calculate-bmi/train/python


def bmi(weight, height):
    bmi = weight/height**2
    if bmi <= 18.5:
        return "Underweight"
    elif bmi <= 25.0:
        return "Normal"
    elif bmi <= 30.0:
        return "Overweight"
    else:
        return "Obese"

# Test.describe("Basic tests")
# Test.assert_equals(bmi(50, 1.80), "Underweight")
# Test.assert_equals(bmi(80, 1.80), "Normal")
# Test.assert_equals(bmi(90, 1.80), "Overweight")
# Test.assert_equals(bmi(110, 1.80), "Obese")
# Test.assert_equals(bmi(50, 1.50), "Normal")
