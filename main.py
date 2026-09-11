#from fastapi import FastAPI
# http://127.0.0.1:8000/hello?name=Dhwani&age=20
#app = FastAPI()

#@app.get("/hello")
#def hello_world(name:str,age:int):
#    print("data->",name , age)
#    return {"message": f"Hello ,{name}!"}

#@app.post("/hello")
#def hello_world():
#    return {"message": "Hello , world!"}
from fastapi import FastAPI
from pydantic import BaseModel
# http://127.0.0.1:8000/hello/Dhwani
#app = FastAPI()

#@app.get("/hello/{name}/{age}")
#def hello_world(name:str,age:int):
#    print("data->",name , age)
#    return {"message": f"Hello , {name}-{age}!"}

#@app.post("/hello")
#def hello_world():
#    return {"message": "Hello , world!"}

app = FastAPI()

class PostHello(BaseModel):
    name:str
    age:int

@app.post("/hello")
def hello_world(post_hello: PostHello):
    print("data->",post_hello)
    return {"message": f"Hello , {post_hello.name}-{post_hello.age}!"}

@app.get("/hello/{name}/{age}")
def hello_world(name:str,age:int):
    print("data->",name , age)
    return {"message": f"Hello , {name}-{age}!"}