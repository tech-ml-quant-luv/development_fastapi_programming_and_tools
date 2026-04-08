import turtle
import inspect

# members = inspect.getmembers(turtle)
# members = inspect.getmembers(turtle, inspect.isclass)
members = inspect.getmembers(turtle, inspect.isfunction)
for name, obj in members:
    print(name, obj)

# Get all the attributes
for name, obj in inspect.getmembers(turtle):
    if not (inspect.isclass(obj) or inspect.isfunction(obj)) and not name.startswith("__"):
        print(name, obj)

# Deep inspection

for name, cls in inspect.getmembers(turtle, inspect.isclass):
    if cls.__module__ != turtle.__name__:
        continue

    print(f"\nClass: {name}")

    for attr_name, attr_value in cls.__dict__.items():
        if not attr_name.startswith("__"):
            if inspect.isfunction(attr_value):
                print(f"  Method: {attr_name}()")
            else:
                print(f"  Attribute: {attr_name} = {attr_value}")