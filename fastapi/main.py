from fastapi import FastAPI #FastAPI is a python class that provides all the functionality for our API.

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