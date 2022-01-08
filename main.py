from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def root():
    return { "message": "Hello World" }

@app.get('/posts')
def getPosts():
    return { "data": "This is your post" }
