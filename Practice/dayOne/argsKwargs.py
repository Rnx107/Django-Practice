# https://medium.com/@devendra631995/understanding-args-and-kwargs-in-python-8a3222c9d2b3
#

# *args- Arguments
def greet(*args) -> None:
    for name in args:
        print(f"Hello, {name}")

greet("Alice", "Bob", "Alex")

"""Challenge 1: The Configurable HTML Tag Generator (**kwargs)
Goal: Practice mapping keyword arguments to string attributes.

Write a function make_tag(tag_name, content, **attributes) that generates an HTML string. The keyword arguments should be converted into attributes inside the opening tag.

Input: make_tag("a", "Click Here", href="https://google.com", target="_blank", cls="btn")

Special Requirement: Since class is a reserved keyword in Python, handle a keyword named cls by converting it to class in the output.

Expected Output: <a href="https://google.com" target="_blank" class="btn">Click Here</a>"""

def make_tag(tag_name, content, **attributes):
    #1. Convert cls to class
    if 'cls' in attributes:
        attributes['class'] = attributes.pop('cls')

    #2. Build a list using .items()
    attr_list =[]
    for key, value in attributes.items():
        attr_list.append(f'{key}="{value}"')

    #3. Convert List to String
    attr_string =" ".join(attr_list)
    
    attr_string = " "+attr_string

    print(f"<{tag_name}{attr_string}>{content}</{tag_name}>")

make_tag("a","Click Here", href="https://google.com", target="_blank", cls="btn")


"""Challenge 2: The Logic Pipeline (*args and **kwargs)
Goal: Practice passing arguments through a chain of functions.

Create a function called apply_operations(initial_value, *functions, **config) that takes an initial number and "pipes" it through a series of mathematical functions provided in *args.

The *args: Will be a list of functions (like lambda x: x + 2).

The **config: Should look for a key called precision. If it exists, round the final result to that many decimal places. If a key verbose=True is passed, print the result of each step.

Requirement: If no functions are provided in *args, return the initial_value as-is."""
from tabnanny import verbose


def apply_operations(initial_value, *args, **kwargs) -> None:
    new_value = initial_value
    for func in args:
        new_value = func(new_value)
        
        if kwargs.get("verbose"):
            print(f"step result: {new_value}")
    if "precision" in kwargs:
        new_value = round(new_value, kwargs["precision"])
    print(f"{initial_value} became {new_value}")

apply_operations(5,lambda x: x+2,lambda x: x**2, percision=2, verbose= True)