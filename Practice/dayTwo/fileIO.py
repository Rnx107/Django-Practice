# Python: file I/O, exceptions, context managers — script that reads a CSV and handles bad rows gracefully
file = open("data.csv", "w")
# reading from a file
content = file.read() # reads whole file asa string
lines = file.readlines()  # Reads file line by line
file.close() # it is essential to close the file to free system resources


# Context Managers
'''When a with statement is executed, Python calls the __enter__() method to acquire the resource (opening the file) and assigns the result to the variable specified after as. Upon exiting the block, the __exit__() method is automatically invoked to release the resource (closing the file), regardless of whether the block completed successfully or raised an exception. This mechanism is functionally equivalent to a try...finally block but significantly reduces boilerplate code. '''

with open("data.csv", "r") as file:
    for line in file:
        print(line.strip())
# file is automatically closed here

# Exception handling in python
""" ZeroDivisionError, TypeError, ValueError
    1. try, 2. except, 3. finally"""

def divide(a,b) -> None:
    try:
        result = a/b
        print("Result", result)
    except ZeroDivisionError:
        print("Cannot divide by zero")
    except TypeError:
        print("Please use numbers only")
    except ValueError:
        print("Error Invalid value")
    except Exception as e:
        print("error occured: ", e)
    finally:
        print("The setup is complete")

divide(10, 2)     # Works fine
divide(10, 0)     # ZeroDivisionError
divide("10", 2)   # TypeError