def exponentiate(x, y):
    """
    raises x to the y power
    """
    return x ** y

def raise_to_fourth_power(x):
    """
    calls exponentiate fx to raise this parameter to 4th power
    """
    return exponentiate(x, 4)

square = lambda x: exponentiate(x, 2)
cube = lambda x: exponentiate(x, 3)

print(square(2))
print(cube(2))
print(raise_to_fourth_power(2))