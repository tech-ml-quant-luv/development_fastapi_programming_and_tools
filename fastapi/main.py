from fastapi import FastAPI #FastAPI is a python class that provides all the functionality for our API.
import random
#LEVEL 1

app = FastAPI() #By this we create a fastapi instance. Here the app variable will be an "instance" of the class FastAPI.
#This app will be the main point of interaction to create all our API

#adding our first endpoint/path/route. "Path" here refers to the last part of the URL starting from the first /.
#Operations are one of the HTTP methods. - GET, POST, PUT, DELETE

@app.get("/")
async def root():
    return {"message": "Hello Other world"}


# The @app.get("/") tells fastAPI that the function right below is in charge of handling requests that go to:
# The path /
# Using the operator get

# That @something syntax in pythong is called a "decorator". We will put it on toop of a function. Like a pretty decorative hat( I guess that's where the term came from').
# A "decorator" takes the function below and does something with it.
# In the case of FastAPI, the decorator tells FastAPI that the function below corresponds to the path / with an operation get.
# It is the "path operation decorator"

# we can also have other path operation decorators like - @app.post(), @app.put(), @app.delete()

# the python function below the "decorator" is the path operation function. This function will be called by the FastAPI whenever it receives a request to the URL "/" using the GET operation.  In this case it is an async function.

@app.get("/normal")
def func():
    return {"message": "Normal Function"}

# Last it the return function. We can return a dict, list, singular values as str, int etc. We can also return pydantic models

#-------------------------------------------------------------------------------------------------------------------------

#LEVEL 2

@app.get("/items/{item_id}")
async def read_item(item_id):
    return {"Your updated ID is": int(item_id)+random.randint(0,5)}

#The value fo the path parameter item_id will be passed to our function as the argument item_id

# We can declare the type of the path parameter in the function, using standard python type annotations 0 this will give us editor support inside our function with error checks, completions etc.


@app.get("/items_with_type/{item_id}")
async def read_item(item_id: int):
    return {"Your updated ID is": item_id+random.randint(0,5)}

# with that type declaration, FastAPI gives you automatic request "parsing".

# But if you go to the browser at http://127.0.0.1:8000/items/foo, you will see a nice HTTP error. This is because the path parameter item_id had a value of "foo" which is not an int. This would be same if we provide a float value instead of an int.

# So, with the same Python type declaration, FastAPI gives you data validation.
# Notice that the error also clearly states exactly the point where the validation didn't pass.
# This is incredibly helpful while developing and debugging code that interacts with your API.

# Note - All the data validation is performed under the hood by Pydantic, so we get all the benefits from it.

# Order matters
# When creating path operations, you can find situations where you have a fixed path.
# Like /users/me, let's say that it's to get data about the current user.
# And then you can also have a path /users/{user_id} to get data about a specific user by some user ID. Because path operations are evaluated in order, you need to make sure that the path for /users/me is declared before the one for /users/{user_id}:














