from enum import Enum
from fastapi import FastAPI
from typing import Literal


#In standard Python, you can put any data into any variable, and Python won't complain until the code actually runs and crashes. The typing module lets you define what should be in those variables before you even run the code. With typing: You add "hints." You aren't forcing the computer to change how it works; you are telling your IDE (PyCharm) and Frameworks (FastAPI) what to expect.

#FastAPI is unique because it doesn't just treat types as hints; it uses them as instructions.

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

literal = Literal["alexnet","resnet","lenet"]
# Literal is a specialized tool from the typing module. It literally means: "This variable must be exactly one of these specific strings."

app = FastAPI()


# The Interactive Docs (/docs)
# With Enum/Literal: You get a nice Dropdown Menu.
# Manual: You get a plain Text Box. The user has to guess or read your documentation to know what to type.

@app.get("/")
async def root():
    return "Welcome Bitch!"

@app.get("/models/{model_name}")
async def get_model(model_name: literal):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet": #You can get the actual value (a str in this case) using model_name.value, or in general, your_enum_member.value:
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}

# Because the available value for the path parameter are predefined, the interactive docs can show them nicely.


#In this case, the name of the parameter is a filepath and the last part :path, tells it that paramater should match any path
@app.get("/test/{test}")
async def test_path(test):
    return test
#The requested url will be http://127.0.0.1:8000/test/test

@app.get("/{file_path:path}")
async def read_file(filepath: str):
    return {"file_path": filepath}
#The requested url will be http://127.0.0.1:8000/{file_path}?filepath=test_path

#You might need the parameter to contain /home/johndoe/myfile.txt, with a leading slash (/).

# In that case, the URL would be: /files//home/johndoe/myfile.txt, with a double slash (//) between files and home.





