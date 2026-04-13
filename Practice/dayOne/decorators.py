# https://book.pythontips.com/en/latest/decorators.html

# --- Basic Decorator Example ---

def my_decorator(func):
    def wrapper():
        print("Beofre Function is called")
        func()
        print("After function is called")
    return wrapper

@my_decorator
def say_hello():
    print("Hello")

say_hello()


# --- Login Required Decorator Example ---

# User is not logged in
current_user = {"name": "Alice", "is_logged_in": False}

# checking for is_logged_in
def login_required(func):
    def wrapper(*args, **kwargs):
        if current_user.get("is_logged_in"):
            return func(*args, **kwargs)
        else:
            print("Access Denied, please login first")
            return None
    return wrapper

@login_required
def view_profile(user):
    print(f"Welcome to your profile, {user['name']}")

view_profile(current_user)


# --- Logger Decorator with Arguments (*args, **kwargs) ---

def logger(func):
    # *args collects positional arguments (like "Alice")
    # **kwargs collects keyword arguments (like age=25)
    def wrapper(*args, **kwargs):
        print(f"--- LOG: Running '{func.__name__}' ---")
        print(f"--- LOG: Arguments received: {args} {kwargs} ---")
        
        result = func(*args, **kwargs) # Pass everything into the real function
        
        print(f"--- LOG: '{func.__name__}' finished successfully ---")
        return result
    return wrapper

@logger
def add_user_to_database(name, email, age=None):
    print(f"Saving {name} ({email}) to the database...")

@logger
def process_payment(amount, currency="USD"):
    print(f"Processing payment of {amount} {currency}...")

# Testing with different amounts of data:
add_user_to_database("Alice", "alice@example.com", age=30)
print("\n") # Just for spacing
process_payment(99.99)