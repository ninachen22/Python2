# greet = lambda name: print("Hello " + name + "!")
def greet(name):
    """
    takes a name parameter and prints greeting with name
    """
    print("Hello " + name + "!")
greet("Nina")

def name_input():
    """
    asks user to input name and returns input as string
    """
    name = input("Please enter your name: ")
    return name

greet(name_input())