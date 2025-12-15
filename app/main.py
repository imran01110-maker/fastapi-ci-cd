from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def health():
    print("Health check")
    return {"status": "ok"}


@app.get("/sum")
def sum(a:int,b:int)->dict:
    return {"result":a+b}