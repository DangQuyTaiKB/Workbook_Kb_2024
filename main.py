from fastapi import FastAPI
import json
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

# read json file
@app.get("/data")
async def read_json():
    with open('systemdata.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data




