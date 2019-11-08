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

# -=-=-=-=-=-=-=-

# https://www.codewars.com/kata/59a8570b570190d313000037/train/python


def sum_cubes(n):
    sum = 0
    for x in range(n):
        sum += (x+1)**3
        print(sum)
    return sum

# better practice:
# def sum_cubes(n):
#     return sum(i**3 for i in range(0, n+1))


sum_cubes(1)

# test.assert_equals(sum_cubes(1), 1)
# test.assert_equals(sum_cubes(2), 9)
# test.assert_equals(sum_cubes(3), 36)
# test.assert_equals(sum_cubes(4), 100)
# test.assert_equals(sum_cubes(10), 3025)
# test.assert_equals(sum_cubes(123), 58155876)
